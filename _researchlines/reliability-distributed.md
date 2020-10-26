---
layout: research-line
title: "Reliability of Distributed Software Systems"
description: Develop methods and tools for increasing reliability of concurrent and distributed systems.
responsible: "Burcu Kulahcioglu Ozkan"
---

Today’s software is evolving in the direction of more concurrency (to exploit multiple cores) and decentralization (to exploit networked systems). With the increasing use of mobile devices and cloud services, the applications we use today are deployed to geo-replicated distributed systems, easily accessible from everywhere.

However, it is difficult to implement distributed systems correctly since their behavior is more complicated than classical sequential programs. The nondeterminism in the delivery order of concurrent messages, network failures, or node crashes may result in subtle executions that lead to buggy behavior. It is difficult for the programmers to consider all possible executions during the system design and implementation. The reliability of distributed systems requires different techniques than the techniques designed for sequential software. 

The goal of this research line is to build program analysis, testing, and debugging methods for increasing the reliability of concurrent programs and distributed systems. While our interests span different kinds of concurrent programs (asynchronous, event-driven, etc), we currently focus on testing distributed systems, asking the following question: 

**How can we design efficient tests to detect and diagnose bugs** that occur due to unexpected event orderings or  faults in:

* **Fault-tolerant consensus systems** - that implement consensus protocols such as Paxos and Raft
* **Weakly consistent systems** - that provide weak levels of consistency such as causal or eventual consistency in favor of higher availability
* **Blockchains** – that is basically a distributed, decentralized database that stores information in a chain of blocks 

The research is related to the work in the [CI4SE]({% link _researchlines/ci4se.md %}), [Software Engineering for Fintech](https://se.ewi.tudelft.nl/research-lines/se-for-fintech/), and [Software Quality](https://se.ewi.tudelft.nl/research-lines/software-quality/) research lines.
