---
layout: event
title: "Master Thesis Defense: Bug Detection in Distributed Systems with Platform-independent Fault Injection: A Case Study at Adyen"
categories: [events, defenses]
start: "10:00"
end: "12:00"
speaker: Nick Dekker
where: Lecture hall D@ta, Building 36
---

**Abstract**

Fault injection has been a long-standing technique for testing software. Injecting faults into a system, either in production or development environments, offers unique opportunities to discover bugs that are difficult to reproduce using conventional testing methods. However, it is widely considered to have a high implementation threshold. Due to this threshold and out of skepticism of its effectiveness, many developers are resistant to the idea of injecting faults as a testing method. This thesis introduces ``Yet Another Fault Injector": YAFI, a platform-independent fault injection framework designed for distributed systems. Our hope is that this framework is adopted to research future fault injection and causes the bar to apply fault injection on previously hard-to-test systems to be lowered.
We perform a case study to evaluate YAFI and find that with minimal implementation of fault injectors and little developer input, bugs and flaws can be detected in a system by running fault injection experiments.
A case study, performed at Adyen, shows that the system under test (SUT) is resilient in certain scenarios. Automatically generated failure plans have been shown to result in system behavior without requiring in-depth knowledge of the SUT. Injected faults were reflected in the response metrics when information from the experiments was used to generate additional failure plans. This emphasizes the need for gathering proper response data and system metrics to evaluate the system's behavior under different fault conditions.
Additionally, YAFI has been executed on a project based on Apache ZooKeeper, to show portability to other systems.

By introducing YAFI and showcasing its effectiveness through the case study, this thesis contributes to the advancement of fault injection techniques and encourages wider adoption of fault injection for testing distributed systems.
