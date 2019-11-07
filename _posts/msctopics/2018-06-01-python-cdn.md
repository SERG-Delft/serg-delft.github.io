---
layout: page
title: Call-based dependency networks for Python
where: TU Delft
contact: Georgios Gousios
---

#### Project description

In today’s software development, most programs comprise an ever growing list of
other programs they depend on. The Online Package Repositories (OPRs) of modern
programming languages such as Java’s Maven, JavaScript’s NPM, or Python's PyPI,
allow the efficient (re-)use and combination of such existing functionality in
one’s own program. As much as it is handy, reuse of packages through package
repositories is not without problems.

One solution to many of those problems is building callgraph-based dependency
networks: instead of relying on dependency information from the package manager,
we build callgraphs for each version of each package version on the package repository and then we link those together.

The purpose of this project is to build such a callgraph based dependency
network for Python (or another dynamically typed language). The main issue
with such languages is the accurate building of callgraphs. For this reason,
the project needs both to use static callgraph generators and dynamic instrumentation while running the program's tests.


#### Related work

[1] J. Hejderup, A. van Deursen, and G. Gousios, “Software Ecosystem Call Graph for Dependency Management,” in Proceedings of the 40th International Conference on Software Engineering: New Ideas and Emerging Results, New York, NY, USA, 2018, pp. 101–104.

#### Contacts about the project:

* [Joseph Hejderup](mailto:j.i.hejderup@tudelft.nl) (TU Delft)
* [Georgios Gousios](mailto:g.gousios@tudelft.nl) (TU Delft)
