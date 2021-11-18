---
layout: research-line
title: "Software Reliability for Concurrent and Distributed Systems"
description: Develop techniques and tools for increasing reliability of concurrent and distributed systems.
responsible: "Burcu Kulahcioglu Ozkan"
---

Today’s software is evolving in the direction of more concurrency (to exploit multiple cores) and decentralization (to exploit networked systems). With the increasing use of mobile devices and cloud services, the applications we use today are deployed to geo-replicated distributed systems, easily accessible from everywhere.

However, it is difficult to implement distributed systems correctly since their behavior is more complicated than classical sequential programs. The nondeterminism in the delivery order of concurrent messages, network failures, or node crashes may result in subtle executions that lead to buggy behavior. It is difficult for the programmers to consider all possible executions during the system design and implementation. The reliability of distributed systems requires different techniques than the techniques designed for sequential software. 

The goal of this research line is to build program analysis, testing, and debugging methods for increasing the reliability of concurrent programs and distributed systems. Our research interests span different kinds of concurrent programs, e.g., multi-threaded programs, asynchronous, event-driven, and distributed systems. 

We currently focus on testing distributed systems, asking how can we design efficient tests to detect and diagnose bugs that occur due to unexpected event orderings or  faults in:

* Fault-tolerant consensus systems - that implement consensus protocols such as Paxos and Raft
* Weakly consistent systems - that provide weak levels of consistency such as causal or eventual consistency in favor of higher availability
* Blockchains – that is basically a distributed, decentralized database that stores information in a chain of blocks 


### Ongoing projects:

<span style="color:#00A6D6">**[Open PhD position, application deadline: December 17th, 2021]**</span> We're looking for a motivated PhD student to work on testing fault-tolerance of distributed systems. 
You can find more information [on the application site](https://www.tudelft.nl/over-tu-delft/werken-bij-tu-delft/vacatures/details?jobId=4663)! 

**Ongoing MSc projects:** 

- Martijn van Meerten, *Search-based Testing of Ripple Consensus* (co-supervised with Annibale Panichella)

- Mingyu Gao, *Probabilistic Testing for Weak Memory Concurrency* (co-supervised with Soham Chakraborty)

**Available MSc projects:** 

- [Machine Learning for Concurrent Programs](https://projectforum.tudelft.nl/admin/thesis_projects/206) (co-supervision with [Earl T. Barr](https://earlbarr.com/))

<!--- [Probabilistic Testing for Weak Memory Concurrency](https://pl.ewi.tudelft.nl/master-projects/master/2021/06/07/Probabilistic-Testing-Weak-Memory-Concurrency/) (co-supervised with [Soham Chakraborty](https://www.st.ewi.tudelft.nl/sschakraborty/))-->

- [Design and Implementation of a Conflict-Free Replicated Datatype (CRDT) Library for Distributed Systems](https://projectforum.tudelft.nl/admin/thesis_projects/157)

- [Controlled Crash-recovery Testing of Distributed Systems](https://projectforum.tudelft.nl/admin/thesis_projects/161)


&nbsp;

[Contact](mailto:b.ozkan@tudelft.nl) if you are interested in working on software testing, concurrent programming, distributed systems, and blockchains.

<!--
The research is related to the work in the [CI4SE]({% link _researchlines/ci4se.md %}), [Software Engineering for Fintech](https://se.ewi.tudelft.nl/research-lines/se-for-fintech/), and [Software Quality](https://se.ewi.tudelft.nl/research-lines/software-quality/) research lines. -->


