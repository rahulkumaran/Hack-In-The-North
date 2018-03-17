from rasa_core.actions import Action
from rasa_core.events import SlotSet

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
    
class ActionPatientInfo(Action):
       def name(self):
           return "patient_consultation_info"
        
       def run(self, dispatcher, tracker, domain):
           
            
            
            