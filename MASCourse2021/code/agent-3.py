from time import sleep
from random import uniform,randint
from threading import Thread,Lock

class Environment:
    v = 0
    l = Lock()
    def increase(self, name):
        with self.l:
            x = randint(1,4)
            print("Agent " + name + " increase the value by "+ str(x))
            self.v = self.v+x
            print("  --> " + str(self.v))

    def perceive(self):
        return self.v

class Agent(Thread):
    def __init__(self, name, env):
        Thread.__init__(self)
        self.name = name
        self.env = env

    def run(self):
        while True:
            self.procedural_loop()

    def procedural_loop(self):
        self.b = self.env.perceive()
        self.act()
        sleep(uniform(0.1,0.5))

class AgentOdd(Agent):
    def act(self):
        if self.b%2!=0:
            self.env.increase(self.name)

class AgentEven(Agent):
    def act(self):
        if self.b % 2 == 0:
            self.env.increase(self.name)

class Runtime:
    def __init__(self):
        e = Environment()
        a = AgentOdd("Alice", e)
        b = AgentEven("Bob", e)
        a.start()
        b.start()

Runtime()


# with somelock: ...

