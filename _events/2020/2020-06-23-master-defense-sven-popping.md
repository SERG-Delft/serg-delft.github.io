---
layout: event
title: "Master Thesis Defense: Automated Crash Fault Localization"
categories: [events, defenses]
start: "13:30"
end: "15:00"
speaker: Sven Popping
where: Zoom
---

Debugging application crashes is an expensive and time-taking process, relying on the developer's expertise, and requiring knowledge about the system.
Over the years, the research community has developed several automated approaches to ease debugging.
Among those approaches, search-based crash reproduction, which tries to generate a test case capable of reproducing a given crash to make it observable to the developers, solely based on the stack trace included in the crash report.
We believe that this makes crash reproduction the perfect candidate to achieve end-to-end crash fault localization.
In this thesis, we explore and empirically evaluate the usage of search-based crash reproduction combined with spectrum-based fault localization on 50 real-world crashes.
Starting from a crash report, we generate crash-reproducing test cases and use them in conjunction with the existing or an automatically generated unit test suite as input for spectrum-based fault localization.
Our results show that, although, hand-written test cases remain the most efficient in the general scenario, automatically generated crash-reproducing test cases still reduce the number of statements to be investigated by developers.
Additionally, when considering the best-case scenario where only crash-reproducing test cases covering the fault are evaluated, we observe no statistically significant difference between the accuracy of fault localization when using hand-written or automatically generated test cases.
Our results confirm the feasibility of end-to-end automated crash fault localization.
The results also identify new challenges for both automated test case generation and fault localization, as well as when they are combined.

Thesis: [link](http://resolver.tudelft.nl/uuid:da6486bd-886c-44ac-832a-f9825f6a2ba8)
