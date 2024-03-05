---
layout: event
title: "Lincheck: A Practical Framework for Testing Concurrent Data Structures on JVM"
categories: [events,guest-lecture]
start: "13:45"
end: "15:30"
speaker: Nikita Koval (JetBrains)
where: "EEMCS-Lecture Hall D@ta (36.HB.01.630)"
---

**Abstract**

In this guest lecture of CS4110, [Nikita Koval](https://nikitakoval.org/) from JetBrains will introduce [Lincheck](https://github.com/JetBrains/lincheck), a new practical and user-friendly framework for testing concurrent algorithms on the Java Virtual Machine (JVM). Lincheck provides a simple and declarative way to write concurrent tests: instead of describing how to perform the test, users specify what to test by declaring all the operations to examine; the framework automatically handles the rest. As a result, tests written with Lincheck are concise and easy to understand. The framework automatically generates a set of concurrent scenarios, examines them using stress-testing or bounded model checking, and verifies that the results of each invocation are correct. Notably, if an error is detected via model checking, Lincheck provides an easy-to-follow trace to reproduce it, significantly simplifying the bug investigation.
