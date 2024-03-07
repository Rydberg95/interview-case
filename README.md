# Interview Case - Data Engineer
This repo contains the codebase for a case interview in the recruitment process for a Data Engineer position. Below follows some light documentation as well as questions to be answered during the interview.

The documentation and questions will be in English, but the interview will be held in Swedish. Answers to the questions and reasoning should be prepared in Swedish.

### Description
The codebase for the interview case is a template project written in Python with the flask library being the main library serving the application. Documentation for the flask library can be found at [https://flask.palletsprojects.com](https://flask.palletsprojects.com). Since flask is a quite "bare bones" library, the [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask) template project has been used as inspiration to creating this template.

The datamodel provided in this sample project only contains a single "Insurance Claim" object. This objects reflects an insurance claim (sv. "skadeanmälan") reported by a customer. The 

### Running the project
Follow the below steps for running the application. UNIX commands is used for commands like `cd` and `source` and will have to be adjusted slightly if the host OS doesn't support UNIX commands.

**Python 3.x is assumed to be installed prior to following below steps.** Python 3.12 was used when making the project, but any relatively recent Python version should work without issues.

Clone the repository  
`git clone https://github.com/Rydberg95/interview-case/ && cd interview-case`

Create a Python virtual environment (optional, but highly recommended)  
`python -m venv .venv && source .venv/bin/activate` 

Install required Python packages  
`pip install -r requirements.txt`

Run the application  
`flask -A 'flaskr:create_app' run`

You should now be able to see terminal output saying that the flask app is running, and at what address you can access the application in the web browser.

You can now visit the endpoint `/generate_random_claim` to generate a random insurance claim, that should show then be displayed in your browser.

### Tasks and Questions

Although you could answer some of the below questions by presenting your reasoning behind a solution, it is preferred to have working code (or at least an attempt) presented that solves the requested feature/issue.

* **Add a new object to the application that reflects insurance policies**  
*The insurance policy is the actual product that the customer buys, which gives a customer the right to later report an insurance claim.* 
The insurance policy object should (at least) have (1) a unique identifier and (2) a premium (price of the insurance.) Create a page similar to the one displaying claims, but for insurance policies. All though not mandatory, feel free to add styling of the page as you'd like.

* **Export the available claims data to a data file**  
Create a new web endpoint that, when visited, creates a data file containing the claims data that is available.
*Since the [pandas](https://pandas.pydata.org/) library is used for calculations carried out by ClaimBook (the application you would develop), solutions where this might be used are preferred.*