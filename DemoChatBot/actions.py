from rasa_core.actions import Action
from rasa_core.events import SlotSet

import requests
import pymysql

class ApiAction(Action):
    def name(self):
        return "action_retrieve_image"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for a good img")
        url = "https://picsum.photos/200/300/?random"
        return [SlotSet("img_api_response", url)]

class UserInfo(Action):
	def name(self):
		return "action_get_user"
	def run(self,dispatcher,tracker,domain):
		user_name=input("enter user name")
		
		#user_name=tracker.get_slot('user_name')
		user_name_db=""
		db=pymysql.connect("localhost","root","root","Test")
		cursor=db.cursor()
		print("username taken")
		sql="select * from chatbotusers"
		try:
			cursor.execute(sql)
			results=cursor.fetchall()

			for row in results:
				if row[0]==user_name :
					user_name_db=row[0]
					break
			print("Username saved from db",user_name_db)
		except:
			print("unable to fetchdata")
			db.close()
		
		return [SlotSet("usernamedb",user_name_db)]