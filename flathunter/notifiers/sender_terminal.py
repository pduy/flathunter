from typing import Dict
from flathunter.abstract_notifier import Notifier
from flathunter.abstract_processor import Processor
from flathunter.config import YamlConfig


class SenderTerminal(Processor, Notifier):
    def __init__(self, config: YamlConfig) -> None:
        self.config = config

    def process_expose(self, expose: Dict) -> Dict:
        """Send a message to a Slack channel describing the expose"""
        message = self.config.message_format().format(
            title=expose['title'],
            rooms=expose['rooms'],
            size=expose['size'],
            price=expose['price'],
            url=expose['url'],
            address=expose['address'],
            durations="" if 'durations' not in expose else expose[
                'durations']).strip()
        self.notify(message)
        return expose
    
    def notify(self, message: str) -> None:
        print(message)
