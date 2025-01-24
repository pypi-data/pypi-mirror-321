import logging

from openai import AzureOpenAI

from itsai.aspire.datastore.azure_ai_search import AzureAISearch
from itsai.aspire.vanna.openai import OpenAI_Chat


class App(AzureAISearch, OpenAI_Chat):
    def __init__(self, client: AzureOpenAI, config=None):
        AzureAISearch.__init__(self, config=config)
        OpenAI_Chat.__init__(self, client=client, config=config)

    def set_logger(self, logger: logging.Logger) -> None:
        self._logger = logger

    def log(self, message: str, title: str = 'Info'):
        self._logger.info(f'{title}: {message}')
