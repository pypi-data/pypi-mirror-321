=====================================
Nash_DAG
=====================================

Nash_DAG (directed acyclic graph) allows connecting multiple nodes, each of which is a one-shot
multilayer game, into a compound game. A DAG is similar to a tree, but it may be possible to reach the
same node through multiple paths. The graph will have one or more terminal nodes (one is super boring).
At a terminal node there is a score for each player. Non-terminal nodes will have rules specifying the
possible player actions at that node, and the child node that results from the combination of player actions.
The module will use reverse-induction to find the equilibrium probabilities of player actions at the
non-termnal nodes and sums the values at the child nodes weighted by the probability of the node being reached to
assign a value to non-terminal nodes. A node is identified by a key (generally a tuple) which contains
the information necessary to dtermine the possible player actions and child nodes.

The games at the nodes may have multiple nash equilibria, but in order to define a value for the non-terminal nodes
it is necessary that all equlibria at a given node have the same player payoffs. The easiest way to ensure this is to
make the payoffs at all terminal nodes sum to zero. In that case payoffs at non-terminal nodes must also sum to zero.

Currently there is only one sample Nash_DAG game called "patrik".
