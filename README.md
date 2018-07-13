# chatlib

chatlib allows beginners to make chatbots easily! If you're having trouble with coding, chatlib can help you! Even if you can code well, chatlib will allow you to make chatbots quicker!

# Commands

Bot(name, greeting) - the main class for your bot

Bot.get_name() - set name of user

Bot.create_path(name) - create new dialogue option

Bot.add_keyword(path, keyword) - add keyword to path; keyword is checked for anywhere in response

Bot.add_phrase(path, phrase) - add phrase to path; checked if response is phrase

Bot.add_response(path, response) - add response to path; randomly chosen for bot to say

Bot.start() - starts bot

Bot.username - user's name

Bot.name - bot's name

Bot.greeting - bot's greeting; the message displayed at start