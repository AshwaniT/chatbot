## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## WF Happy Path
* greet
  - utter_greet
  - utter_what_Can_I_Do
* informed_wfentities{"wf_entity":"Areapath","wf_action":"create"}
  - action_ssa_helper
  - slot{"wf_entity":"Areapath","wf_action":"delete"}
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye


## WF Happy Path+Action
* greet
  - utter_greet
  - utter_what_Can_I_Do
* informed_wfentities{"wf_entity":"Areapath"}
  - utter_ask_action
 * workflowa_action{"wf_action":"create"} 
  - action_ssa_helper
  - slot{"wf_entity":"Areapath","wf_action":"delete"}
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## name of the story
* bake_roti
  - respond_bake_roti
