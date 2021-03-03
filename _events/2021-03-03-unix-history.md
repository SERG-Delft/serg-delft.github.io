---
layout: event
title: "Evolution of the Unix System Architecture (Guest Lecture IN4315 Software Architecture)"
categories: [events, guest-lecture]
start: "13:45"
end: "15:30"
speaker: Diomidis Spinellis
where: Online (Zoom)
---

Unix has evolved for almost five decades, shaping modern operating systems, key software technologies, and development
practices. Studying the evolution of this remarkable system from an architectural perspective can provide insights on how to manage
the growth of large, complex, and long-lived software systems. Along main Unix releases leading to the FreeBSD lineage we examine
core architectural design decisions, the number of features, and code complexity, based on the analysis of source code, reference
documentation, and related publications. We report that the growth in size has been uniform, with some notable outliers, while
cyclomatic complexity has been religiously safeguarded. A large number of Unix-defining design decisions were implemented right
from the very early beginning, with most of them still playing a major role. Unix continues to evolve from an architectural perspective,
but the rate of architectural innovation has slowed down over the system’s lifetime. Architectural technical debt has accrued in the
forms of functionality duplication and unused facilities, but in terms of cyclomatic complexity it is systematically being paid back through
what appears to be a self-correcting process. Some unsung architectural forces that shaped Unix are the emphasis on conventions
over rigid enforcement, the drive for portability, a sophisticated ecosystem of other operating systems and development organizations,
and the emergence of a federated architecture, often through the adoption of third-party subsystems. These findings have led us to
form an initial theory on the architecture evolution of large, complex operating system software.

This lecture is based on the IEEE TSE paper "Evolution of the Unix System Architecture: An Exploratory Case Study", authored by [Diomidis Spinellis](https://www2.dmst.aueb.gr/dds/) and [Paris Avgeriou](http://www.cs.rug.nl/~paris/).

- [paper](https://ieeexplore.ieee.org/document/8704965) (Open Access)
- [GitHub Repo](https://github.com/dspinellis/unix-history-repo)

[diomidis]: 