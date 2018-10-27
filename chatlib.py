# chatlib.py
# by python-b5
#
# chatlib.py is a simple library for creating chatbots.
# It could be useful for teaching basic programming
# concepts, or just for quickly making a chatbot.
#
# Idea from elizascript by Terry Cavanagh.

# Imports
import random
from collections import defaultdict

# Bot class
class Bot:
    # Initialize bot
    def __init__(self, name):
        self.name = Value(name)
        self.username = Value("unnamed")
        self.punctuation = ['\n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '-', '=', '[', ']', '\\', ';', "'", ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' ']
        self._current_question = None
        self._keywords = defaultdict(list)
        self._responses = defaultdict(list)
        self._questions = defaultdict(dict)
        self._question_keywords = defaultdict(dict)
        self._question_phrases = defaultdict(dict)
        self._phrases = defaultdict(list)
        self._keywords["_main"] = []
        self._responses["_main"] = []
        self._questions["_main"] = defaultdict(dict)
        self._question_keywords["_main"] = defaultdict(dict)
        self._question_phrases["_main"] = defaultdict(dict)
        self._phrases["_main"] = []
        self._do_question = False

    # Find response (no question)
    def find_response(self, path):
        self._current_path = path
        self._choices = [self._responses[self._current_path], self._questions[self._current_path]]
        for i in self._choices:
            if len(i) < 1:
                self._choices.remove(i)
        self._selected_rp = random.choice(self._choices)
        self._response = []
        response = random.choice(self._selected_rp) if self._selected_rp == self._responses[self._current_path] else random.choice(list(self._questions[self._current_path]))
        if isinstance(response, tuple):
            for i in response:
                if isinstance(i, Value):
                    self._response.append(str(i.value))
                else:
                    self._response.append(str(i))
        else:
            self._response.append(str(response))
        self._response = "".join(self._response)
        return "r" if self._selected_rp == self._responses[self._current_path] else (self._current_path, self._response)
    
    # Find response (question)
    def find_question_response(self, path, question, question_path):
        self._current_path = path
        self._selected_rp = self._questions[self._current_path][question][question_path]
        self._response = []
        response = random.choice(self._selected_rp)
        if isinstance(response, tuple):
            for i in response:
                if isinstance(i, Value):
                    self._response.append(str(i.value))
                else:
                    self._response.append(str(i))
        else:
            self._response.append(str(response))
        self._response = "".join(self._response)

    # Set bot username
    def set_username(self, name):
        self.username.value = name

    # Create new path
    def create_path(self, name):
        self._keywords[name] = []
        self._phrases[name] = []
        self._responses[name] = []

    # Add phrase to path
    def add_phrase(self, path, phrase):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._phrases[self._path].append(phrase)

    # Add keyword to path
    def add_keyword(self, path, keyword):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._keywords[self._path].append(keyword)

    # Add response to path
    def add_response(self, path, response):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._responses[self._path].append(response)
    
    # Add question to path
    def add_question(self, path, question):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._questions[self._path][question] = {}
        self._question_keywords[self._path][question] = {}
        self._question_phrases[self._path][question] = {}
    
    # Add path to question
    def add_question_path(self, path, question, question_path):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._questions[self._path][question][question_path] = []
        self._question_keywords[self._path][question][question_path] = []
        self._question_phrases[self._path][question][question_path] = []
    
    # Add response to path in question
    def add_question_response(self, path, question, question_path, response):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._questions[self._path][question][question_path].append(response)
    
    # Add keyword to path in question
    def add_question_keyword(self, path, question, question_path, keyword):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._question_keywords[self._path][question][question_path].append(keyword)

    # Add phrase to path in question
    def add_question_phrase(self, path, question, question_path, phrase):
        if path == "":
            self._path = "_main"
        else:
            self._path = path
        self._question_phrases[self._path][question][question_path].append(phrase)

    # Get standard response (no question)
    def get_standard_response(self, keywords, phrases, find_response_function):
        for i in phrases:
            if self.end:
                break
            for j in phrases[i]:
                if self.end:
                    break
                phrase = []
                if isinstance(j, tuple):
                    for k in j:
                        if isinstance(k, Value):
                            phrase.append(str(k.value))
                        else:
                            phrase.append(str(k))
                else:
                    phrase.append(str(j))
                phrase = "".join(phrase)
                if phrase.lower() == self._message:
                    self._response_type = find_response_function(i)
                    self.end = True
                    break
        for i in keywords:
            if self.end:
                break
            for j in keywords[i]:
                if self.end:
                    break
                keyword = []
                if isinstance(j, tuple):
                    for k in j:
                        if isinstance(k, Value):
                            keyword.append(str(k.value))
                        else:
                            keyword.append(str(k))
                else:
                    keyword.append(str(j))
                keyword = "".join(keyword)
                bad = False
                index = 0
                count = 0
                while count < len(keyword):
                    try:
                        if self._message[index] == keyword[count]:
                            count += 1
                        else:
                            count = 0
                    except IndexError:
                        pass
                    index += 1
                try:
                    if self._message[index] not in self.punctuation:
                        bad = True
                except IndexError:
                    pass
                if bad:
                    continue
                if keyword in self._message:
                    self._response_type = find_response_function(i)
                    self.end = True
                    break
        if not self.end:
            self._response_type = "r"
            self._response = random.choice(self._responses["_main"])
    
    # Get question response
    def get_question_response(self, keywords, phrases, find_response_function):
        for i in phrases:
            if self.end:
                break
            for j in phrases[i]:
                if self.end:
                    break
                for k in phrases[i][j]:
                    if self.end:
                        break
                    for l in phrases[i][j][k]:
                        if self.end:
                            break
                        phrase = []
                        if isinstance(l, tuple):
                            for m in l:
                                if isinstance(m, Value):
                                    phrase.append(str(m.value))
                                else:
                                    phrase.append(str(m))
                        else:
                            phrase.append(str(l))
                        phrase = "".join(phrase)
                        if phrase.lower() == self._message:
                            find_response_function(i, j, k)
                            self.end = True
                            break
        for i in keywords:
            if self.end:
                break
            for j in keywords[i]:
                if self.end:
                    break
                for k in keywords[i][j]:
                    if self.end:
                        break
                    for l in keywords[i][j][k]:
                        if self.end:
                            break
                        keyword = []
                        if isinstance(l, tuple):
                            for m in l:
                                if isinstance(m, Value):
                                    keyword.append(str(m.value))
                                else:
                                   keyword.append(str(m))
                        else:
                            keyword.append(str(l))
                        keyword = "".join(keyword)
                        bad = False
                        index = 0
                        count = 0
                        while count < len(keyword):
                            try:
                                if self._message[index] == keyword[count]:
                                    count += 1
                                else:
                                    count = 0
                            except IndexError:
                                pass
                            index += 1
                        try:
                            if self._message[index] not in self.punctuation:
                                bad = True
                        except IndexError:
                            pass
                        if bad:
                            continue
                        if keyword in self._message:
                            find_response_function(i, j, k)
                            self.end = True
                            break
        if not self.end:
            self._response_type = "r"
            self._response = random.choice(self._responses["_main"])

    # Get response
    def get_response(self, message):
        self.end = False
        self._message = message.lower()
        if not self._do_question:
            self.get_standard_response(self._keywords, self._phrases, self.find_response)
            if isinstance(self._response_type, tuple):
                self._current_question == self._response_type
                self._do_question = True
        else:
            self.get_question_response(self._question_keywords, self._question_phrases, self.find_question_response)
            self._do_question = False
        return self._response

# Alterable value class
class Value:
    def __init__(self, initial_value):
        self.value = initial_value
