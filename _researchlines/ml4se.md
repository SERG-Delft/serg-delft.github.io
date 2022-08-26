---
layout: research-line
title: "Machine Learning for Software Engineering"
description: How can machine learning be used to improve complex software development tasks?
responsible: "Georgios Gousios, Maurício Aniche, Annibale Panichella"
---


Lately, researchers (and large companies, such as Microsoft, Google, and Facebook) have been successfully applying artificial intelligence and deep learning techniques in software engineering tasks, such as finding bugs, detecting system anomalies, infering types, etc. 

The goal of this research line is to explore how techniques deriving from AI and machine learning (ML) can be applied on software engineering tasks.

## Machine Learning for Software Engineering

Software repositories archive valuable software engineering data, such as source code, execution traces, historical code changes, mailing lists, and bug reports. This data contains a wealth of information about a project's status and history. Doing data science on software repositories, researchers can gain an empirically based understanding of software development practices, and practitioners can better manage, maintain, and evolve complex software projects.

In the recent years, the advances in Machine Learning and AI technologies, as demonstrated by the successful application of Deep Neural Networks in various domains did not go unnoticed in the field of Software Engineering (see the [ML for Big Code and Naturalness](https://ml4code.github.io/papers.html) and the [Awesome ML on Code](https://github.com/src-d/awesome-machine-learning-on-source-code) repositories). Researchers have applied DNNs to tackle issues such as automated program repair, code summarization, code structure representation, defect prediction, etc.

Our research topics include:

* **Code completion**: Helping developers code faster.

* **Type inference**: Inferring the type of a variable, especially in dynamically typed languages, can be a challenge. 

* **Log engineering**: Software monitoring is a fundamental practice in modern software systems. However, monitoring systems often depend on the quality of the log data that the software system produces. In this line of work, we aim to create recommenders that support developers in understanding what, when, and how to log their systems.

* **Bug detection**: Some bugs are definitely hard to be detected by humans. Or even by state-of-the-art static analysis tools. In this line of work, we focus on developing machine learning/deep learning models that are able to identify bugs that existing tools can not. 

* **Vulnerability detection**: Detecting bugs that can lead to security vulnerabilities via machine learning and grammar inference. ML can be used to learn patterns of bug related to security vulnerabilities by mining  open-source and industrial code (see for example [Firewall Testing](https://pure.tudelft.nl/portal/en/publications/a-machine-learningdriven-evolutionary-approach-for-testing-web-application-firewalls(af7bf5df-6fab-4739-ae38-27abf8a4fafe).html)).

* **Software refactoring**: Identifying pieces of code that need refactoring is a challenging task. We aim to build data-driven refactoring recommendation tools.

