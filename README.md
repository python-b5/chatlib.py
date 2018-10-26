# chatlib

chatlib allows beginners to make chatbots easily! If you're having trouble with coding, chatlib can help you! Even if you can code well, chatlib will allow you to make chatbots quicker!

## Instructions

To use chatlib.py, simply copy the chatlib.py file to your project folder. Then simply import the module "chatlib" in your script, like this:

```python
import chatlib
```

You can then create your bot.

## Docs

### Classes

```python
Bot(name) # the main class for your bot
```

### Functions

```python
Bot.set_username(name) # set name of user

Bot.create_path(name) # create new dialogue option

Bot.add_keyword(path, keyword) # add keyword to path; keyword is checked for anywhere in response

Bot.add_phrase(path, phrase) # add phrase to path; checked if response is phrase

Bot.add_response(path, response) # add response to path; randomly chosen for bot to say

Bot.add_question(path, question) # add question to path; sometimes chosen instead of response

Bot.add_question_path(path, question, name) # add path to question

Bot.add_question_keyword(path, question, question_path, keyword) # add keyword to path in question

Bot.add_question_phrase(path, question, question_path, phrase) # add phrase to path in question

Bot.add_question_keyword(path, question, question_path, response) # add response to path in question

Bot.get_response(message) # gets response from bot
```

### Values

```python
Bot.username # user's name

Bot.name - bot's name

Bot.greeting - bot's greeting
```
