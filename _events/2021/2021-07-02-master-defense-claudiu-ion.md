---
layout: event
title: "Master Thesis Defense on A Static-Based Approach to Detect SQL Semantic Bugs"
categories: [events, defenses]
start: "14:30"
end: "16:30"
speaker: Claudiu Ion
where: Online (Zoom)
---
While SQL engines are now capable of detecting a large number of syntactic mistakes, most often semantic errors are not detected, which can lead to serious performance issues or even security vulnerabilities being introduced in the system. This thesis proposes a set of 25 validated heuristics together with a new rule-based static analysis tool for detecting the most common types of semantic bugs in SQL queries, based on evidence from previous research. We conduct an empirical study on the prevalence of semantic bugs in SQL on two datasets with queries collected from different open source industry projects as well as on a large dataset of queries collected from StackOverflow posts. Manual analysis of more than 500 queries shows that our tool is able to detect semantic bugs in SQL queries with an accuracy of 97%. Furthermore, out of all 191,994 collected queries, we identified a total of 36,818 queries which contain at least one semantic bug, meaning that 19.17% of queries contained some semantic problem in their formulation. To the best of our knowledge, this is the largest dataset of SQL queries extracted from StackOverflow and could later be used for subsequent studies as well.