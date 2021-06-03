---
layout: research-line
title: "DevOps"
description: "To understand and improve the modern CI/CD and DevOps practices."
responsible: "Sebastian Proksch, Arie van Deursen"
---

Collaborative Software Engineering has been revolutionized by novel practices like CI/CD or DevOps. We try to understand how to further improve development processes by analyzing the artifacts and the traces that are left behind by developers that adopt these practices. We also try to expand the interpretation of the underlying principles to help developers from other fields, like data analysts or AI experts, with adopting these practices to gain similar benefits.

Right now, we have several open thesis proposals in this area:

* **Community-dependent interpretation of CI principles**: Continuous integration is based on a set of principles and practices that developers should follow to gain full benefits. The interpretation of these principles does not seem to be universal though and different communities have developed a different understanding. For example, while the Java community agrees on the advantages of fixed version numbers for the reproducibility of builds, other communities always rely on "newest versions" and perform the equivalent of trunk-based development on the ecosystem level. We will analyze this observation across several communities.

* **Continuous integration for AI**: While CI has been widely adopted in traditional software teams and the benefits have been proven, it did not find its way into related communities. Non computer-scientists (mathematicians, data analysts, AI experts, ...) might be used to different workflows and might not be aware of the benefits of sucha process. We will analyze how to transfer best practices of traditional software engineering into new fields. For example, by rejecting changes to an AI model that has negative impact on the memory consumption of a model.

* **Continuous experimentation in (mobile) marketplaces**: Continuous experimentation is a release engineering technique that investigates the effects of new features on the user population before a big roll out. Through monitoring the effects on relevant business metrics (like click rates, performance, active users, ...) it can then be decided on the process level, whether features are included in the software or whether they should be rolled back. This is challenging for apps that are released on marketplaces though, because the design of such a release channel makes it impossible to release multiple verisons of a software at the same time.

* **Monitoring transient developer behavior**: Mega datasets about development behavior are availabel for easy analysis. However, these datasets only contain static information. Some development details are transient and do not get persisted in online repositories, like local changes to a file that are discard and never get pushed to the repository. We expect that developers often need help in situation, in which they are not sure what to do and that these situations are not well reflected in the public datasets, so we are going to analyze local behavior of developers to identify their pain points.

* **What can we learn from postmortem analyses?**:  Many information technology organizations, after the occurrence of a serious operational issue, analyse its causes and publish a postmortem analysis.  A large collection of such analyses is available [online] (https://github.com/danluu/post-mortems).  The aim of this research is to conduct a systematic study of these texts in order to answer the following research questions.  What kinds of primary faults lead to operational problems?  What kinds of secondary issues contribute to operational problems?  The questions can be answered through the hierarchical classification of the faults and issues as well as their statistical analysis.

* **Automatic detection of runtime code smells**: By analyzing trace data associated with calls made to the operating system or to library routines one can find problematic programming practices and improve a system's runtime efficiency and performance.  Examples of such practices are memory leaks; polling; repeated execution of expensive operations, such as context switches or program executions; function calls with incorrect parameters; useless function calls.  The aim of this research is to develop a tool that can identify such smells and validate its operation in practice.

Right now, these proposals are only stubs that will be extended over time. Please get in contact with the research line leaders if you are interested in understanding more details about these topics.
