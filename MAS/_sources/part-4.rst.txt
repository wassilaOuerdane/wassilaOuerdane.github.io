2.1. Introduction
================================================================================


TO BE DONE

1. Simulation
--------------------------------------------------------------------------------

**Simulation definition**

Simulation is one of the most effective decision support tools available to scientists, designers and managers of complex systems. It consists in building a model of a real system and conducting experiments on this model in order to understand the behavior of this system and improve its performance. Here is one of the definitions of a simulation: 

  "The process of designing a model of a real system and conducting experiments with this model for the purpose either of understanding the behaviour of the system or of evaluating various strategies (within the limits imposed by a criterion or a set of criteria) for the operation of the system." Shannon, 1998.

The issue behind a digital simulation is therefore to study a real system in order to understand its internal functioning and / or to predict its evolution under certain conditions. Moreover, to achieve these objectives, this study is necessarily done through a **model** of the **real system** which is used to carry out the experiments. The terms **real system** and **model** are the two keywords in this definition. 

It is important to understand that the real system does not necessarily refer to a phenomenon that exists in nature. It can also be an intellectual construction of a virtual phenomenon. This
denomination is in fact used to clearly distinguish the phenomenon to be studied from its model which is also considered as a system. 

Shannon adds that a simulation process is constituted by the construction of the model and by the analytical use which is made of the model to study the system.

**Computeur simulation definition**

Computer simulation is in fact inseparable from the *experimental process* which is linked to its objective. 

  "Computer simulation is the discipline of designing a model of an actual or theoretical physical system, executing the model on a digital computer, and analyzing the execution output." Fishwick, 1997.

This definition gives a global overview of a process of a computer simulation process. Fishwick defines this discipline as an iterative and nonlinear process composed of three interdependent fundamental tasks:

1. The development of the model.
2. Running the model on a computer.
3. Analysis the execution of the model and the obtained results. 

.. image:: img/simu_def_fish.png
    :align: center

This definition clearly shows the importance of the model and its development for the design of a simulation. 

**Simulation as an experimental process**

Most of the time, Fishwick's definition is sufficient to illustrate clearly and simply the different stages that constitute the development of a computer simulation. However, it may be interesting to detail these steps: 

1. Definition of the problem: clearly define the objectives of the study. What are the questions we want to answer?
2. Definition of the system: determine which parts of the system to study. The model will then be developed according to the objectives set.
3. Definition of the model: develop a first model graphically or in pseudo code. This involves defining the different entities that belong to the system: components, variables, interaction between components, etc.
4. Preliminary analysis of the experiment: determine what the criteria are which will make it possible to assess the quality of the experiment: what are the parameters to vary, with what amplitude and over how many runs? How experience will be needed for the whole experiment?
5. Definition of initial parameters: determine and collect the data that are necessary for the development of the initial values ​​that will be used for the configuration of the model.
6. Implementation of the model: convert the developed model into a simulation language to allow its implementation on a computer.
7. Verification and validation of the model: check that the simulator correctly execute the model to validate the results obtained by it. Are they acceptable and representative of the system being want to study?
8. Experimentation: run the actual simulation to recover desired results and perform a sensitivity analysis of the model taccording to the initial parameters.
9. Interpretation of the results: conclude on the model from the results obtained.

.. image:: img/simu_det_fish.png
    :align: center

This more complete description provides a better idea of what a computer simulation is and the different challenges to be overcome. It also introduces the validation and verification steps in a simulation: these two steps are fundamental and cannot be dissociated from the experimental process (even more in the context of a computer simulation). 

**Dynamic systems**

Now that we have an idea of what a computer simulation is, it is worth presenting the different concepts that are manipulated to model real systems. In this context, the notion of *dynamic system* is essential. By *dynamic system* we mean:

    "Any formal construct which provides general modeling concepts for various kind of disciplines." Rozenblit & Zeigler, 1993.

Most models used to represent a *dynamic system* are based on the abstractions offered by the **systems theory**.

The basic principle of this theory is to consider that a system can be specified according to two fundamental aspects:

- The *behavior of the system* at its limits (external behavior): the observable reactions of the system from outside it;
- The *internal structure* of the system: its internal state and its intrinsic functioning (its dynamics). 

Thus, at the highest level of abstraction, a dynamic system is seen as a black box which has an input, an output and an internal structure as shown in the following figure:

.. image:: img/dyn_sys.png
    :align: center

The external behavior of the system is defined by the relationship between the history of inputs and the history of observed output results. In other words, it characterizes how the system reacts from the observer's point of view at the input / output level (I/O).

The internal structure of the system is defined according to three parameters:

- The *system state* which is generally represented by one or more variables called **state variables**. 
- The *system state change mechanism*, which refers to how *state variables* change based on inputs or on their own. This aspect of *system dynamics* is modeled by what is generally referred to as **the state transition function**. 
- The *production mechanism* of the system which refers to how the system produces an output result based on its internal state. This is called the **system output function**. 

Generally, the last two points are implicitly grouped together when talking about the dynamics of the system which concerns the mechanisms of evolution of the system over time, as opposed to the state of the system which refers to the situation in which the system is at a specific time step.

