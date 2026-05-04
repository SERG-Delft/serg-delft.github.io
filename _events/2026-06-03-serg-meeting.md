---
layout: event
title: "SERG Seminar"
categories: [events]
start: "13:45"
end: "14:45"
speaker: Finn Hackett
where: "Social Data Lab (B28, ground floor)"
---

For this week's SERG seminar, **[Finn Hackett](https://fhackett.com/)**, who is visiting our group, will be presenting his PhD work on linking formal models of concurrent and distributed systems with implementations.

**Title:** Linking Formal Models of Concurrent and Distributed Systems with Implementations at Compile and Runtime

**Abstract:** Reasoning about concurrent and distributed systems is hard. Tests are flaky, interleaving of operations is non-obvious, and failures may only occur under heavy load. Abstractly modeling a system's intended behavior can help cut through the implementation's incidental complexity and uncover key design flaws, but it does not answer whether an implementation actually conforms to its abstract design. Most recently, we have approached this matching problem via trace validation: record traces of implementation behavior and match them against a formal model in TLA+. Unlike existing trace validation techniques, we adapted timeboxes from linearizability checking to allow blackbox recording of time ranges in which an event happened. To deal with operations whose behavior is not atomic, we extended linearizability checking to add sub-steps, meaning a single black-box implementation event may be modeled as multiple atomic sub-steps. We performed validation of a diverse collection of concurrent systems: WiredTiger, an industrial database storage layer; ConcurrentQueue, an optimized non-linearizable concurrent queue; and Balanced Augmented Trees, a state of the art concurrent dictionary structure with linearizable range queries. In our evaluation, we found previously unknown bugs, and found that OmniLink outperforms state of the art linearizability checkers on longer traces.

I will also discuss our prior work on compiling specifications to executable code, and auto-instrumenting systems compiled in this way for trace validation. I'll also briefly overview our latest ongoing collaboration on using trace validation results as feedback for LLM based specification inference, to filter out provably inaccurate specifications.

**Bio:** Finn is a PhD student in the [Systopia](https://systopia.cs.ubc.ca/) and [Software Practices](https://spl.cs.ubc.ca/index.html) labs at the University of British Columbia. His interests relate to programming language design, implementation, and formally modeling systems. He usually targets domains that are challenging to program, like concurrent and distributed systems, compilers, interpreters. 


---
If you are interested to give a talk or host a discussion session in one of our next meetings, please contact Carolin Brandt via Mattermost or email.
