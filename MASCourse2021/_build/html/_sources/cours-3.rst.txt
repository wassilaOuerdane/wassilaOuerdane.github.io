3. Interaction mechanisms : models and implementation
================================================================

Agenda -- Recall
-----------------

1. Friday, March the 5th, 2021 : Introduction to MAS : definitions and implementation of a platform
2. Friday, March the 12th, 2021 : Multiagent simulation : preys and predators
3. Friday, March the 19th, 2021 : Interaction mechanisms : models and implementation
4. Friday, March the 26th, 2021 : Practical session
5. Friday, April the 2nd, 2021 : Argumentation-based negotiation I: what is argumentation?
6. Friday, April the 9th, 2021 : Argumentation-based negotiation II: what is a negotiation protocol?
7. Friday, April the 16th, 2021 : Practical session


Session 3. 
~~~~~~~~~~~~~~~~~~~~~~~

Multiagent systems is not just about having different processes (or piece of code) that run in parallel, as we did in the previous sessions. Indeed, agents need to share some information to work together.

In the Alice and Bob examples (session 1, section 2) as well as in the Multi-Agent Based Simulation you implemented in the second session, agents worked separately and acted, in a concurrent manner, on a shared variable in the environment. This very primitive type of interactions is called *indirect interactions*. We will give a brief presentation of indirect interaction mechanisms in the first section of today's course session.

In the Money example (session 1, section 4), agents act directly on their peers variables. This is not supposed to happen in a MAS: agents can only interact with their environment. However, it is often required that agents request modifications to other agents. Such mechanisms are called *direct interactions* and will be presented in the second section of this course session.

The third section will give you an overview of software engineering practices and tools that you should adopt as MAS designers.

The fourth section will present a Mesa-based library for direct interactions that we shall use in the remaining of this course.

As for the previous sessions, all implementation is done using the Python programming language and the Mesa library.



References
~~~~~~~~~~

- Ferber, J. (1995), *Les Systèmes Multi-Agents*, InterEditions. **(French version)**
- Ferber, J. (1999), *Multi-agent systems: An introduction to distributed artificial intelligence*, Addison Wesley. **(English version)**
- Michael Wooldridge (2002), *An Introduction to MultiAgent Systems*, John Wiley & Sons Ltd.
- `The AgentLink roadmap <http://www.agentlink.org/roadmap/>`_


