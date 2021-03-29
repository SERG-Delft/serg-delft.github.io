---
layout: event
title: "SERG Lunch: Class Integration Testing (CLING)"
categories: [events, lunch-talks]
start: "12:30"
end: "13:30"
speaker: Pouria Derakhshanfar
where: Social Data Lab, Building 28
---

Search-based approaches have been used in the literature to automate the process of creating unit test cases. However, related work has shown that generated unit-tests with high code coverage could be ineffective, i.e., they may not detect all faults or kill all injected mutants. In this paper, we proposed an integration-level test case generator named CLING, that exploits the integration code of a pair of classes (caller and callee) that interact with one another through method calls. In particular, CLING generates integration-level test cases that maximize the Coupled Branches Criterion (CBC). CBC is a novel integration-level coverage criterion that measures how thoroughly a test suite exercises the interactions between callers and callees. We evaluate CLING on 140 pairs of classes from five different open-source Java projects. Our results show that (1) CLING generates test suites with high CBC coverage; (2) such generated suites can kill, on average, 10% mutants that are not killable by unit-level tests generated with EvoSuite for the same classes; (3) CLING detects 29 integration faults that remain undetected when using automatically generated unit-level test suites.
