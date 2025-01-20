---
layout: event
title: "PhD Defense: Test Amplification For and With Developers"
categories: [events, talk]
start: "17:00"
end: "19:30"
speaker: Carolin Brandt 
where: Senaatszaal, TU Delft
---

Including Layman's talk and Reception :)

**Summary**

Developer testing has become an established practice in large software projects.
The developers working on the functionality of a project also write short, automated scripts that check the behavior of their code.
While the benefits of developer testing are widely accepted, writing tests is still seen as tedious and time-consuming.
Researchers are working towards alleviating developer effort by automatically generating tests.
One approach to do this is test amplification, which modifies existing, manually written tests to create new tests that improve the strength of the existing test suite.
When trying to fully automatically generate tests, test generation tools face the relevance problem and the oracle problem:
Which behavior of the system is worth testing and what is the expected output to check for?
The developer already needs to have an understanding of these two aspects to write the code under test.
We propose to leverage this knowledge of the developer to improve the test amplification process.
Conjecturing that a consciously designed interaction is the key to an effective collaboration, we propose a developer-centric approach to test amplification that uses a dedicated test exploration tool to communicate and collaborate with the developer.

During the five design science studies in this thesis we investigate key factors for an effective collaboration between software developers and test amplification tools.
Starting off, we explore what is important in the amplified tests and the test exploration tool.
We also study the information needs of the developer when inspecting amplified tests, and the value test amplification can provide to the developer.
We explore the use of a visualization to convey the execution behavior and coverage impact of a test,
and the impact of explicit guidance towards a coverage target.
By collecting feedback from open source maintainers on amplified tests, we gather the types of changes developers can expect to make to amplified tests.
Through discussions with developers on partial, fuzzer-based tests that target coverage gaps, we learn that not all coverage gaps are relevant to be closed or worth the effort to close them.

Concluding this thesis, we formulate guidelines on how to design an effective collaboration between software developers and test amplification tools.
The insights we gained also include guidelines for developers on how to examine and edit amplified tests.
We learned that developers can contribute valuable, hard-to-automate improvements to amplified tests and call to focus on supporting the developers in their contributions over further focussing on full automation.
At the same time, we also observe the effort required from developers to understand and complete partial tests, which can inhibit the use of our tools.
Therefore, managing the trade-off between perceived value and required effort should be central during the design of an effective collaboration between software developers and automatic generation.
