---
layout: event
title: "Checking Distributed Database Isolation through Anti-Pattern Detection"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Jason Qiu
where: Hybrid
---

**Abstract:**

Transactional isolation levels in distributed databases often struggle to fulfill their intended guarantees due to sharding and replication. As a result, the problem of checking isolation levels is consistently receiving attention from academia and industries. Recently, researchers have increasingly utilized dependency graphs and related graph-based anti-patterns in various isolation checkers. Graph databases, known for their efficiency and convenience in graph representations and analytics, offer a promising approach for implementing isolation level checkers. In this work, we present a novel implementation using ArangoDB, a popular graph database. We collect execution histories from ArangoDB, operating in both single-instance and cluster modes, and transform them into a labeled property model for storage in the graph database. We then utilize customized AQL queries to detect isolation levels by identifying anti-patterns. Through our experiments, we demonstrate that our graph-based checker is both comprehensive and efficient compared to existing isolation checkers. 

The thesis artifact is online at [https://github.com/jasonqiu98/GRAIL-artifact/tree/thesis](https://github.com/jasonqiu98/GRAIL-artifact/tree/thesis). 