The important point to remember here is the distinction that systems theory makes between the different aspects of a *dynamic system*: behavior and internal structure.

**The different temporal models used for the representation of dynamic systems**

A dynamic system is defined by how it evolves over time. So, one of the most important features of a model which represent a dynamic system is how time is represented.

There are three types of time representations:

- *Continuous* time models: in a finite time interval, the system state variables change in value infinitely often, ie continuously.

  .. image:: img/continuous.png
    :align: center

.. warning::
  The simulation of continuous models raises many problems due to the nature of the computer: it is simply impossible to reproduce the continuity of the dynamics of a system because it evolves infinitely often while the computer simulation needs punctual computations.

- *Discrete* time models: the time axis is discretized according to a constant period of time called time step (dt). The evolution of the system state variables is done in a discrete way, ie instantaneous, from t to t + dt.

  .. image:: img/discrete.png
    :align: center

.. note::
  The simulation of discrete models is easy. When the functions which implement the dynamics of the system are clearly defined, it is only necessary to set up an algorithm that applies these functions and then increments time.

  .. image:: img/time_discrete.png
    :align: center

- *Discrete event* time models: the time axis is generally continuous, ie represented by a real number. However, unlike continuous models, system state variables change discretely to specific times that are called *events*.

  .. image:: img/events.png
    :align: center

.. note::
  There are three ways to simulate discrete event time models: (1) activity scanning, (2) interaction process and (3) event sceduling. The last one is the most common way and is described by the figure below.

  .. image:: img/time_event.png
    :align: center

**Modeling & Simulation theory**

Because to what it allows, computer simulation should not be only considered as a tool but as a discipline and should therefore be theorized. This is the goal of Zeigler's *Modeling and Simulation theory*.

Thereby, the Modeling and Simulation theory helps to identify the different entities that constitute a simulation and study the relations that exist between these different entities. This is to give precise definitions to the different concepts that are manipulated in the field of computer simulation.

There are 6 entities clearly defined in the Modeling and Simulation theory:

- The *source system* and its behavioral database. The source system corresponds to the environment to be modeled. It must be seen as a source of observable data that constitutes what is called the behavioral database.
- The *experimental scope*. It is a specification of (1) the observing conditions of the system and of (2) the objectives of the simulation project.
- The *model*. It refers to the specification of all the instructions used to generate the behavior of the system.
- The *simulator*. It refers to any computing system capable of executing the model and generate its behavior. By separating a model from its simulator, a model can be run by different simulators which increases its portability.
- The *simulation relationship*. It defines the notion of validity of the model. *Does the modeling which is made of the system is an acceptable simplification of this one according to the qualitative criteria chosen and the objectives of the experimentation ?*
- The *modeling relationship*. It defines the notion of validity of the simulator. *Does the simulator correctly generates the behavior of the model ? Does the simulator reproduces the mechanisms defined in the model (without introducing errors) ?*

  .. image:: img/resume.png
    :align: center

The Modeling and Simulation theory makes it possible to highlight, through the modeling and simulation relationships, important issues related to simulation such as the simplicity of the model, the behavior of the simulated model, the validation of the simulation, the reproducibility of the simulation, etc. We will discuss some of these issues in more detail later.

2. Multi-Agent Based Simulation
--------------------------------------------------------------------------------

**Difficulties of classical modeling**

To model dynamic systems, a mathematical approach has long been used. Called Equation Based Model (EBM), it is build on an interrelation of a set of equations that captures the variability of a system over time. EBM represents the whole system and does not support an explicit representation of components (top-down). The whole system is globally represented by equations defined at the macroscopic level which does not make it possible to take into account the individual characteristics of the entities that compose the system. Moreover, this level of representation raises the question of the realism and the complexity of the parameters used to formulate the equations which model the system. So, EBM is most naturally used to model central systems.

.. note::
  Take the example of the prey / predatory model: it is used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey.

  .. image:: img/preypredatorebm.png
    :align: center

  It focus on the global variation of the prey and predator populations. Below, you can find the output of a prey/predator EBM simulation:

  .. image:: img/preypredatorebmout.png
    :align: center

.. warning::
  Limits of the Equation Based Model (EBM):

  - Large number of parameters sometimes hard to understand.
  - Diffculty to move from macro to micro level.
  - Does not represent behaviors but behaviors results.
  - Difficulty to represent behaviors.
  - Does not represent interactions and organizations.

To overcome EBM limitations, it is possible to use models that focus on entities and their interactions (bottom-up) and also considers that the dynamics of the system come from the interactions between the entities.

**An agent is a dynamic system**

Modeling a dynamic system using agents is simple because it is obvious that an agent can be considered as a dynamic system within the meaning of systems theory. Indeed, an agent has an internal state that changes according to his perceptions (inputs) and it has behaviors to react in its environment. 

.. image:: img/dyn_sys_agent.png
  :align: center

As shown in the figure above, an agent is defined by a set of perceptions (inputs), a set of actions (outputs) and we speak of the internal architecture of the agent to denote the mechanisms that define its intrinsic dynamics.

