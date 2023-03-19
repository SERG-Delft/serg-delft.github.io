---
layout: event
title: "SERG talk: An Empirical Study of Software Vulnerabilties via Fine-grained Analysis in Maven"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Amir M. Mir
where: Hybrid
---

***Abstract***
Reusing software libraries is a pillar of modern software engineering and the average Java application depends on
40 third-party projects/libraries in 2022. Unfortunately, relying on such libraries exposes a project to potential vulnerabilities
and may put an application and its users at risk. Research on software ecosystems has shown that more and more projects are
affected by such vulnerabilities. However, previous investigation usually reason about dependencies on the dependency level and
we believe that this highly inflates the actual number of affected packages. In this work, we study the effect of transitivity and
granularity on vulnerability propagation in the Maven ecosystem. In our research methodology, we gathered a large dataset of
3M recent Maven packages. For this dataset, we obtain the full transitive set of dependencies, construct whole-program call
graph and perform reachability analysis. This approach allows us to identify Maven packages that are actually affected by using
vulnerable dependencies.
Our empirical results show that: (1) about 1/3 of packages in our dataset are identified as vulnerable if and only if all
the transitive dependencies are considered. (2) less than 1% of packages have a reachable call path to vulnerable code in their
dependencies, which is far lower than that of a naive dependency-based analysis. (3) limiting the depth of the resolved dependency
tree might be a useful technique to reduce computation time for expensive fine-grained (vulnerability) analysis.