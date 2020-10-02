---
layout: event
title: "SERG talk: Testing Consensus Implementations Using Communication Closure"
categories: [events, lunch-talks]
start: "14:00"
end: "15:00"
speaker: Burcu Kulahcioglu Ozkan
where: Online
---

Large scale production distributed systems are difficult to design and test. Correctness must be ensured whenprocesses run asynchronously, at arbitrary rates relative to each other, and in the presence of failures, e.g.,process crashes or message losses. These conditions create a huge space of executions that is difficult toexplore in a principled way. Current testing techniques focus on systematic or randomized exploration of allexecutions of an implementation while treating the implemented algorithms as black boxes. On the otherhand, proofs of correctness of many of the underlying algorithms often exploit semantic properties that reducereasoning about correctness to a subset of behaviors. For example, the communication-closure property, used inmany proofs of distributed consensus algorithms, shows that every asynchronous execution of the algorithmis equivalent to a lossy synchronous execution, thus reducing the burden of proof to only that subset. In a lossysynchronous execution, processes execute in lock-step rounds, and messages are either received in the sameround or lost forever—such executions form a small subset of all asynchronous ones. 

We formulate the communication-closure hypothesis, which states that bugs in implementations of distributedconsensus algorithms will already manifest in lossy synchronous executions and present a testing algorithmbased on this hypothesis. We prioritize the search space based on a bound on the number of failures in theexecution and the rate at which these failures are recovered. We show that a random testing algorithm basedon sampling lossy synchronous executions can empirically find a number of bugs—including previouslyunknown ones—in production distributed systems such as Zookeeper, Cassandra, and Ratis, and also producemore understandable bug traces.


This is a joint work with Cezara Dragoi, Constantin Enea, Rupak Majumdar, and Filip Niksic.

Accepted at [OOPSLA'20](https://2020.splashcon.org/track/splash-2020-oopsla)
