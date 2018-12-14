from rasa_core.agent import Agent
agent = Agent.load('models/dialogue', interpreter='./models/nlu/default/current')

print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        print(response["text"])

