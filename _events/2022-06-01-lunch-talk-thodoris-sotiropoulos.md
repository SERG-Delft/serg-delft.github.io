---
layout: event
title: "Well-Typed Programs Can Go Wrong: Enhancing the Reliability of Static Typing in Compilers"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Thodoris Sotiropoulos 
where: Hybrid
---

Thodoris Sotiropoulos, PhD student at the Athens University of Economics and Business, advised by Prof Diomidis Spinellis, will present his work on enhancing the reliability of static typing in compilers. 


**Abstract**

Despite the substantial progress in compiler testing, research endeavors
have
mainly focused on detecting compiler crashes and subtle miscompilations
caused
by bugs in the implementation of compiler optimizations. Surprisingly,
this growing
body of work neglects other compiler components, most notably the front-end.
In statically-typed programming languages with rich and expressive type
systems
and modern features, such as type inference or a mix of object-oriented
with functional
programming features, the process of static typing in compiler
front-ends is complicated
by a high-density of bugs. Such bugs can lead to the acceptance of
incorrect programs
(breaking code portability or the type system's soundness), the
rejection of correct
(e.g., well-typed) programs, and the reporting of misleading errors and
warnings.

This talk gives an overview of our recent work on enhancing the reliability
of static typing in compilers. Guided by the findings and observations
of our recent
empirical study on typing bugs found in popular JVM compilers,
we have designed a set of techniques that rely on both program
generation and
transformation-based compiler testing. The purpose of these techniques
is to generate programs,
or apply targeted transformations to existing programs in order to
detect various typing compiler bugs,
including type inference or soundness issues. Our implementation has
been used to test
the compilers of three well-known languages, namely, Java, Kotlin, and
Groovy. Currently,
we have found 156 bugs (137 confirmed and 85 fixed) with diverse
manifestations and root causes
in all the examined compilers. Most of the discovered bugs lie in the
heart of many critical components
related to static typing, such as type inference. We believe that our
work fills the research
gap in automated testing of static typing, and can drive future
researchers to build
appropriate methods and techniques for more holistic testing of compilers.
