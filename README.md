# chatlib

chatlib allows beginners to make chatbots easily! If you're having trouble with coding, chatlib can help you! Even if you can code well, chatlib will allow you to make chatbots quicker!

Try a demo at https://chatlibpy.evangorman.repl.run.

## Instructions

To use chatlib.py, simply copy the chatlib.py file to your project folder. Then simply import the module "chatlib" in your script, like this:

```python
import chatlib
```

You can then create your bot.

## Tutorial

chatlib.py is fairly simple to use, once you've got the hang of it. Let's start with the basics.

We start by importing chatlib.py in our script, like this:

``` python
import chatlib
```

Now we can access the Bot class. Let's create our new bot, like this:

``` python
bot = chatlib.Bot("Bob")
```

This creates a bot named "Bob". Let's add some basic responses to Bob, for when he doesn't understand us:

``` python
bot.add_response("", "Sorry, I don't understand.")
bot.add_response("", "Uh...")
```

Let's add a mainloop to our bot, so we can talk to it:

``` python
bot.set_username(input("Username? ")) # Get username
print() # Print empty line
print(bot.name + ":", "Hi, I'm", bot.name + "!\n") # Print bot greeting


while True:
    r = input(bot.username + ": ") # Get user message
    print() # Print empty line
    print(bot.name + ":", bot.get_response(r)) # Print bot response
    print() # Print empty line
```

We can now try talking to our bot, like so:

```
User: Hi!

Bob: Uh...

User: Hello??

Bob: Sorry, I don't understand.
```

Hmm...this bot isn't very fun to talk to! It doesn't understand anything we say! Let's add a path to our bot so it can understand something. Let's add some code back above the mainloop.

``` python
bot.create_path("hello")
```

We now have a path called "hello". Let's add some keywords to this path for the bot to recognize.

``` python
bot.add_keyword("hello", "hello")
bot.add_keyword("hello", "hi")
```

Now the bot can recognize the words "hello" and "hi"! Let's add some things for the bot to say in response.

``` python
bot.add_response("hello", "Hi!")
bot.add_response("hello", "Hello!")
```

Let's try our bot now:

```
User: Hello!

Bob: Hi!
```

Already there's an improvement! But what if we want to check for an exact response from the user? Let's add a phrase to the path.

``` python
bot.add_phrase("hello", "(waves at robot)")
```

Now we can "wave" at the bot and it will respond accordingly! But when you use the word "waves" out of context, the robot will not say "hi", like would happen in a real conversation. Here's an example:

```
User: (waves at robot)

Bob: Hello!

User: I like it when flags wave.

Bob: Sorry, I don't understand.
```

What if you want your bot to ask a question? Let's make a new path, with a keyword and phrase (keywords can have spaces too, and allow for more varied user messages):

``` python
bot.create_path("howareyou")
bot.add_keyword("howareyou", "how are you")
bot.add_phrase("howareyou", "Are you doing well?")
```

Now we can add a question to our path.

``` python
bot.add_question("howareyou", "I'm good, how about you?")
```

Questions can have paths too. Let's add one to our question:

``` python
bot.add_question_path("howareyou", "I'm good, how about you?", "good")
```

Notice that we refer to questions as the question itself. Let's add some keywords/phrases/responses to this path:

``` python
bot.add_question_keyword("howareyou", "I'm good, how about you?", "good", "good")
bot.add_question_phrase("howareyou", "I'm good, how about you?", "good", "I'm doing amazing!")
bot.add_question_response("howareyou", "I'm good, how about you?", "good", "Good to hear that!")
bot.add_question_response("howareyou", "I'm good, how about you?", "good", "That's great!")
```

Let's add a question path for if you're not feeling that great:

``` python
bot.add_question_path("howareyou", "I'm good, how about you?", "bad")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "bad")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "terrible")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "awful")
bot.add_question_phrase("howareyou", "I'm good, how about you?", "bad", "Not that great...")
bot.add_question_response("howareyou", "I'm good, how about you?", "bad", "Sorry to hear that...")
bot.add_question_response("howareyou", "I'm good, how about you?", "bad", "I hope you feel better soon.")
```

Let's test our chatbot now.

```
User: Hi!

Bob: Hello!

User: How are you?

Bob: I'm good, how about you?

User: I'm doing amazing!

Bob: Glad to hear that!
```

Already our bot feels a lot more "real"! Feel free to add to this bot, or make your own! Here's the final code for our bot:

``` python
import chatlib
bot = chatlib.Bot("Bob")

bot.add_response("", "Sorry, I don't understand.")
bot.add_response("", "Uh...")

bot.create_path("hello")
bot.add_keyword("hello", "hello")
bot.add_keyword("hello", "hi")
bot.add_phrase("hello", "(waves at robot)")
bot.add_response("hello", "Hi!")
bot.add_response("hello", "Hello!")

bot.create_path("howareyou")
bot.add_keyword("howareyou", "how are you")
bot.add_phrase("howareyou", "Are you doing well?")
bot.add_question("howareyou", "I'm good, how about you?")

bot.add_question_path("howareyou", "I'm good, how about you?", "good")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "good", "good")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "good", "great")
bot.add_question_phrase("howareyou", "I'm good, how about you?", "good", "I'm doing amazing!")
bot.add_question_response("howareyou", "I'm good, how about you?", "good", "Good to hear that!")
bot.add_question_response("howareyou", "I'm good, how about you?", "good", "That's great!")

bot.add_question_path("howareyou", "I'm good, how about you?", "bad")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "bad")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "terrible")
bot.add_question_keyword("howareyou", "I'm good, how about you?", "bad", "awful")
bot.add_question_phrase("howareyou", "I'm good, how about you?", "bad", "Not that great...")
bot.add_question_response("howareyou", "I'm good, how about you?", "bad", "Sorry to hear that...")
bot.add_question_response("howareyou", "I'm good, how about you?", "bad", "I hope you feel better soon.")

bot.set_username(input("Username? "))
print()
print(bot.name + ":", "Hi, I'm", bot.name + "!\n")

while True:
    r = input(bot.username + ": ")
    print()
    print(bot.name + ":", bot.get_response(r))
    print()
```


## Docs

Listed here are all the functions, classes and values in chatlib.py, for your reference.

All paths, keywords, phrases, questions and paths, keywords and phrases inside questions should be listed in order of priority, from most important to least important.

The path for when no conditions for other paths are met is simply nothing, like

```python
Bot.add_response("", response)
```

### Classes

```python
Bot(name) # the main class for your bot
```

### Functions

```python
Bot.set_username(name) # set name of user

Bot.create_path(name) # create new dialogue option

Bot.add_keyword(path, keyword) # add keyword to path; keyword is checked for anywhere in response

Bot.add_phrase(path, phrase) # add phrase to path; checked if whole response is exactly phrase

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

Bot.name # bot's name

Bot.greeting # bot's greeting
```
