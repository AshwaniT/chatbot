# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSSAHelper(Action):

    def name(self) -> Text:
        return "action_ssa_helper"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        enitity = tracker.get_slot("wf_entity")
        actions=tracker.get_slot("wf_action")
        # business logic i want 
      
        dispatcher.utter_message("Here is the WIKI for {}:{}".format(enitity, actions))

        return [SlotSet("wf_entity", enitity),SlotSet("wf_action", actions)]
