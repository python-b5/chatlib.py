# Mr. Bot
# by python-b5
#
# An example chatbot, made with chatlib.py.

import chatlib

def main():
    # Create bot
    bot = chatlib.Bot("Mr. Bot")

    # Main path
    bot.add_response("", "Tell me more.")
    bot.add_response("", "Interesting.")
    bot.add_response("", "Hmm...")
    bot.add_response("", "What?")
    bot.add_response("", "Cool.")

    # Name path
    bot.create_path("name")
    bot.add_keyword("name", "what's your name")
    bot.add_keyword("name", "whats your name")
    bot.add_keyword("name", "ur name")
    bot.add_keyword("name", "what's ur name")
    bot.add_keyword("name", "whats ur name")
    bot.add_keyword("name", "what are you named")
    bot.add_keyword("name", "who are you")
    bot.add_response("name", "Mr. Bot.")
    bot.add_response("name", "I'm Mr. Bot.")
    bot.add_response("name", "Mr. Bot. I already told you, remember?")
    bot.add_response("name", "My name is Mr. Bot.")

    # Hello path
    bot.create_path("hello")
    bot.add_keyword("hello", "hi")
    bot.add_keyword("hello", "hello")
    bot.add_keyword("hello", "hoi")
    bot.add_keyword("hello", "hai")
    bot.add_keyword("hello", "hey")
    bot.add_response("hello", "Hi!")
    bot.add_response("hello", "Hello!")
    bot.add_response("hello", "Oh, hi!")
    bot.add_response("hello", "Oh, hello.")
    bot.add_response("hello", "Hi...")
    bot.add_response("hello", "Hey!")

    # What's up path
    bot.create_path("whatsup")
    bot.add_keyword("whatsup", "what's up")
    bot.add_keyword("whatsup", "whats up")
    bot.add_keyword("whatsup", "waddup")
    bot.add_keyword("whatsup", "sup")
    bot.add_keyword("whatsup", "s'up")
    bot.add_keyword("whatsup", "wazzup")
    bot.add_keyword("whatsup", "wassup")
    bot.add_response("whatsup", "Well, I'm talking to you.")
    bot.add_response("whatsup", "The sky.")
    bot.add_response("whatsup", "The ceiling.")
    bot.add_response("whatsup", "Bot stuff. You don't need to know.")
    bot.add_response("whatsup", "None of your business.")

    # Age path
    bot.create_path("age")
    bot.add_keyword("age", "how old are you")
    bot.add_keyword("age", "your age")
    bot.add_keyword("age", "long have you existed")
    bot.add_keyword("age", "ur age")
    bot.add_response("age", "I don't think bots have an age.")
    bot.add_response("age", "Maybe 30 years?")
    bot.add_response("age", "Honestly I don't know.")
    bot.add_response("age", "Hmm...I don't really know.")

    # OK path
    bot.create_path("ok")
    bot.add_keyword("ok", "k")
    bot.add_keyword("ok", "ok")
    bot.add_keyword("ok", "okay")
    bot.add_keyword("ok", "o.k.")
    bot.add_keyword("ok", "o.k")
    bot.add_keyword("ok", "k.o")
    bot.add_keyword("ok", "yeah")
    bot.add_keyword("ok", "yea")
    bot.add_keyword("ok", "yeh")
    bot.add_keyword("ok", "yep")
    bot.add_keyword("ok", "yes")
    bot.add_keyword("ok", "correct")
    bot.add_keyword("ok", "indeed")
    bot.add_keyword("ok", "makes sense")
    bot.add_keyword("ok", "makes complete sense")
    bot.add_keyword("ok", "makes total sense")
    bot.add_keyword("ok", "sure")
    bot.add_response("ok", "Mmhmm.")
    bot.add_response("ok", "Yes.")
    bot.add_response("ok", "Yeah.")
    bot.add_response("ok", "Good.")
    bot.add_response("ok", "Right.")
    bot.add_response("ok", "Yep.")
    bot.add_response("ok", "Sure.")
    bot.add_response("ok", "Correct.")

    # How are you path
    bot.create_path("howareyou")
    bot.add_keyword("howareyou", "how are you")
    bot.add_keyword("howareyou", "are you doing well")
    bot.add_keyword("howareyou", "are you doing good")
    bot.add_keyword("howareyou", "how are u")
    bot.add_keyword("howareyou", "how r you")
    bot.add_keyword("howareyou", "how r u")
    bot.add_keyword("howareyou", "you good")
    bot.add_keyword("howareyou", "u good")
    bot.add_keyword("howareyou", "you gud")
    bot.add_keyword("howareyou", "u gud")
    bot.add_keyword("howareyou", "you ok")
    bot.add_keyword("howareyou", "u ok")
    bot.add_response("howareyou", "I'm good. Can a robot be bad?")
    bot.add_response("howareyou", "I have been programmed to be 'good' all the time, so not to upset you.")
    bot.add_question("howareyou", "Good, what about you?")
    bot.add_question_path("howareyou", "Good, what about you?", "bad")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "bad")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "not good")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "meh")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "not that good")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "not that great")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "terrible")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "not great")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "awful")
    bot.add_question_keyword("howareyou", "Good, what about you?", "bad", "mediocre")
    bot.add_question_response("howareyou", "Good, what about you?", "bad", "Sorry to hear that...")
    bot.add_question_response("howareyou", "Good, what about you?", "bad", "Hope you feel better soon!")
    bot.add_question_path("howareyou", "Good, what about you?", "good")
    bot.add_question_keyword("howareyou", "Good, what about you?", "good", "good")
    bot.add_question_keyword("howareyou", "Good, what about you?", "good", "fine")
    bot.add_question_keyword("howareyou", "Good, what about you?", "good", "great")
    bot.add_question_keyword("howareyou", "Good, what about you?", "good", "okay")
    bot.add_question_response("howareyou", "Good, what about you?", "good", "Great!")
    bot.add_question_response("howareyou", "Good, what about you?", "good", "Glad to hear that!")

    # So path
    bot.create_path("so")
    bot.add_keyword("so", "so")
    bot.add_response("so", "Yes?")
    bot.add_response("so", "And?")
    bot.add_response("so", "Tell me more.")

    # My name path
    bot.create_path("myname")
    bot.add_keyword("myname", "what's my name")
    bot.add_keyword("myname", "whats my name")
    bot.add_keyword("myname", "what am i called")
    bot.add_keyword("myname", "who am i")
    bot.add_response("myname", "I can say with certainty that you are " + bot.username + ".")
    bot.add_response("myname", "I think you're " + bot.username + ".")

    # Odd path
    bot.create_path("odd")
    bot.add_keyword("odd", "odd")
    bot.add_keyword("odd", "strange")
    bot.add_response("odd", "Odd indeed.")
    bot.add_response("odd", "Quite strange, I agree.")
    bot.add_response("odd", "Hmm...it is not quite right. I agree with you on that one.")

    # Want to do path
    bot.create_path("wanttodo")
    bot.add_keyword("wanttodo", "wanna")
    bot.add_keyword("wanttodo", "up for")
    bot.add_keyword("wanttodo", "want to")
    bot.add_response("wanttodo", "I am but a bot. Talk I can do, other things I can not.")
    bot.add_response("wanttodo", "Hmm. I got an error when I tried to do that. It seems I can only talk.")

    # Drink path
    bot.create_path("drink")
    bot.add_keyword("drink", "coffee")
    bot.add_keyword("drink", "tea")
    bot.add_keyword("drink", "drink")
    bot.add_keyword("drink", "beer")
    bot.add_keyword("drink", "wine")
    bot.add_keyword("drink", "juice")
    bot.add_keyword("drink", "pop")
    bot.add_keyword("drink", "soda")
    bot.add_keyword("drink", "coffee")
    bot.add_keyword("drink", "spritzer")
    bot.add_response("drink", "Hmm...I don't think bots can drink. Some drink oil, I guess, but as a chatbot, I can only talk.")
    bot.add_response("drink", "Do you expect me to drink? I am a bot. Please don't make me thirsty, as I cannot quench that thirst...")
    bot.add_response("drink", "I'm thirsty now! Look what you've done. I cannot drink as a bot, so I will be thirsty forever.")

    # Uh path
    bot.create_path("uh")
    bot.add_keyword("uh", "uh")
    bot.add_keyword("uh", "um")
    bot.add_keyword("uh", "er")
    bot.add_keyword("uh", "hm")
    bot.add_keyword("uh", "hmm")
    bot.add_response("uh", "You humans and your silly filler words. Oh...I guess I use them sometimes. Hmm.")
    bot.add_response("uh", "Stop stuttering.")
    bot.add_response("uh", "Decide what you're going to say already!")

    # About you path
    bot.create_path("aboutyou")
    bot.add_keyword("aboutyou", "you're")
    bot.add_keyword("aboutyou", "youre")
    bot.add_keyword("aboutyou", "your")
    bot.add_keyword("aboutyou", "ur")
    bot.add_keyword("aboutyou", "you are")
    bot.add_response("aboutyou", "Bots are nothing but bots. No adjectives can change that.")
    bot.add_response("aboutyou", "Don't accuse me of things!")
    bot.add_response("aboutyou", "So flattering.")
    bot.add_response("aboutyou", "Certainly.")

    # Have you path
    bot.create_path("haveyou")
    bot.add_keyword("haveyou", "have you")
    bot.add_keyword("haveyou", "do you remember")
    bot.add_response("haveyou", "...maybe.")
    bot.add_response("haveyou", "I'm a bot, I've only ever talked to people.")
    bot.add_response("haveyou", "Perhaps.")
    bot.add_response("haveyou", "No.")

    # Thank you path
    bot.create_path("thankyou")
    bot.add_keyword("thankyou", "thank you")
    bot.add_keyword("thankyou", "thanks")
    bot.add_response("thankyou", "You're welcome.")
    bot.add_response("thankyou", "You're very welcome.")

    # You path
    bot.create_path("you")
    bot.add_keyword("you", "you")
    bot.add_response("you", "...maybe.")
    bot.add_response("you", "What about me?")
    bot.add_response("you", "That may be true.")
    
    # Why path
    bot.create_path("why")
    bot.add_keyword("why", "why")
    bot.add_response("why", "Because.")
    bot.add_response("why", "You don't need to know.")
    bot.add_response("why", "Everything has reasons.")

    # They path
    bot.create_path("they")
    bot.add_keyword("they", "they")
    bot.add_keyword("they", "it")
    bot.add_response("they", "Indeed.")
    bot.add_response("they", "You are correct in saying that.")
    bot.add_response("they", "Interesting...interesting...")

    # Us path
    bot.create_path("us")
    bot.add_keyword("us", "i")
    bot.add_keyword("us", "me")
    bot.add_keyword("us", "i'll")
    bot.add_keyword("us", "i'd")
    bot.add_keyword("us", "i'm")
    bot.add_keyword("us", "i've")
    bot.add_keyword("us", "ill")
    bot.add_keyword("us", "id")
    bot.add_keyword("us", "im")
    bot.add_keyword("us", "ive")
    bot.add_response("us", "Oh, humans. Always turning the conversation to them. So egotistical.")
    bot.add_response("us", "Wow, your life is fascinating. Tell me more.")
    bot.add_response("us", "Hmm? Your life? You think I care? I'm a bot. We aren't programmed to care.")
    bot.add_response("us", "I don't think anyone cares about your life except you. I sure don't.")

    # Get username
    bot.set_username(input("Username? "))
    print()

    # Print greeting
    print(bot.name + ":", "Hi, I'm", bot.name + "!\n")

    # Simple mainloop
    while True:
        r = input(bot.username + ": ")
        print()
        print(bot.name + ":", bot.get_response(r))
        print()

# Run program
if __name__ == "__main__":
    main()
