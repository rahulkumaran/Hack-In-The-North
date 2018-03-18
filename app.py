
#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import json

app = Flask(__name__)
ACCESS_TOKEN = 'EAAELWqoKdy4BAKRnsbp8kZB6QivZBN46vVla9CTzEHwZCcsAAGQuyA9hLPacPXsUJGZAetuhVTO8nX6HMpEgxFfEuGimZAAGoaPvALO1GpgjrPA4VFoqToNF8HkB6c4GvGDmbS6CsKVSQY3oiz6xSZCCMsGVKX4oEcgoIsTWTSzQZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)
predefined_responses = ['Hey! Can I know your name?', 'And your age?', 'Gender?', 'How long have you been in depression?']

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])

def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                print(recipient_id)
                print(message)
                
                json_file = open('user.json', 'r')
                json_data = json.load(json_file)
                json_file.close()
                # Close after read
                # If the user sends the message for the first time add calue to the database.
                if recipient_id not in json_data:
                    print("Adding", recipient_id, "to json")
                    dump_data = {
                        "name" : "",
                        "age" : "",
                        "gender" : "",
                        "how_long" : "",
                        "count" : 0
                    }
                    json_data[recipient_id] = dump_data
                    # Write
                    json_file = open('user.json', 'w')
                    json.dump(json_data, json_file)
                    json_file.close()
                    send_message(recipient_id, predefined_responses[0])
                    # Close after write
                # if the instance of the user is already defined
                else :
                    print(recipient_id,"is already present")
                    print(message['message']['text'])
                    json_data[recipient_id]['count'] = json_data[recipient_id]['count'] + 1
                    # Increment the counter and write to the file.
                    json_file = open('user.json','w')
                    if(json_data[recipient_id]['count'] == 1): 
                        print("Name is", message['message']['text'])
                        json_data[recipient_id]['name'] = message['message']['text']
                        json.dump(json_data, json_file)
                        json_file.close()
                        send_message(recipient_id, predefined_responses[ json_data[recipient_id]['count'] ])
                    elif(json_data[recipient_id]['count'] == 2):
                        print("Age is", message['message']['text'])
                        json_data[recipient_id]['age'] =  message['message']['text']
                        json.dump(json_data, json_file)
                        json_file.close()
                        send_message(recipient_id, predefined_responses[ json_data[recipient_id]['count'] ])
                    elif(json_data[recipient_id]['count'] == 3):
                        print("Gender is", message['message']['text'])
                        json_data[recipient_id]['gender'] = message['message']['text']
                        json.dump(json_data, json_file)
                        json_file.close()
                        send_message(recipient_id, predefined_responses[ json_data[recipient_id]['count'] ])
                    elif(json_data[recipient_id]['count'] == 4):
                        print("Has been suffering since", message['message']['text'])
                        json_data[recipient_id]['how_long'] = message['message']['text']
                        json.dump(json_data, json_file)
                        json_file.close()
                        send_message(recipient_id, "It's great to know you")
                    else:
                        response_sent_text = get_message()
                        json_data[recipient_id]['how_long'] = message['message']['text']
                        json.dump(json_data, json_file)
                        json_file.close()
                        send_message(recipient_id, response_sent_text)
                        # file_object = open('user.json','r')
                        # json_data = json.load(file_object)
                        # file_object.close()
                        # print("The json data is",json_data)
                        # for key in json_data:
                        #     if json_data[key]['age'] == 'Gender?':
                        #         del(key)
                        # print("The  new json data is",json_data)
                        # file_object = open('user.json','w')
                        # json.dump(json_data, file_object)
                        # file_object.close()
                
                # if message['message'].get('text'):
                #     response_sent_text = get_message()
                #     send_message(recipient_id, response_sent_text)

        

        
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()