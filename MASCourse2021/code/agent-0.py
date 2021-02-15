from time import sleep

class Environment:
    def act(self,message):
        print(message)
    def perceive(self):
        pass

class Agent:
    def __init__(self,name,env):
        self.name = name
        self.env = env
    def procedural_loop(self):
        while True:
            self.env.act("Agent "+self.name+" says hello!")
            sleep(0.1)

class Runtime:
    def __init__(self):
        e = Environment()
        (Agent("Alice",e)).procedural_loop()
        (Agent("Bob",e)).procedural_loop()

Runtime()