**Multi-agent modeling**

The multi-agent approach is based on an individual-centered approach: it considers that it is possible to model not only individuals and their behaviors, but also the interactions that take place between these individuals. It considers that the overall dynamics of a system, at the macroscopic level, result directly from the interactions between the individuals who compose this system at the microscopic level. Thus, while EBM model the relationships that exist between the different identified entities of a system using mathematical equations, the multi-agent approach directly models the interactions generated by individual behaviors.

.. image:: img/mabs.png
  :align: center

To create a multi-agent simulation, you must follow the principles of the agent paradigm presented in the previous course:  
- Creating an artificial world made up of interacting agents (Agent-Based Models) living in an environment.
- Each agent is described as an autonomous entity.
- The behaviour of agents is the consequence of their observations, internal trends, beliefs and interactions with the environment and other agents.
- Agents act and change the state of the environment through their actions.

.. note::
  Take again the example of the prey / predatory model. Each entity (prey and predator) is represented by an agent and has behaviors:

  - Prey: move, eat, reproduce, flee and die.
  - Predator: move, eat, reproduce, hunt and die.
  
  Each agent activate one of its behavior according to its perception of the environment. This simulation focus on the local behaviors of the prey and predator populations. Below, you can find the output of a prey/predator EBM simulation:

  .. image:: img/prey_predator.jpg
    :align: center

Due to its ability to model the interactions between entities and the variations of a system at the micro level, Multi-Agent Based Simulation is used in many fields of application. 

- Special effects in movies:
  
  .. figure:: img/massive.png
    :align: center

    *Massive software for crowd simulation*

- Video games:
  
  .. figure:: img/glassbox.png
    :align: center

    *Glassbox engine for SimCity*

- Simulation of complex systems:
  
  .. figure:: img/flocking.png
    :align: center

    *Flock of birds simulation*

- Collective robotics:
  
  .. figure:: img/col_rob.png
    :align: center
  
    *Collective behaviors for cooperative actions*

3. Visualizing Multi-Agent Based Simulation
--------------------------------------------------------------------------------

4. Implementing Multi-Agent Based Simulation
--------------------------------------------------------------------------------

5. Implementing  a prey / predator simulation with Mesa
--------------------------------------------------------------------------------

The objective of this practical work is to implement a simulation of a prey - predator model. The prey - predator model is a simple ecological model, consisting of three agent types: wolves, sheep, and grass. The wolves and the sheep wander around the grid at random. Wolves and sheep both expend energy moving around, and replenish it by eating. Sheep eat grass, and wolves eat sheep if they end up on the same grid cell.

If wolves and sheep have enough energy, they reproduce, creating a new wolf or sheep (in this simplified model, only one parent is needed for reproduction). The grass on each cell regrows at a constant rate. If any wolves and sheep run out of energy, they die.

The implementation of this model will make you use several Mesa concepts and features:
  - MultiGrid.
  - Multiple agent types (wolves, sheep, grass).
  - Overlay arbitrary text (wolf's energy) on agent's shapes while drawing on CanvasGrid.
  - Agents inheriting a behavior (random movement) from an abstract parent
  - Writing a model composed of multiple files.
  - Dynamically adding and removing agents from the schedule.

The goal is to implement a prey - predator model closely based on the NetLogo Wolf-Sheep Predation Model: *Wilensky, U. (1997). NetLogo Wolf Sheep Predation model*. http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation

**Practice yourself!**

Download the following archive which contains the project from which to start and extract it. The extracted folder contains 6 python files:

- *prey_predator/random_walker.py*: this defines the *RandomWalker* agent, which implements the behavior of moving randomly across a grid, one cell at a time. Both the Wolf and Sheep agents will inherit from it.
- *prey_predator/agents.py*: defines the Wolf, Sheep, and GrassPatch agent classes.
- *prey_predator/schedule.py*: defines a custom variant on the RandomActivation scheduler, where all agents of one class are activated (in random order) before the next class goes -- e.g. all the wolves go, then all the sheep, then all the grass.
- *prey_predator/model.py*: defines the Prey-Predator model itself.
- *prey_predator/server.py*: sets up the interactive visualization server
- *run.py*: launches a model visualization server.

So, now it's up to you to work and implement the prey - predator model:

1. Defines the Wolf, Sheep, and GrassPatch agent classes in the *prey_predator/agents.py* file.

 - A sheep that walks around, reproduces (asexually) and gets eaten.
 - A wolf that walks around, reproduces (asexually) and eats sheep.
 - A patch of grass that grows at a fixed rate and it is eaten by sheep.

2. Defines the Prey-Predator model by completing the *prey_predator/model.py* file.

3. Sets up the interactive visualization server by completing *prey_predator/server.py* file.

 - Display the different agents on the grid. 
 - Added buttons to control the initial settings.

4. Tune the initial parameters to find a balanced state in the model: none of the species disappears during the simulation. The output graph should be like that:

.. image:: img/preypredatorebmout.png
  :align: center
