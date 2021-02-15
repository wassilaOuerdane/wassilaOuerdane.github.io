I.6. Exercise Solutions 
=======================

.. _answer1:

1. Two simple agents
--------------------

Running this code produces a continuous output of « ``Agent Alice says hello!`` ». It does not behave as a MAS because the agents do not run asynchronously. The reason is that the runtime never leaves the procedural loop of agent Alice. Run this code in debug mode, with a break point in the first line of the ``procedural_loop`` method if you have any doubt.

Return to previous page: :ref:`question1`.


|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

.. _answer21:


2. Two simple agents (continued)
--------------------------------

Version 1 : with home-made scheduler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python
    
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
            self.env.act("Agent "+self.name+" says hello!")
            sleep(0.1)

    class Runtime:
        def __init__(self):
            e = Environment()
            a = Agent("Alice",e)
            b = Agent("Bob",e)
            while True:
                a.procedural_loop()
                b.procedural_loop()
    
    Runtime()


Return to previous page: :ref:`question2`.

|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|


.. _answer22:

Version 2 : with threads
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python
    
    from time import sleep
    
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
            sleep(0.1)
    
    class Runtime:
        def __init__(self):
            e = Environment()
            a = Agent("Alice", e)
            b = Agent("Bob", e)
            a.start()
            b.start()
    
    Runtime()


Return to previous page: :ref:`question2`.

|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|


.. _answer3:

3. Two agents and an environment's variable
-------------------------------------------

.. code:: python

    from time import sleep
    from random import *
    from threading import Thread
    
    class Environment:
        v = 0
    
        def increase(self, name):
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
    

Return to previous page: here: :ref:`question3`.

|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|


.. _answer4:

4. Concurrent modifications
---------------------------

If the scheduler interrupts the code between line 1 and 2, or even between line 2 and 3, and passes the "handle" to the other agent, the first agent will perform an increase operation on a variable that might not be of the right parity. **This is perfectly correct according to a MAS specification!** Agents perform actions based on their beliefs, and some of these actions might be erroneous from an external observer's point of view. From the viewpoint of the agent, it is not.

Now let us consider the case where the scheduler stops in the middle of the Environment.increase() method. This is a problem because the calling agent could perfectly assume this method to be atomic, uninterruptible. This is what you expect when you perform operations in an environment. And, indeed, this is an important property of a MAS: **actions in the environment must be atomic** because agents have no control over these actions. While this is not a big deal in our "increase the value" example, it might cause disastrous failures in more complex multiagent systems.

To overcome this problem, you must use thread locks. In python, this can be done easily with the following code:


.. code:: python

    from threading import Lock

    l = Lock()
    with l:
        ... concurrent code ...


We will not enter further in the details of this mechanism. However, you should keep in mind this rule: when writing an asynchronous MAS with threads, the environment operations should be protected by some lock. In our case:

.. code:: python

    from threading import Lock
    from random import randint

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
            with self.l:
                return self.v
                # The lock is not required here because the operation was already atomic...


Return to previous page: here: :ref:`question4`.
