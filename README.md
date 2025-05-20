Username Generator Microservice
This microservice generates unique music-themed usernames based on user information provided by the main application.
Communication Contract
How to REQUEST data from the microservice
The microservice accepts HTTP POST requests to the /generate endpoint. The request should contain a JSON body with user information.
Endpoint:
POST http://localhost:5000/generate


Headers:
Content-Type: application/json


Request Body Parameters:
first_name (optional): User's first name
last_name (optional): User's last name
favorite_genre (optional): User's favorite music genre
Example Request:
import requests
import json


data = {
   "first_name": "John",
   "last_name": "Smith",
   "favorite_genre": "rock"
}


response = requests.post(
   "http://localhost:5000/generate",
   headers={"Content-Type": "application/json"},
   data=json.dumps(data)
)


# Process the response
usernames = response.json()["usernames"]


How to RECEIVE data from the microservice
The microservice returns a JSON response with generated username options.
Response Format:
{
 "success": true,
 "usernames": [
   "jsmith123",
   "melodicjohn5",
   "rockmaestroab2"
 ]
}


Example Processing Response:
if response.status_code == 200:
   response_data = response.json()
   if response_data["success"]:
       # Get the list of generated usernames
       usernames = response_data["usernames"]
       # Use the first username or present choices to the user
       selected_username = usernames[0]
else:
   print(f"Error: {response.status_code}")
   print(response.text)


UML Sequence Diagram
Below is a UML sequence diagram showing how the main program interacts with the username generator microservice:



Health Check Endpoint
The microservice also provides a health check endpoint:
GET http://localhost:5000/health


Response:
{
 "status": "healthy",
 "service": "username-generator"
}


This can be used to verify that the microservice is up and running.



