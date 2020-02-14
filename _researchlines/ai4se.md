---
layout: research-line
title: "Artificial Intelligence and Machine Learning for Software Engineering"
description: How can techniques from artificial intelligence and machine learning be used to improve complex software development tasks?
responsible: "Georgios Gousios, Maurício Aniche, Annibale Panichella"
---


In the late years, researchers (and large companies, such as Microsoft, Google, and Facebook!) have been successfully applying artificial intelligence and deep learning techniques in software engineering tasks, such as finding bugs, detecting system anomalies, infering types in dynamic languages, and etc. 

The goal of this research line is to explore how AI can help software engineers to produce
better software. There are many tribes of AI, namely Symbolists, Evolutionists, Bayesians, Kernel Conservatives, Connectionists). Our research focuses on applying these tribes to solve SE problems. We can divide our AI-related research topics in two main directions: **machine learning and deep learning for software engineering**, and **search-based software engineering**. 

## Machine Learning and Deep Learning for Software Engineering

Software repositories archive valuable software engineering data, such as source code, execution traces, historical code changes, mailing lists, and bug reports. This data contains a wealth of information about a project's status and history. Doing data science on software repositories, researchers can gain an empirically based understanding of software development practices, and practitioners can better manage, maintain, and evolve complex software projects.

In the recent years, the advances in Machine Learning and AI technologies, as demonstrated by the successful application of Deep Neural Networks in various domains did not go unnoticed in the field of Software Engineering (see the [ML for Big Code and Naturalness](https://ml4code.github.io/papers.html) and the [Awesome ML on Code](https://github.com/src-d/awesome-machine-learning-on-source-code) repositories). Researchers have applied DNNs to tackle issues such as automated program repair, code summarization, code structure representation, defect prediction, etc.

Our research topics include:

* **Type inference**: Inferring the type of a variable, especially in dynamically typed languages, can be a challenge. 

* **Log engineering**: Software monitoring is a fundamental practice in modern software systems. However, monitoring systems often depend on the quality of the log data that the software system produces. In this line of work, we aim to create recommenders that support developers in understanding what, when, and how to log their systems.

* **Bug detection**: Some bugs are definitely hard to be detected by humans. Or even by state-of-the-art static analysis tools. In this line of work, we focus on developing machine learning/deep learning models that are able to identify bugs that existing tools can not. 

* **Vulnerability detection**: Detecting bugs that can lead to security vulnerabilities via machine learning and grammar inference. ML can be used to learn patterns of bug related to security vulnerabilities by mining  open-source and industrial code (see for example [Firewall Testing](https://pure.tudelft.nl/portal/en/publications/a-machine-learningdriven-evolutionary-approach-for-testing-web-application-firewalls(af7bf5df-6fab-4739-ae38-27abf8a4fafe).html)).

* **Software refactoring**: The development of data-driven refactoring recommendation tools. More information about it can be found in our [Software Refactoring]({% link _researchlines/software-refactoring.md %}) research line.

## Search-based software engineering

The development, maintenance, and testing of large software products involve many activities that are complex, expensive, and error-prone. For example, complex systems (e.g., autonomous cars) are typically built as a composition of features that tend to interact and impact one another’s behavior in unknown ways. Therefore, detecting feature interaction failures with manual testing becomes infeasible and too expensive when the number and the complexity of the features increase.

Nowadays, researchers and large tech companies use **Computational Intelligence** (CI) to automate expensive development activities, since more development automation would require less human resources. 
One of the most common ways to make such automation is the **Search-Based Software Engineering** (SBSE), which reformulates traditional software engineering tasks as search (optimization) problems. Then, **CI algorithms** (e.g., genetic algorithms, genetic programming, simulated annealing) are used to automate the process of discovering (e.g., detecting software defects) and building optimal solutions (e.g., software fixes).

SBSE is not only an academic research area, but it is achieving significant uptake in many industrial sectors. For example, **Facebook** uses multi-objective solvers to automatically design system-level test cases for mobile apps [[1]](https://link.springer.com/chapter/10.1007/978-3-319-99241-9_1);  Google uses multi-objective solvers for regression testing [[2]](http://sebase.cs.ucl.ac.uk/fileadmin/crest/sebasepaper/YooNH11_01.pdf). SSBSE techniques has been also applied in the automotive domain (**IEE S.A.** [[3]](https://pure.tudelft.nl/portal/files/45811366/paperASE18N2016pdf.pdf)), in satellite domain (**SES S.A.** [[4]](https://pure.tudelft.nl/admin/files/47344874/main.pdf)) and security testing.

Our research topics include but are not limited to the following research topics:

* **Test Case Generation**: 
Developing tools that automatically synthetize (generate) test cases with high code coverage (e.g., branch coverage) and that reveal faults or trigger crashes. Related projects include [Botsing](https://github.com/STAMP-project/botsing) for crash replication and [EvoSQL](https://github.com/SERG-Delft/evosql) for testing SQL queries. We also actively contribute to the [EvoSuite](https://github.com/EvoSuite/evosuite) framework for unit-level testing [[5]](https://apanichella.github.io/publication/ieee-tse2018b/), [[6]](https://apanichella.github.io/publication/ssbse2018b/), [[7]](https://apanichella.github.io/publication/infsof2018b/).

* **AI-based Penetration Testing**: 
Enterprise web systems use different protection layers (e.g., input sanitization, Web Application Firewalls) against malicious attacks (**code injection**). Since cyber-attacks are increasingly sophisticated, these protection layers become complex and difficult to maintain and test manually. We develop penetration testing tools that use **machine learning** (ML) techniques to identify and predict malicious string patterns that are more likely violating the security layers. For example, we use SBSE in combination with ML to test [[8]](http://orbilu.uni.lu/handle/10993/34224) Vulnerable Web Application Firewalls (WAFs) and the input validation and sanitization procedures in front-end web applications [[10]](https://apanichella.github.io/publication/ieee-tse2018a/). 

* **Testing Autonomous Cars**: 
Self-driving cars, and in general automotive systems, are feature-based systems where different units of functionalities (features) work together. To test these complex systems in an automated fashion, we use ML, and SSBSE to find test scenarios (simulation settings) that violate system requirements, hence leading to software failures [[11]](https://apanichella.github.io/publication/ase2018/).

* ** Automated Program Repair **: 
Patching defective code is a human-intensive activity. The goal of this line for research is to develop techniques that can automatically generate correct patches boggy code without causing software regression. The most common techniques for program repair include evolutionary algorithms and machine learning (see for example [Repairing Firewall](https://ieeexplore.ieee.org/document/8109099/)).


## Collaborators

The lab collaborates with the following people/organizations (reported in alphabetic order):
* SVV Lab - Interdisciplinary Centre for Security, Reliability and Trust, University of Luxemburg
* Fitsum Kifetew, Fondazione Bruno Kessler
* Sebastiano Panichella, Zurich University of Applied Sciences
* Paolo Tonella, Universita' della Svizzera Italiana
