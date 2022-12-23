# stepik_selenium_run_browser_language
This is a tutorial project from stepic course https://stepik.org/course/575/syllabus:
"Test automation with Selenium and Python".

The project purpose is to send a language information for a browser 
in accept-language header in order a server can determine which page language
must be returned.

The lesson is: https://stepik.org/lesson/237240/step/10?unit=209628
## Pycharm project configuration
After cloning the project from git perform steps:
- add 3.11 Python interperter with virtual environment.
Open terminal and install libraries:
	
- pip install selenium
- pip install pytest

## Tests execution in console 
For all tests a Chrome browser is used. 
Run commands in console by using a language parameter
### Spanish
pytest --language=es test_items.py
### French
pytest --language=fr test_items.py
### English
pytest --language=en test_items.py
### Russian
pytest --language=ru test_items.py
### Without any parameters a default English language is used
pytest test_items.py