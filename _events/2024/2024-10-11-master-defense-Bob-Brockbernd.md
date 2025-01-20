---
layout: event
title: "MSc Defense: Static Deadlock Analysis for Kotlin Coroutines"
categories: [events, defenses]
start: "13:30"
end: "15:30"
speaker: Bob Brockbernd 
where: Echo hall B1, TU Delft
---

**Summary**

Asynchronous programming is often a difficult and non-trivial task. To make asynchronous programming more straightforward, languages are continuously introducing new syntax and patterns, making it easier to think about and develop solutions for concurrent problems. JetBrains introduced coroutines for Kotlin in 2018. Although Kotlin coroutines promise safe execution and concise code, it is not immune to concurrency bugs such as deadlocks. Particular *runBlocking* deadlocks are common when working with Kotlin coroutines. While other languages have made various advancements in detecting deadlocks, Kotlin lags behind.

In this work, we present two static analysis techniques that help developers detect and prevent deadlocks. The first technique, focused on the *runBlocking* problem, successfully identified dangerous patterns in open source repositories, leading to their resolution. Additionally, this technique has been integrated into JetBrains flagship IDE: IntelliJ IDEA. The second technique, aimed at general deadlock detection, has been developed and tested as a prototype. By using existing modeling techniques combined with novel approaches we have been able to accurately predict deadlocks in a controlled environment. Overall, this study tackled a common problem in Kotlin coroutines and made the first steps toward general deadlock detection.
