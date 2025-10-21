import logging

class ErrorHandler:
    #erro de colocar pdf em vez de image
    @staticmethod
    def handle_upload_error(error):
        """Erro relacionado ao upload de arquivos"""
        logging.error(f"Erro no upload de arquivo: {str(error)}")
    
    @staticmethod
    def handle_generic_error(error):
        """Erro genérico, capturado quando não se sabe a causa exata"""
        logging.error(f"Erro genérico: {str(error)}")