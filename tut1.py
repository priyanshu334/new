import random
import time

#greeting the user
print("Hello! I am your chatbot. What is your name?")
name = input()
print("Nice to meet you, " + name + "!")
time.sleep(1) #pausing for 1 second 

#list of possible responses 
responses = ["I'm doing great!", "Not too bad!", "Pretty good!"] 
  
#function to generate a response 
def generate_response(): 

    #returning a random response from the list 
    return random.choice(responses) 

  
#infinite loop which will end when user types 'bye'  
while True: 

    #taking input from user 
    userInput = input()

    if userInput == "bye": #ending the loop if user types 'bye' 

        print("It was nice talking to you, "+name+"!") 

        break

    else: #if user inputs other than 'bye' then generating a response using generate_response() function  

        print(generate_response())