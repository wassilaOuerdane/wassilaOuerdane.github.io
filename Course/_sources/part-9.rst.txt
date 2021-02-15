.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike> 

6.1 Negotiation protocols 
=============================

The other rules that form the negotiation protocol may address the follwoing issues: 

- rules for admission, which specify when an agent can participate in a negotiation dia-
logue and under what conditions;
- termination rules, which specify when an encounter must end (e.g., if one agent utters
an acceptance locution);
- rules for proposal validity, which specify when a proposal is compliant with some con-
ditions (e.g., an agent may not be allowed to make a proposal that has already been
rejected);
- rules for outcome determination, which specify the outcome of the interaction; in
argumentation-based frameworks, these rules might enforce some outcome based on
the underlying theory of argumentation (e.g., if an agent cannot construct an argument
against a request, it accepts it [Parsons et al., 1998]);
- commitment rules

1. An example of a negotiation protocol
---------------------------------------

We are at the end of this practical work.  The diffrent questions and function implemented till now will help you to run (very soon :-) )  a negotiation between two agents. 
Before to push the run button, you need to check that you have implemented all the necessary elements. For this, the following algorithm synthetises the conditions and the rules for the different moves during and interaction.  



.. image:: img/algo.png
  :width: 550


This algorithm is represented by the following transition state diagram and a possible output (interaction) is depicted in the figure.

.. image:: img/nego.png
  :width: 300




.. image:: img/ex_nego.png
  :width: 350

For recall, the different perfomatives used in the algorithm are described in what follows. 

1- PROPOSE(item): an agent sends this message after: 

- either by selecting randomly an item, or selecting the most prefered item. It means you need to calculate the global score of each item and to compare them. Actually, if you follow correctly the different steps, this is was done in  question #2 of "Testing your Prefrence Class". 
- generating the different arguments pro the item (Question 5 in "Generating Arguments"). 


2- ACCEPT(item): an agent sends this message if:



3- ARGUE(ITEM, REASONS):  an agent send this message after: 





2. Questions
-------------------------


1- Read carefully the algorithm and update your implementation (when it is necessary) that it corresponds to the described functioning. Again this is just an example and you can choose different stratgies/conditions. Feel free to make your own choices.  

2- set-up a number of agents and lunch the negotiation processes between each pair of agents. 

3- At the end of each negotiation: 

- récupérer l'agent gagnant, c'est celui qui a parlé en dernier avant un ACCEPT ou le récupérer dans les arguments qui ont zéro contre-arguments dans la structure de données. 

- récupérer du coup l'item (ou les items) défendu par ces arguments

- Faire une petie analyse pour chaque agent combien de negotiation il a gagné, quel item est le plus défendu, quel est le critère le plus mis en avant, et. 

4- à partir de :math:`n>4` construire le graphe d'arguments  (issus des différentes négotiations) et calculer l'ensemble des **arguments acceptables** selon une semantique de votre choix (cours: Semantic de Dung). Quelle conclusion peut on déduire

.. note::

 Question 4 is to be done only if you have managed to complete all the requested questions. 










