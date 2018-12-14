from flask import Flask, request, render_template
from rasa_core.agent import Agent



app=Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/chat/")
def chat():
	message=request.args.get('msg')
	
	if not message:
		return "enter some message"
		
	
	res=""
	responses = agent.handle_message(message)
	for response in responses:
		print(response["text"])
		res=res+response["text"]
	print("final output is %s "% res),
	return res;

if __name__=="__main__":
	agent = Agent.load('./models/dialogue', interpreter='./models/nlu/default/current')
	app.run()