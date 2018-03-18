from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

from outcome import predict_outcome 

class ActionPatientInfoRecurrence(Action):
    def name(self):
        return "patient_consultation_info"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Getting patient depression recurrence../")
        rec_info = predict_outcome()
 
class ActionPatientGeneralInfo(Action):
    def name(self):
        return "patient_general_info"    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Patient's general info")
        
                    
  
           
           
           
            
            
            