from time import sleep


class Environment:
    def act(self, message):
        print(message)

    def perceive(self):
        pass

class Agent:
    def __init__(self, name, env):
        self.name = name
        self.env = env

    def procedural_loop(self):
        self.env.act("Agent " + self.name + " says hello!")
        sleep(0.1)

'''
# version 0
class Runtime:
    def __init__(self):
        e = Environment()
        a = Agent("Alice", e)
        b = Agent("Bob", e)
        while True:
            a.procedural_loop()
            b.procedural_loop()

'''
# version 1
from random import shuffle

class Runtime:
    def __init__(self):
        e = Environment()
        agents = [Agent("Alice", e), Agent("Bob", e)]
        while True:
            shuffle(agents)
            for a in agents:
                a.procedural_loop()


Runtime()

