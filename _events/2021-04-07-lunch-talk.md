---
layout: event
title: "SERG talk"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Jeanderson Barros Cândido, Timothy Zemp
where: Online
---


**An Exploratory Study of Log Placement Recommendation in an Enterprise System (Jeanderson Barros Cândido)**

Logging is a development practice that plays an important role in the operations and monitoring of complex systems. Developers place log statements in the source code and use log data to understand how the system behaves in production. Unfortunately, anticipating where to log during development is challenging. Previous studies show the feasibility of leveraging machine learning to recommend log placement despite the data imbalance since logging is a fraction of the overall code base. However, it remains unknown how those techniques apply to an industry setting, and little is known about the effect of imbalanced data and sampling techniques. In this paper, we study the log placement problem in the code base of Adyen, a large-scale payment company. We analyze 34,526 Java files and 309,527 methods that sum up +2M SLOC. We systematically measure the effectiveness of five models based on code metrics, explore the effect of sampling techniques, understand which features models consider to be relevant for the prediction, and evaluate whether we can exploit 388,086 methods from 29 Apache projects to learn where to log in an industry setting. Our best performing model achieves 79% of balanced accuracy, 81% of precision, 60% of recall. While sampling techniques improve recall, they penalize precision at a prohibitive cost. Experiments with open-source data yield under-performing models over Adyen’s test set; nevertheless, they are useful due to their low rate of false positives. Our supporting scripts and tools are available to the community.

Preprint: [https://arxiv.org/pdf/2103.01755.pdf](https://arxiv.org/pdf/2103.01755.pdf)


**CInder - Find the matching project for your next CI Study (Timothy Zemp)**

Continuous Integration (CI) is a software development practice introduced by the Agile movement with the aim of delivering reliable software releases quickly by regularly integrating changes to the software. The spread and success of CI has lead to a spike in empirical software engineering research, examining the benefits and the impact of this new practice. Implementing Continuous Integration is relatively simple because it is only required to add a configuration file to the repository and register with a CI cloud provider. Unfortunately, due to its easy adaptability, in many software repositories the process is poorly implemented. This is a substantial risk that threatens the validity of CI-based studies unless care is taken in the selection of repositories. To overcome this risk we present CINDER, a tool that detects genuine CI configuration files. The tool works by using a random forest classifier trained on a labeled ground truth data set and various features describing the characteristics of configuration files. With CINDER we show that significant action within the pipeline and its regular adaptation is a strong indicator of the genuineness of a configuration file. By replicating a study we show that the selection of projects has a significant impact on the results of CI based studies. With CINDER we provide researchers with a tool to enhance the process of selecting applicable software repositories, consequently improving the quality and validity of their studies.

Master thesis: [https://tzemp.ch/Masterarbeit.pdf](https://tzemp.ch/Masterarbeit.pdf)

Timothy Zemp is a master student in Information System at the University of Zurich (UZH), Switzerland, where he also received his BSc in Informatics. He is interested in supporting developers during their daily work, e.g remove unnecessary tasks, speed up development processes. Besides studying, he is involved in several startups. His mission is to apply research in practice and, in this way, support his colleagues.
