---
layout: event
title: "Master Thesis Defense on Probabilistic Concurrency Testing for Weak Memory Concurrency"
categories: [events, defenses]
start: "13:30"
end: "15:30"
speaker: Mingyu Gao
where: 2.W510 Hilbert, Building 28
---
***Abstract***

The Probabilistic Concurrency Testing (PCT) algorithm provides theoretical guarantees for the probability of detecting concurrency bugs in a sequential consistency memory model, but its theoretical guarantees do not apply to weak memory concurrency. The weak memory concurrency refers to the modern compiler’s optimization that relaxes the sequential consistency requirements. The PCT approach is based on the sequential consistency interleaving semantics, which does not hold for weak memory concurrency. It is because weak memory concurrency allows additional behaviors that cannot be produced by any interleaving execution.

Based on the PCT algorithm transforming the concurrency bug to the ordering constraints(bug depth), this thesis presents Probabilistic Concurrency Testing for Weak Memory (PCTWM) to capture the concurrency behavior in weak memory programs, further revising the notion of the bug depth to the constraints of communication relations between events.

We implement both the PCT and PCTWM algorithms on top of the state-of-the-art weak memory testing tool - C11Tester. We empirically evaluate the bug detection ability of the PCTWM on a set of well-known weak memory program benchmarks. Our results show that PCTWM can detect concurrency bugs more frequently than C11Tester.
