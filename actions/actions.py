from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.actions import Action
from rasa_sdk.events import SlotSet
import requests

class FetchProfileAction(Action):
    def name(self):
        return "action_fetch_profile"

    def run(self, dispatcher, tracker, domain):
        url = "http://myprofileurl.com"
        data = requests.get(url).json
        return [SlotSet("account_type", data["account_type"])]

class SetAINameAction(Action):
    def name(self):
        return "action_set_ai_name"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("ai_name", "Tu prima")]


class SetLatestScoreForFeelingAction(Action):
    def name(self):
        return "action_set_latest_score_feeling"


    def run(self, dispatcher, tracker, domain):
        SlotSet("account_type", data["account_type"])
        return []

class SetScoreForFeelingAction(Action):
    def name(self):
        return "action_set_score_feeling"

    def run(self, dispatcher, tracker, domain):
        # Save last score detected in DB
        # IF (we have detected a total of then 7 scores for any of the 3 feelings)
        #   Use the last 7 answers only lets calculate the DASS table avg
        #   If we do not have 7 lets extrapolate the value
        #   save the avg in the slots
        return []
