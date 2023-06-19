---
layout: event
title: "Master Thesis Defense: Testing Distributed Database Isolation through Anti-Pattern Detection"
categories: [events, defenses]
start: "14:00"
end: "16:00"
speaker: Jason Qiu
where: HB 13.140, Building 36

---
**Abstract**

Distributed databases often struggle to fulfill their transactional isolation guarantees due to sharding and replication. As a result, the problem of checking isolation levels is consistently receiving attention from academia and industries. Transactional dependency graphs form a useful abstraction to analyze the transactions’ dependencies and check for isolation anomalies using graph-based anti-patterns. Meanwhile, graph databases, known for their efficiency and convenience in graph representations and analytics, become promising for implementing isolation level checkers. In this work, we present a novel isolation level checker in the distributed graph database, ArangoDB. We collect execution histories from ArangoDB, operating in both single-machine and cluster modes. Also, we transform the execution histories to a dependency graph in another ArangoDB server. We then utilize customized AQL queries to detect anti-patterns on the graph. Our evaluation demonstrates the effectiveness and scalability of our checker, as well as its efficiency compared to existing isolation checkers. Also, we have found three underlying factors that are significantly correlated with the runtime of the checker: history length (the number of committed transactions), density (the density of the dependency graph), and contributing traversals (the number of traversals spent on cycles). 

The thesis artifact is available at [https://github.com/jasonqiu98/GRAIL-artifact/tree/thesis](https://github.com/jasonqiu98/GRAIL-artifact/tree/thesis).
