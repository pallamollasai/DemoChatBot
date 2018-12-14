## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format intent[entities] -->
  - utter_happy
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_goodbye
## get username
* inform
  - action_get_user
  - utter_did_that_help
  
## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action the bot should execute -->
* mood_unhappy
  - action_retrieve_image
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy
  
## get username
* inform
  - action_get_user
  - utter_did_that_help
* inform
  - action_get_user
  - utter_did_that_help
## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - action_retrieve_image
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye
## get username
* inform
  - action_get_user
  - utter_did_that_help  
## strange user
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_unclear

## say goodbye
* goodbye
  - utter_goodbye

## fallback
- utter_unclear
## Generated Story -645369142239310911
* unclear
    - utter_greet
* inform
    - action_get_user
    - slot{"usernamedb": "Bond"}
    - utter_did_that_help
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* unclear
* inform
    - action_get_user
    - slot{"usernamedb": "ROck"}
    - utter_did_that_help
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* greet
    - export

## Generated Story 4241416653921577281
* greet
    - utter_greet
* goodbye
    - utter_goodbye
* inform
    - utter_ask_username
* 
    - utter_goodbye
* unclear
* inform
    - action_get_user
    - slot{"usernamedb": "Bond"}
    - utter_did_that_help
* unclear
* mood_unhappy
    - utter_happy
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
    - export

## Generated Story -2207865759588442700
* inform
    - action_get_user
    - slot{"usernamedb": ""}
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* greet
    - utter_greet
* mood_unhappy
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* mood_unhappy
    - action_retrieve_image
    - slot{"img_api_response": "https://picsum.photos/200/300/?random"}
* 
    - export

## Generated Story 4043012730193592851
* inform
    - action_get_user
    - slot{"usernamedb": ""}
* inform
    - action_get_user
    - slot{"usernamedb": "Bond"}
    - utter_did_that_help
* greet
    - utter_greet
* inform
    - action_get_user
    - slot{"usernamedb": "ROck"}
    - utter_did_that_help
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* greet
    - export

## Generated Story -7432944521246188858
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* unclear
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* unclear
    - utter_unclear
* unclear
    - utter_unclear
* unclear
    - utter_unclear
* greet
    - utter_greet
* greet
    - utter_greet
* unclear
    - utter_unclear
* unclear
    - utter_unclear
* goodbye
    - utter_goodbye
    - utter_goodbye
    - utter_goodbye
    - utter_goodbye
* goodbye
    - utter_goodbye
* goodbye
    - utter_goodbye
* inform
* unclear
    - utter_unclear
* goodbye
    - utter_goodbye
    - utter_goodbye
    - utter_goodbye
    - utter_goodbye
* inform
    - action_get_user
    - slot{"usernamedb": ""}
    - utter_did_that_help
* unclear
    - utter_unclear
    - utter_unclear
* unclear
    - utter_unclear
    - utter_unclear
    - utter_unclear
    - utter_unclear
    - utter_unclear
    - utter_unclear
    - utter_unclear
* greet
    - export

