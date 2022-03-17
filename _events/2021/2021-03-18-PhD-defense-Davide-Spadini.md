---
layout: event
title: "PhD Defense: Supporting Quality In Test Code For Higher Quality Software Systems"
categories: [events, talk]
start: "15:00"
end: "17:00"
speaker: Davide Spadini
where: Senaatszaal, TU Delft
---

**Summary**

Automated testing has become an essential process for improving the quality of software systems. Automated tests can help ensure that production code is robust under many usage conditions and that code meets performance and security needs. Nevertheless, writing effective tests is challenging and, unfortunately, often neglected. In the first part of this dissertation, we summarize and explain why test and production code are not treated with the same care, and we set our goal: we want to discover new techniques and tools to support developers when writing and reviewing code. To this aim, we investigate the impact of test design issues on code quality and the practices when writing and reviewing test code.

First, we create and make publicly available Pydriller, a Python framework to analyze software repositories that will help us gather important information for the following studies. Then, we study test design issues and their impact on the overall software code quality, demonstrating how important it is to have a good and effective test suite. Afterward, together with SIG, a company setting in which part of this dissertation was conducted, we study how developers in industry react to these test design issues. Our results show that the current detection rules for test issues are not precise enough and, more importantly, do not support prioritization. We present new rules that can be used to prioritize these issues and show that the results achieved with the new rules better align with developers’ perception of importance.

In the second part of the dissertation we focus on how to help developers better reviewing test code. First, we investigate developers’ needs when it comes to code reviewing, identifying seven high-level information needs that could be addressed through automated tools, saving up time for reviewers. Then, we focus on code review of test code specifically: we first study when and how developers review test code, identifying current practices, revealing the challenges faced during test code reviews, and uncovering needs for tools that can support the review of test code. Later, we investigate the impact of TestDriven Code Review (TDR) on the code review effectiveness, showing that it can increase the number of test code issues found. We discuss when TDR can and can not be applied and why not all developers see TDR as a worthy practice.




**Advisors:** Alberto Bacchelli, Arie van Deursen
