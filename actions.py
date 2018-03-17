from rasa_core.actions import Action
from rasa_core.events import SlotSet
from outcome import predict_outcome

#class ActionCheckRestaurants(Action):
 #  def name(self):
      # type: () -> Text
  #    return "action_check_restaurants"

   #def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

    #  cuisine = tracker.get_slot('cuisine')
     # q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      #result = db.query(q)

      #return [SlotSet("matches", result if result is not None else [])]
f = []    

class ActionPatientInfoRecurrence(Action):
       
    def name(self):
        return "patient_consultation_info"
        
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Getting patient depression recurrence../")
        outcome = predict_outcome()
        f.append(outcome)
        
class ActionPatientGeneralInfo(Action):
    def name(self):
        return "patient_general_info"
            
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Patient's general info")
        f.append(tracker.get_slot(name))
        f.append(tracker.get_slot(age))
        f.append(tracker.get_slot(gender))
        f.append(tracker.get_slot(history))
        
        
                    
  
           
           
           
            
            
            