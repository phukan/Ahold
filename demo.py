from api.ai import Agent

import json





#initialize the agent 

agent = Agent(

     '14a0e917-6bfe-49bd-b335-eeee6e0f1295',

     '4529f6f5b60d4f7bb2ec7be2750f3565',

     '3861744a9f1c4805a2411b676823563b',

)



# actions defined in the API.AI console that fire locally when an intent is

# recognized

def ChooseType(type):

	print 'Available types : Tulip, Roses, bulb'

def saveType(flowerType):

	print 'Available color : blue,red,violet'



def saveColor(color):

	print 'Address format: city, lane, house number'



def createOrder(address):

	print 'Please continue if you need any other flower'



def main():

	user_input = ''



	#loop the queries to API.AI so we can have a conversation client-side

	while user_input != 'exit':



		#parse the user input

		user_input  = raw_input("me: ")

		#query the console with the user input, retrieve the response

		response = agent.query(user_input)

		#parse the response

		result = response['result']

		fulfillment = result['fulfillment']



		print 'bot: ' + fulfillment['speech']



		#if an action is deteted, fire the appropriate function

		if result['action'] == 'ChooseType':

			ChooseType(user_input)

		if result['action'] == 'saveFlowerType':

			saveType(user_input)

		if result['action'] == 'saveColor':

			saveColor(user_input)

		if result['action'] == 'createOrder':

			createOrder(user_input)





if __name__ == "__main__":

    main()
