---
layout: event
title: "Trace aware random testing for distributed systems with probabilistic guarantees"
categories: [events, talks]
start: "15:00"
end: "16:00"
speaker: Burcu Özkan, MPI-SWS
where: Social Data Lab
---

## Abstract

Distributed and concurrent applications often have subtle bugs that only get exposed under specific schedules. While these schedules may be found by systematic model checking techniques, in practice, model checkers do not scale to large systems. On the other hand, naive random exploration techniques often require a very large number of runs to find the specific interactions needed to expose a bug. In recent years, several random testing algorithms have been proposed that, on the one hand, exploit state-space reduction strategies from model checking and, on the other, provide guarantees on the probability of hitting bugs of certain kinds.

These existing techniques exploit two orthogonal strategies to reduce the state space: partial-order reduction and bug depth. Testing algorithms based on partial order techniques, ensure non-redundant exploration of independent interleavings among system events by imposing an equivalence relation on schedules and ideally exploring only one schedule from each equivalence class. Techniques based on bug depth, exploit the empirical observation that many bugs are exposed by the clever scheduling of a small number of key events. They bias the sample space of schedules to only cover all executions of small depth, rather than the much larger space of all schedules. At this point, there is no random testing algorithm that combines the power of both approaches.

In this talk, I will present our trace-aware PCT (taPCTCP) algorithm, that extends and unifies several different algorithms in the random testing literature. It samples the space of low-depth executions by constructing a schedule online, while taking dependencies among events into account. Moreover, the algorithm comes with a theoretical guarantee on the probability of sampling a trace of low depth---the probability grows exponentially with the depth but only polynomially with the number of racy events explored.

We empirically compare our algorithm with several state-of-the-art random testing approaches for concurrent software on two large-scale distributed systems, Zookeeper and Cassandra, and show that our approach is effective in uncovering subtle bugs and usually outperforms related random testing algorithms.

This talk is based on and expands upon two recent OOPSLA papers, from 2018 and 2019:

- [Trace Aware Random Testing for Distributed Systems](https://people.mpi-sws.org/~burcu/files/oopsla19.pdf). Burcu Kulahcioglu Ozkan, Rupak Majumdar, Simin Oraee. Proceedings of the ACM on Programming Languages (PACMPL), volume 3, number OOPSLA, 2019.

- [Randomized Testing of Distributed Systems with Probabilistic Guarantees](https://dl.acm.org/citation.cfm?id=3276530). Burcu Kulahcioglu Ozkan, Rupak Majumdar, Filip Niksic, Mitra Tabaei Befrouei, Georg Weissenbacher. Proceedings of the ACM on Programming Languages (PACMPL), volume 2, number OOPSLA, 2018. _(Recipient of the Distinguished Paper Award)_


## Biography

[Burcu Özkan][burcu] is a postdoc researcher at Max Planck Institute for Software Systems, working with Rupak Majumdar. She got her PhD from Koc University under the supervision of Serdar Tasiran.

Her research aims to improve the reliability of software by building program analysis, testing and verification techniques. As software systems have become ubiquitous in our lives, modern applications are designed to be highly concurrent, responsive, fault tolerant and distributed. Increased complexity of the software systems makes it more difficult to reason about possible behaviors of a system and to produce correct software. Her research goal is to advance the state of the art of software reliability techniques for modern programming models and software systems. To this end, her research lies at the intersection of software engineering, formal methods, programming models and languages.

[burcu]: https://people.mpi-sws.org/~burcu/

