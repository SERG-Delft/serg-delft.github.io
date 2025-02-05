---
layout: event
title: "\"Flaky Tests at Exact\", Master Thesis Defense"
categories: [events,thesis-defenses]
start: "14:00"
end: "15:30"
speaker: "George Vegelien"
where: "Echo, Hall-D"
---

George Vegelien, a master student working with Exact and supervised by Carolin Brandt and Arie van Deursen, will defend his thesis on the topic of flaky tests. Asterios Katsifodimos will act as the external examiner.

## Addressing Test Flakiness: Practical Approaches in a Database-Reliant Industrial System

[Link to Thesis on the repository](https://resolver.tudelft.nl/uuid:ad279f6c-fbc6-4104-90b7-0a5b9e1f0088)

#### Abstract:
In today's rapidly evolving software landscape, where continuous integration and continuous delivery are paramount, the presence of flaky tests poses a significant obstacle. These tests, exhibiting unpredictable pass/fail behavior, hinder development progress, waste valuable resources, and erode developer trust. This research delves into the root causes and mitigation strategies for flaky tests within a large-scale, database-driven industrial setting: Exact.  
The increasing reliance on databases in modern software systems, including Exact's own platform, necessitates a deeper understanding of the unique challenges posed by database-dependent tests. By analyzing flaky test behavior through repeated test runs on the same code, we identified key contributors to flakiness, including resource contention, test order dependencies, dirty tests that leave the system in an inconsistent state, platform-specific issues, and combinations thereof.  
Based on the root causes for flakiness at Exact, we developed and evaluated three mitigation strategies and supporting tools: minimizing redundant database background tasks, explicitly disposing of test data, and disabling database dirty tests. Our study resulted in a substantial reduction in flakiness, leading to a significant increase in the release rate from Exact from 60% to 96%. We improved the chance of their CI/CD pipeline passing with no code changes from 27% to 95%.  
Furthermore, this research highlights the importance of collecting and analyzing rich, granular test data to identify patterns and root causes of flakiness. Providing developers with actionable information from this analysis motivates them to address flakiness proactively. Moreover, understanding the interplay between different types of tests, such as the impact of dirty tests on other seemingly unrelated tests or in combination with other factors, is crucial for effectively mitigating cascading failures.
