from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime as dtime
import time
import pytz
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from weather import Weather


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        print("junior")
        print(city)
        #temp=int(Weather(city)['temp']-273)
        temp=Weather(city)
        # dispatcher.utter_template("utter_temp",tracker,temp=temp)
        dispatcher.utter_message(text=f"DESCRIÇÃO: {temp}")
        dispatcher.utter_message(response="utter_goodbye")
        return []

# class ValidateTicketForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_ticket_form"

#     def validate_consult_ticket_id(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate consult_ticket_id value."""

#         return {"consult_ticket_id": slot_value}


# class ActionConsultTicketCallback(Action):

#     def name(self) -> Text:
#         return "action_consult_ticket_callback"

#     def run(self, dispatcher: CollectingDispatcher,
#     tracker: Tracker,
#     domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         if tracker.latest_message["text"] == "Sim":
#             # consult_ticket_id = tracker.get_slot("consult_ticket_id")
#             # description = tracker.get_slot("description") or "❌ Sem título"
#             # status = tracker.get_slot("status") or "❌ Sem status"

#             # dispatcher.utter_message(text=f"▶️ NÚMERO: {consult_ticket_id}<br>▶️ DESCRIÇÃO: {description}<br>▶️ STATUS: {status}")
#             dispatcher.utter_message(response="utter_consult_ticket_loading")
#             return []
#             # SlotSet("consult_ticket_id", None), SlotSet("description", None), SlotSet("status", None)]
                
#         dispatcher.utter_message(response="utter_consult_ticket_error")
#         return []
#         # SlotSet("consult_ticket_id", None), SlotSet("description", None), SlotSet("status", None)]

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
