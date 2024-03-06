# Interview Case - Data Engineer
This repo contains the codebase for a case interview in the recruitment process for a Data Engineer position. Below follows some light documentation as well as questions to be answered during the interview.

The documentation and questions will be in English, but the interview will be held in Swedish. Answers to the questions and reasoning should be prepared in Swedish.

### Description
The codebase for the interview case is a template project written in Python with the flask library being the main library serving the application. Documentation for the flask library can be found at [https://flask.palletsprojects.com](https://flask.palletsprojects.com). Since flask is a quite "bare bones" library, the [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask) template project has been used as inspiration to creating this template.

### Running the project
Follow the below steps for running the application. UNIX commands is used for commands like `cd` and `source` and will have to be adjusted slightly if the host OS doesn't support UNIX commands.

Clone the repository
`git clone https://github.com/Rydberg95/interview-case/ && cd interview-case`

Create a Python virtual environment (optional, but highly recommended)
`python -m venv .venv && source .venv/bin/activate` 

Install required Python packages
`pip install -r requirements.txt`

Run the application
`flask -A 'flaskr:create_app' run`

You should now be able to see terminal output saying that the flask app is running, and at what address you can access the application in the web browser.

### Tasks and Questions

