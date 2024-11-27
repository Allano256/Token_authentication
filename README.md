# Token_authentication

This is an API that has or tests three simple endpoints using Token Authentication, that is:

Signup:
-Here we provide test signup credentials of the user, i.e username, password and email.

Login:
-After successfull signup we retrive the token key provided as a result and use it in the Authorization to login the user,a new token is always created for a new user and this allows the application to log in the rightful user.

Test Token:
-This final endpoint ideally or ensures that the previous endpoints work with a successfull message displayed at the end or an error otherwise.
-Here we have the Authorizatio still and the Token key to verify.

API Retrieval and Usage

1. Clone the repository
   -git clone https://github.com/Allano256/Token_authentication

   -Navigate into the project directory:
   -cd restaurant_app

2. Setup the enviroment
   -Ensure you have the necessary dependencies and enviroment variables configured.

   -pip install -r requirements.txt

   -Create an .env file (or env.py) to store environment variables, including API keys or secret tokens. Example:

   -SECRET_KEY=your_secret_key
   -DEBUG=True

3. Run the application
   -python manage.py runserver

   API Retrieval and Usage
   -Follow these steps to retrieve and use the API provided in this repository:

4. Clone the Repository
   -Start by cloning this repository to your local machine:

   -git clone https://github.com/Allano256/Token_authentication
   -Navigate into the project directory:

   -cd restaurant_app 2. Set Up the Environment
   -Ensure you have the necessary dependencies and environment variables configured.

Install Python dependencies:

-pip install -r requirements.txt
-Create an .env file (or env.py) to store environment variables, including API keys or secret tokens. Example:

-SECRET_KEY=your_secret_key
-DEBUG=True 3. Run the Application

Start the application to access the API:

-python manage.py runserver
-By default, the API will be available at:
http://127.0.0.1:8000/

4. API Endpoints
   http://127.0.0.1:8000/login :Authenticate a user and retrieve a token.
   http://127.0.0.1:8000/signup : Register a new user.
   http://127.0.0.1:8000/test_token : Test both endpoints

5. Accessing/Testing the API
   -Add the "Rest Client" Extension in your IDE and this will connect to the API and used during the testing period.
