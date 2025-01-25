
import httpx
import requests
import logging
import os
import importlib

from telehook.types import Message, CallbackQuery
from telehook.filters import Filters
from telehook.methods import Methods


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TeleClient:
    def __init__(self, token, url=None, plugins=None):
        """
        Initialize the TeleClient.

        Args:
            token (str): Telegram Bot API token.
            url (str): Optional webhook URL for the bot.
            plugins (dict): Dictionary specifying plugin configuration (e.g., {"root": "server.plugins"}).
        """
        self.token = token
        self.url = url
        self.api_url = f"https://api.telegram.org/bot{self.token}/"
        self.message_handlers = []
        self.edited_message_handlers = []
        self.callback_query_handlers = []

        self.method = Methods(self)

        if plugins and "root" in plugins:
            self.plugins = plugins
            pass

    def load_plugins(self, root_path=None):
        """
        Dynamically load plugin modules from the specified root path.

        Args:
            root_path (str): Root path for plugins, e.g., "server.plugins".
        """
        if root_path == None:
            root_path = self.plugins["root"]
            
        try:
            # Import the root module
            root_module = importlib.import_module(root_path)
            # List all modules in the root
            root_dir = os.path.dirname(root_module.__file__)
            for filename in os.listdir(root_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = f"{root_path}.{filename[:-3]}"
                    importlib.import_module(module_name)
                    logger.info(f"Loaded plugin: {module_name}")
        except Exception as e:
            logger.error(f"Failed to load plugins from {root_path}: {e}")

    def setup_webhook(self):
        response = requests.post(
            f"{self.api_url}setWebhook",
            data={"url": f"{self.url}"}
        )

        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    async def process_update(self, update):
        """
        Process an incoming update.

        Args:
            update (dict): The Telegram webhook update.
        """
        if "message" in update:
            message = Message(self, update["message"])
            for handler, filter_ in self.message_handlers:
                if await filter_(self, message):
                    await handler(self, message)

        elif "edited_message" in update:
            edited_message = Message(self, update["edited_message"])
            for handler, filter_ in self.edited_message_handlers:
                if await filter_(self, edited_message):
                    await handler(self, edited_message)

        elif "callback_query" in update:
            callback_query = CallbackQuery(self, update["callback_query"])
            for handler, filter_ in self.callback_query_handlers:
                if filter_ is None or await filter_(self, callback_query):
                    await handler(self, callback_query)


    def on_message(self, filter_func):
        """
        Decorator to handle messages with a specific filter.

        Args:
            filter_func (function): A function that determines whether the handler should be called.

        Returns:
            function: The decorated function.
        """
        def decorator(func):
            self.message_handlers.append((func, filter_func))
            return func
        return decorator

    def on_edited(self, filter_func):
        """
        Decorator to handle edited messages with a specific filter.

        Args:
            filter_func (function): A function that determines whether the handler should be called.

        Returns:
            function: The decorated function.
        """
        def decorator(func):
            self.edited_message_handlers.append((func, filter_func))
            return func
        return decorator
    
    def on_callback_query(self, filter_func=None):
        """
        Decorator to handle callback queries with an optional filter.

        Args:
            filter_func (function, optional): A function that determines whether the handler should be called.

        Returns:
            function: The decorated function.
        """
        def decorator(func):
            self.callback_query_handlers.append((func, filter_func))
            return func
        return decorator
    


