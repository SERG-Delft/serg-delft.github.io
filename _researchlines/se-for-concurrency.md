---
layout: research-line
title: "Software Reliability for Concurrent and Distributed Systems"
description: Develop techniques and tools for increasing the reliability of concurrent and distributed systems.
responsible: "Burcu Kulahcioglu Ozkan"
---

Today’s software is evolving in the direction of more concurrency and decentralization. With the increasing use of mobile devices and cloud services, the applications we use today are deployed to geo-replicated distributed systems, easily accessible from everywhere. However, the increased complexity of the software systems makes it more difficult to reason about possible behaviors of a system and to produce correct software.

It is challenging to implement distributed systems correctly since their behavior is more complicated than classical sequential programs. The nondeterminism in the delivery order of concurrent messages, network failures, or node crashes may result in subtle executions that lead to buggy behavior. It is difficult for the programmers to consider all possible executions during the system design and implementation. The reliability of distributed systems requires different techniques than those designed for sequential software. 

This research line aims to build program analysis, testing, and debugging methods for concurrent programs and distributed systems. Our research interests span a broad spectrum of concurrent programs: multi-threaded, asynchronous, event-driven, and distributed systems. 

We aim to build software analysis and testing methods for including (but not limited to):

* Decentralized consensus systems and blockchains 
* Distributed systems with weak consistency and weak isolation 
* Distributed systems with microservice architecture
* Shared-memory multicore programs



### Recent Awards:

* <span style="color:#000080">**"Distinguished paper award"**</span> for our paper ["Randomized Testing of Byzantine Fault Tolerant Algorithms"](https://dl.acm.org/doi/abs/10.1145/3586053) at [OOPSLA'23](https://2023.splashcon.org/track/splash-2023-oopsla).


* <span style="color:#000080">**"Stellar Academic Research Grant"**</span> for the research proposal "Feedback-guided fault-injection testing of blockchain systems" from the [Stellar Development Foundation](https://stellar.org/foundation). 

* **[Ripple Bug Bounty Program Award](https://ripple.com/legal/bug-bounty/)** with the bug our recent work discovered in the XRP Ledger of Ripple. Levin Winter's contribution to the bug fix is acknowledged in the release notes of [XRP Ledger version 1.10.0](https://xrpl.org/blog/2023/rippled-1.10.0.html).

* <span style="color:#000080">**"Amazon Research Award"**</span> for the research proposal ["Coverage-directed randomized testing of distributed systems"](https://www.amazon.science/research-awards/recipients/burcu-kulahcioglu-ozkan) in [Fall 2022](https://www.amazon.science/research-awards/program-updates/79-amazon-research-awards-recipients-announced).

### Related MSc Courses:

* CS4405 - Analysis of Concurrent and Distributed Programs ([course page](https://cs4405.github.io/))
* IN4315 - Software Architecture ([course page](https://se.ewi.tudelft.nl/delftswa/index.html))


[Contact](mailto:b.ozkan@tudelft.nl) if you are interested in working on software testing, program analysis, concurrent programming, distributed systems, and blockchains.

<!--
The research is related to the work in the [CI4SE]({% link _researchlines/ci4se.md %}), [Software Engineering for Fintech](https://se.ewi.tudelft.nl/research-lines/se-for-fintech/), and [Software Quality](https://se.ewi.tudelft.nl/research-lines/software-quality/) research lines. -->


