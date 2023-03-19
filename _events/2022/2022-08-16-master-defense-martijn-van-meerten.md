---
layout: event
title: "Master Thesis Defense on Evolutionary Distributed Concurrency Testing of Blockchain Consensus Algorithms"
categories: [events, defenses]
start: "14:00"
end: "16:00"
speaker: Martijn van Meerten
where: Echo-Arena
---
**Abstract**

Distributed concurrency bugs (DC bugs) are bugs that are triggered by a specific order of events in distributed systems. Traditional model checkers systematically or randomly test interleavings but suffer from the state-space explosion in long executions. This thesis presents DiscoTest, a testing tool for DC bugs in blockchain consensus algorithms. The tool guides the search for schedules that trigger DC bugs by an evolutionary algorithm (EA). We apply the tool to Ripple’s consensus algorithm (RCA) and design and evaluate two representations and fitness functions.

We evaluate the representations on locality, redundancy, and scaling, by using graph edit distance (GED) to calculate the distance between schedules. We find that delay scheduling and priority scheduling are representations that allow variation operators of an EA to modify schedules. To evaluate the performance of the representations and fitness functions, we create a custom bug benchmark for RCA. An empirical comparison on the benchmark shows that delay scheduling with time fitness results in a significantly higher success rate than random search on one bug. Finally, we discover an in-production liveness bug in RCA.
