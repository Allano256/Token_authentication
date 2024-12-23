# Token_authentication

This is an API that has or tests three simple endpoints using Token Authentication, that is:

<ul>Signup: </ul>
<li>Here we provide test signup credentials of the user, i.e username, password and email.</li>

<ul> Login:</ul>
<li>After successfull signup we retrive the token key provided as a result and use it in the Authorization to login the user,a new token is always created for a new user and this allows the application to log in the rightful user.</li>

<ul>Test Token: </ul>
<li>This final endpoint ideally or ensures that the previous endpoints work with a successfull message displayed at the end or an error otherwise.
Here we have the Authorization still and the Token key to verify.</li>

<ul>API Retrieval and Usage </ul>

<ul> Clone the repository</ul>
<li>git clone https://github.com/Allano256/Token_authentication</li>
<li>Navigate into the project directory:</li>
<li>cd restaurant_app</li>

<ul>Setup the enviroment </ul>
<li>Ensure you have the necessary dependencies and enviroment variables configured.</li>
<li>pip install -r requirements.txt</li>
<li>Create an .env file (or env.py) to store environment variables, including API keys or secret tokens. Example:</li>
<li>SECRET_KEY=your_secret_key</li>
<li>DEBUG=True</li>

<ul> Run the application </ul>
<li>python manage.py runserver</li>

<ul>Start the application to access the API:  </ul>
<li>python manage.py runserver</li>
<li>By default, the API will be available at:</li>
<li>http://127.0.0.1:8000/</li>

<ul>API Endpoints:  </ul>
<li>http://127.0.0.1:8000/login :Authenticate a user and retrieve a token.</li>
<li>http://127.0.0.1:8000/signup : Register a new user.</li>
<li>http://127.0.0.1:8000/test_token : Test both endpoints</li>

<ul>Accessing/Testing the API  </ul>
<li>-Add the "Rest Client" Extension in your IDE and this will connect to the API and used during the testing period.</li>
