import logging
from error_dispatcher_client.templates import TemplateBase

class ErrorProvider:
    """
    Classe base Provider
    """
    def __init__(self, message_template: TemplateBase):
        self.logger = logging.getLogger("ErrorProvider")
        self.logger.setLevel(logging.INFO)
        self.message_template = message_template if message_template else TemplateBase()


    def send(self, error_data: dict):
        """
        Metodo que deve ser implementado por cada provedor.
        """
        raise NotImplementedError("O metodo `send` deve ser implementado.")
