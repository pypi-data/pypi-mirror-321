import logging
import threading
from typing import List
from .providers.base_provider import ErrorProvider


class MetricsBase:
    def __init__(self, providers: List["ErrorProvider"], app_name : str = None):
        """
        Classe base para criar métricas de erros.
        """
        self.logger = logging.getLogger("MetricsBase")
        self.logger.setLevel(logging.INFO)
        self.providers = providers
        self.app_name = app_name

    def send_to_providers(self, error_data: dict):
        """
        Envia o erro para todos os provedores de forma assíncrona usando threads.
        """
        threads = []
        for provider in self.providers:
            thread = threading.Thread(
                target=self._send_to_provider_thread_safe,
                args=(provider, error_data)
            )
            thread.start()
            threads.append(thread)

    def _send_to_provider_thread_safe(self, provider: "ErrorProvider", error_data: dict):
        """
        Envia o erro para um único provedor dentro de um thread.
        """
        try:
            provider.send(error_data)
            self.logger.info(f"Erro enviado com sucesso via {provider.__class__.__name__}")
        except Exception as e:
            self.logger.error(f"Falha ao enviar erro via {provider.__class__.__name__}: {e}")
