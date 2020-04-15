from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.actions import Action
from rasa_sdk.events import SlotSet
import requests

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World!")

        return []



class FetchProfileAction(Action):
    def name(self):
        return "fetch_profile"

    def run(self, dispatcher, tracker, domain):
        url = "http://myprofileurl.com"
        data = requests.get(url).json
        return [SlotSet("account_type", data["account_type"])]