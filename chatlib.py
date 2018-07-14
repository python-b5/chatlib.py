# chatlib.py
# python-b5

import random
import time
from collections import defaultdict

class Bot:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
        self.prompt = "You:"
        self.username = "You"
        self.keywords = defaultdict(list)
        self.responses = defaultdict(list)
        self.phrases = defaultdict(list)
        self.keywords["_main"] = []
        self.responses["_main"] = []
        self.phrases["_main"] = []

    def display(self):
        print(self.name + ":", self.message)

    def get_response(self):
        return str(input(self.prompt))

    def get_name(self):
        self.username = str(input("Name?"))
        self.prompt = self.username + ":"
        print("")

    def create_path(self, name):
        self.keywords[name] = []
        self.responses[name] = []

    def add_phrase(self, path, phrase):
        if path == "":
            self.rpath = "_main"
        else:
            self.rpath = path
        self.phrases[self.rpath].append(phrase)

    def add_keyword(self, path, keyword):
        if path == "":
            self.rpath = "_main"
        else:
            self.rpath = path
        self.keywords[self.rpath].append(keyword)

    def add_response(self, path, response):
        if path == "":
            self.rpath = "_main"
        else:
            self.rpath = path
        self.responses[self.rpath].append(response)

    def start(self):
        self.current_path = "_main"
        self.message = self.greeting
        self.display()
        done = False
        
        while True:
            if not done:
                self.current_path = "_main"
            self.selected_rp = self.responses[self.current_path]
            self.message = random.choice(self.selected_rp)
            self.response = self.get_response().lower()
            done = False
            for i in self.phrases:
                for j in self.phrases[i]:
                    if j == self.response:
                        if not done:
                            self.current_path = i
                            done = True
                            self.selected_rp = self.responses[self.current_path]
                            self.message = random.choice(self.selected_rp)
                            time.sleep(random.randint(1, 3))
                            self.display()
                            self.current_path = "_main"
            for i in self.keywords:
                for j in self.keywords[i]:
                    bad = False
                    for k in self.response.split():
                        if j in k and len(k) > len(j):
                            bad = True
                    if bad:
                        continue
                    if j in self.response:
                        if not done:
                            self.current_path = i
                            done = True
                            self.selected_rp = self.responses[self.current_path]
                            self.message = random.choice(self.selected_rp)
                            time.sleep(random.randint(1, 3))
                            self.display()
                            self.current_path = "_main"
            if not done:
                time.sleep(random.randint(1, 3))
                self.display()
