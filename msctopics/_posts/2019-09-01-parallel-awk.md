---
layout: page
title: Design and Implementation of a parallel awk-like language
categories: [sal-msc-topics]
where: TU Delft
contact: Diomidis Spinellis
---

#### Project description

The *[awk](https://en.wikipedia.org/wiki/AWK)*
programming language [1] simplifies the processing of field-separated
text files by specifying a predicate to select the lines to operate on
and an action to perform on them.
With suitable restrictions and specialized support on the actions
(mainly on operations with global variables) *awk*-like programs can be
executed in parallel, following the
[MapReduce](https://en.wikipedia.org/wiki/MapReduce) [2] paradigm
by splitting the input into multiple chunks,
running each chunk on a separate CPU core or node cluster, and then
combining the results with a suitable *reduce* operation.
The award-winning *DTrace* dynamic analysis tool [3] follows a similar
design to satisfy different requirements.
The objectives of this project are

* to design this language based on an examination of real-life awk programs,
* to implement the system in a modern systems programming language, such as Rust or Go, and
* to benchmark its performance over the classical version of awk.

#### Related work
[1] Alfred V. Aho, Brian W. Kernighan, and Peter J. Weinberger. *[The AWK Programming Language](https://ia802309.us.archive.org/25/items/pdfy-MgN0H1joIoDVoIC7/The_AWK_Programming_Language.pdf)*. Addison Wesley 1988.

[2] Yang, Hung-chih, et al. "Map-reduce-merge: simplified relational data processing on large clusters." *Proceedings of the 2007 ACM SIGMOD international conference on Management of data*. ACM, 2007.

[3] Gregg, Brendan, and Jim Mauro. *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X, and FreeBSD*. Prentice Hall Professional, 2011.

#### Contacts about the project

* [Diomidis Spinellis](mailto:D.Spinellis@tudelft.nl) (TU Delft)
