---
layout: event
title: "Precise Temporal Analysis Of Source Code Histories At Scale"
categories: [events,lunch-talks]
start: "11:15"
end: "12:00"
speaker: Quentin Le Dilavrec
where: "Hybrid"
---

**Abstract**

This talk is related to the results of my PhD, which I defended last February.
I will present some of the results and mention the scientific contribution (papers),
but I will give priority to possible synergies between these works and the interests of the group.
Actually, during my PhD I developed a library to help with analysing histories of source code, called the HyperAST.
I believe the HyperAST could be used in the team to answer software engineering questions using the code versioned in github repositories.
The HyperAST presents an AST view to the source code, and provides features like structured diffs, tracking, reference analysis, dynamic queries, ...
Internally, it leverages a DAG representation where the nodes of the AST are deduplicated, i.e., a collection of unique code subtrees.
The HyperAST approach leverages its internal representation to offer new trade-offs when designing source code analyses,
notably, by splitting an analysis into modules that compute intermediate results only depending on local information,
then these intermediate results are computed and persisted once per deduplicated node,
thus making the overall analysis incremental and more capable of scaling on large software projects.
