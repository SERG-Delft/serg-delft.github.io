---
layout: event
title: "Practical Automated Network-Level Fault Injection
Testing of Service-Oriented Distributed Systems"
categories: [events, talk]
start: "13:00"
end: "15:00"
speaker: Delano Flipse
where: Echo Arena
---


### Abstract

**Exploring Beyond the Happy Path: Practical Automated Network-Level Fault Injection Testing of Service-Oriented Distributed Systems**

Organisations are increasingly adopting Microservice and Service-Oriented Architectures, moving from monolithic applications to (service-oriented) distributed systems. By their nature, distributed systems are prone to partial failures, where a subset of processes fail while others continue to operate. To assess the behaviour of the system when subjected to partial failures, we can inject faults that mimic partial failures. By automatically injecting all relevant combinations of faults, we can verify the system’s resilience or uncover resilience bugs. However, the search space consisting of all combinations of faults grows exponentially. Moreover, it requires significant engineering effort to adjust systems to work with existing state-of-the-art tools. This work investigates a practical approach to automated fault injection for service-oriented distributed systems while remaining efficient. We design a novel automated fault injection tool that uses network-level instrumentation to inject faults. By using an abstraction to model the system’s behaviour, we can dynamically infer information available to service-level instrumentation. Furthermore, we efficiently represent the search space as a search tree and prune it using multiple pruning policies. To evaluate our design, we developed an implementation of this design called Reynard. Compared to the current state-of-the-art, we show that Reynard is efficient, requiring equal or fewer states in the search space, has minimal overhead, and can be integrated into various existing benchmark systems with a feasible engineering effort. Furthermore, we demonstrate the applicability of Reynard by integrating it into an industry system, highlighting that it can run practical experiments and can identify real bugs. In conclusion, Reynard can provide a starting point for lowering the engineering effort required to perform automated fault injection testing, while increasing the confidence in the resiliency of systems.automated fault injection testing, while increasing the confidence in the resiliency of systems.

[Link to the MSc thesis](https://repository.tudelft.nl/record/uuid:1b478188-f61d-4f3f-93ab-443cfdccc78f)
