import time
import json
import traceback
from fastapi import FastAPI, Request, HTTPException
from .base_metrics import MetricsBase
from fastapi.responses import JSONResponse

class FastAPIMetrics(MetricsBase):
    def init_app(self, app: FastAPI):
        """
        middleware para capturar e enviar as excessoes
        """
        @app.middleware("http")
        async def log_requests(request: Request, call_next):
            """
            Captura a request
            """
            start_time = time.time()
            try:
                duration = time.time() - start_time
                endpoint = request.url.path
                method = request.method
                response = await call_next(request)
                status_code = response.status_code
                self.logger.info(
                    f"Endpoint: {endpoint}, Method: {method}, Status: {status_code}, Duration: {duration:.4f}s"
                )
                return response
            except Exception as e:
                app_name = self.app_name if self.app_name else request.base_url
                duration = time.time() - start_time

                try:
                    body = await request.body()
                    decoded_body = body.decode('utf-8', errors='ignore')
                except Exception:
                    decoded_body = "Unable to parse body"

                error_data = {
                    "app_name": app_name,
                    "endpoint": request.url.path,
                    "full_url": str(request.url),
                    "method": request.method,
                    "status_code": 500 if not hasattr(e, "status_code") else e.status_code,
                    "duration": duration,
                    "headers": dict(request.headers),
                    "query_params": dict(request.query_params),
                    "request_body": str(json.loads(await request.body())) if request.headers.get("Content-Type")
                                           == "application/json" else decoded_body,
                    "client_ip":  request.client.host,
                    "user_agent": request.headers.get("user-agent", "N/A"),
                    "error_details": str(e),
                    "error_type": type(e).__name__,
                    "traceback": traceback.format_exc(),
                    "timestamp": time.time_ns() // 1_000_000
                }

                self.logger.error(error_data)
                self.send_to_providers(error_data)

                if isinstance(e, HTTPException):
                    raise e

                return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
