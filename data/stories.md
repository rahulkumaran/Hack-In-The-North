## depression path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_happy
  - utter_history_question

## depression path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_unhappy
  - utter_history_question


## say goodbye
* goodbye
  - utter_goodbye