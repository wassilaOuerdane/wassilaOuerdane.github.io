from time import sleep
from random import uniform

class Environment:
    def act(self, message):
        print(message)

    def perceive(self):
        pass

from threading import Thread

class Agent(Thread):
    def __init__(self, name, env):
        Thread.__init__(self)
        self.name = name
        self.env = env

    def run(self):
        while True:
            self.procedural_loop()

    def procedural_loop(self):
        self.env.act("Agent " + self.name + " says hello!")
        sleep(uniform(0.1,0.5))

class Runtime:
    def __init__(self):
        e = Environment()
        a = Agent("Alice", e)
        b = Agent("Bob", e)
        a.start()
        b.start()

Runtime()

