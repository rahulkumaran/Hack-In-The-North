## depression path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_great
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  

## depression path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_great
  - utter_history_question
* mood_decline
  - actions.ActionPatientInfoRecurrence  

## depression path 3
* greet
  - utter_greet
* mood_great
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  

## depression path 4
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_great
  - utter_history_question
* mood_decline
  - actions.ActionPatientInfoRecurrence  

## depression path 5
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  
 

## depression path 6
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_decline
  - actions.ActionPatientInfoRecurrence  

## depression path 7
* greet
  - utter_greet
* mood_great
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_decline
  - actions.ActionPatientInfoRecurrence  

## say goodbye
* goodbye
  - utter_goodbye
 
