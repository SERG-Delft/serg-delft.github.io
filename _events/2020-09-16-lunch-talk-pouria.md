---
layout: event
title: "SERG talk: Designing objectives for search-based crash reproduction"
categories: [events, lunch-talks]
start: "14:00"
end: "15:00"
speaker: Pouria Derakhshanfar
where: Online
---

Evolutionary-based crash reproduction techniques aid developers in their debugging practices by generating a test case that reproduces a crash given its stack trace. In these techniques, the search process is typically guided by a single search objective called Crash Distance. Previous studies have shown that current approaches could only reproduce a limited number of crashes due to a lack of diversity in the population during the search.

In this talk, I will present our recent work on the redesign of the search-objectives for crash reproduction by (i) applying Multi-Objectivization using Helper-Objectives (MO-HO) on crash reproduction. In particular, we add two helper-objectives to the Crash Distance to improve the diversity of the generated test cases and consequently enhance the guidance of the search process. And (ii) the introduction of a new secondary objective, called Basic Block Coverage (BBC), taking into account the coverage of implicit code branches during the search. 

References:
- Derakhshanfar, P., Devroey, X., Zaidman, A., van Deursen, A., & Panichella, A. (2020). [Crash Reproduction Using Helper Objectives](https://research.tudelft.nl/en/publications/crash-reproduction-using-helper-objectives). In GECCO 2020 Companion - Proceedings of the 2020 Genetic and Evolutionary Computation Conference Companion (pp. 309-310). (GECCO 2020 Companion - Proceedings of the 2020 Genetic and Evolutionary Computation Conference Companion). ACM DL. https://doi.org/10.1145/3377929.3390077
- Derakhshanfar, P., Devroey, X., Zaidman, A. E., van Deursen, A., & Panichella, A. (2020). [Good Things Come In Threes: Improving Search-based Crash Reproduction With Helper Objectives](https://research.tudelft.nl/en/publications/good-things-come-in-threes-improving-search-based-crash-reproduct). In 35th IEEE/ACM International Conference on Automated Software Engineering (ASE ’20), September 21–25, 2020, Virtual Event, Australia IEEE / ACM. https://doi.org/10.1145/3324884.3416643
- Derakhshanfar, P., Devroey, X., & Zaidman, A. (2020). [It is not Only About Control Dependent Nodes: Basic Block Coverage for Search-Based Crash Reproduction](https://research.tudelft.nl/en/publications/it-is-not-only-about-control-dependent-nodes-basic-block-coverage). In A. Aleti, & A. Panichella (Eds.), Search-Based Software Engineering - 12th International Symposium, SSBSE 2020 Springer.
