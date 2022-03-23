---
layout: event
title: "SERG talk: Automatic Test Suite Generation for Key-Points Detection DNNs using Many-Objective Search"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Donghwan Shin, SnT, University of Luxembourg
where: Online
---

**Abstract:** Automatically detecting the positions of key-points (e.g., facial key-points or finger key-points) in an image is an essential problem in many applications, such as driver's gaze detection and drowsiness detection in automated driving systems. With the recent advances of Deep Neural Networks (DNNs), Key-Points detection DNNs (KP-DNNs) have been increasingly employed for that purpose. Nevertheless, KP-DNN testing and validation have remained a challenging problem because KP-DNNs predict many independent key-points at the same time---where each individual key-point may be critical in the targeted application---and images can vary a great deal according to many factors. 

In this paper, we present an approach to automatically generate test data for KP-DNNs using many-objective search. In our experiments, focused on facial key-points detection DNNs developed for an industrial automotive application, we show that our approach can generate test suites to severely mispredict, on average, more than 93% of all key-points. In comparison, random search-based test data generation can only severely mispredict 41% of them. Many of these mispredictions, however, are not avoidable and should not therefore be considered failures. We also empirically compare state-of-the-art, many-objective search algorithms and their variants, tailored for test suite generation. Furthermore, we investigate and demonstrate how to learn specific conditions, based on image characteristics (e.g., head posture and skin color), that lead to severe mispredictions. Such conditions serve as a basis for risk analysis or DNN retraining.

**Short bio:** Dr. [Donghwan Shin](https://donghwan-shin.github.io) is a research scientist at the SVV (Software Verification and Validation) group, led by Prof. Lionel Briand, at the Interdisciplinary Centre for ICT Security, Reliability, and Trust (SnT) of the University of Luxembourg (UL). He received his B.S., M.S., and Ph.D. in Computer Science from Korea Advanced Institute of Science and Technology (KAIST) in 2010, 2012, and 2018, respectively. His research interests lie in mutation testing, software engineering for deep learning, and log-based analysis. He has published over 20 research papers at venues such as ICSE, ICST, ISSTA, and MODELS and journals such as TSE, EMSE, and STVR.






