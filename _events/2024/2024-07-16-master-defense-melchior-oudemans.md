---
layout: event
title: "Master Thesis Defense: Coverage-Guided Testing of Graph Processing Applications"
categories: [events, defenses]
start: "09:00"
end: "10:30"
speaker: Melchior Oudemans
where: Arena, Echo Building 

---
**Abstract**

The rise of graph processing has led to an increase in the usage of graph databasesand the availability of various frameworks. Graph databases have become more accessibleand, in specific instances, can compete with relational databases. Testing anapplication with a relational database backend has shown limited test coverage, andcurrent test generators cannot cover every branch condition in graph processing applications.There is a lack of test methods specifically designed for applications thatutilize graph structures.
This thesis presents PGFuzz, a coverage-guided, schema-aware fuzzer for graphprocessing applications. PGFuzz utilizes existing graph generators to generate inputsand applies graph-specific mutations to alter the graph state. These mutationsare schema-aware, designed to cover the graph model search space and satisfy logicalconditions from real-world applications. The mutations involve adding new graphelements, removing graph elements, modifying existing elements, altering propertyvalues, and violating graph constraints. When compared against existing graph generatorsand a random byte mutation approach on the nine real-world examples in ourbenchmark suite, PGFuzz demonstrates an increase in coverage over time and detectsmore logic errors than the other methods. PGFuzz can cover all previously uncoveredbranching.
