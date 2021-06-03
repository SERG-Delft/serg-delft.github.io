---
layout: event
title: "Sankie: an AI platform for DevOps"
categories: [events, talks]
start: "13:00"
end: "14:00"
speaker: Chandra Maddila, Microsoft Research
where: Social Data Lab
---

## Abstract

There has been a fundamental shift amongst software developers and engineers in the past few years. The software development life cycle (SDLC) for a developer has increased in complexity and scale. Changes that were developed and deployed over a matter of days or weeks are now deployed in a matter of hours. Due to greater availability of compute, storage, better tooling, and the necessity to react, developers are constantly looking to increase their velocity and throughput of developing and deploying changes. Consequently, there is a great need for more intelligent and context sensitive DevOps tools and services that help developers increase their efficiency while developing and debugging. 

Given the vast amounts of heterogeneous data available from the SDLC, such intelligent tools and services can now be built and deployed at a large scale to help developers achieve their goals and be more productive. 

In this talk, we present Sankie, a scalable and general service that has been developed to assist and impact all stages of the modern SDLC. Sankie provides all the necessary infrastructure (back-end and front-end bots) to ingest data from repositories and services, train models based on the data, and eventually perform decorations or provide information to engineers to help increase the velocity and throughput of changes, bug fixes etc. This paper discusses the architecture as well as some of the key observations we have made from wide scale deployment of Sankie within Microsoft.

We will discuss the construction of Sankie, its use for effort estimates on individual developer check-ins, and its use for differential bug localization in large-scale services.

The talk starts from our three recent papers, and sketches an outlook of further research in the direction of intelligent DevOps.

- Rahul Kumar, Chetan Bansal, Chandra Shekhar Maddila, Nitin Sharma, Shawn Martelock, Ravi Bhargava: [Building sankie: an AI platform for DevOps](https://dl.acm.org/doi/10.1109/BotSE.2019.00020). BotSE@ICSE 2019: 48-53

- 	Chandra Shekhar Maddila, Chetan Bansal, Nachiappan Nagappan: [Predicting pull request completion time: a case study on large scale cloud services](https://dl.acm.org/doi/10.1145/3338906.3340457). ESEC/SIGSOFT FSE 2019: 874-882

- 	Ranjita Bhagwan, Rahul Kumar, Chandra Shekhar Maddila, Adithya Abraham Philip: [Orca: Differential Bug Localization in Large-Scale Services](https://www.usenix.org/conference/osdi18/presentation/bhagwan). USENIX Annual Technical Conference 2019 (also at OSDI). Best paper award.


## Bio

Chandra Maddila is a Senior Research Engineer in Applied Sciences group, Microsoft Research.

His interest areas are at the intersection of Machine Learning, Artificial Intelligence and Software engineering, which has resulted in [various publications](https://dblp.org/pers/hd/m/Maddila:Chandra_Shekhar), including at ICSE 2019, ESEC FSE 2019, the Usenix Annual Conference 2019, and OSDI 2018.

He has finished his masters in Software Systems from [BITS Pilani](https://bits-pilani.ac.in/), India.


