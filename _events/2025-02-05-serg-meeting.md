---
layout: event
title: "SERG Seminar"
categories: [events,lunch-talks]
start: "11:00"
end: "12:00"
speaker: Quentin Le Dilavrec, Carolin Brandt
where: "B28, Hilbert 2.W510"
---

In this edition of our weekly SERG seminar we will have two speakers:

**Quentin Le Dilavrec** will present his research tool enabling the efficient temporal analysis of software histories.
The corresponding tool paper will be presented at MSR 2025, in the continuation of the awarded approach presented at ASE 2022.
The HyperAST notably enables the incremental computation of code metrics, but defining metrics was error prone and required recompilation.
This contribution aims to facilitate the definition of code metrics and analyses on the HyperAST
by providing a sandboxed scripting interface focussing on usability and robustness. [HyperAST tool paper](https://perso.eleves.ens-rennes.fr/people/quentin.le-dilavrec/preprint/HyperAST_tool_paper.pdf)

Quentin will also make a short demo of this tool through its GUI, and show some other features, 
notably on temporal analysis (presented at BENEVOL 2024).

**Carolin Brandt** will introduce a novel way to look at code coverage in software testing. 
The corresponding short paper will be presented at ICST 2025.
[Towards Refined Code Coverage: A New Predictive Problem in Software Testing](https://carolin-brandt.de/works/brandt-icst25)

Abstract:

To measure and improve the strength of test suites, software projects and their developers commonly use code coverage and aim for a threshold of around 80%. 
But what is the 80% of the source code that should be covered? 
To prepare for the development of new, more refined code coverage criteria, we introduce a novel predictive problem in software testing: whether a code line is, or should be, covered by the test suite. 
In this short paper, we propose the collection of coverage information, source code metrics, and abstract syntax tree data and explore whether they are relevant to predict whether a code line is exercised by the test suite or not. 
We present a preliminary experiment using four machine learning (ML) algorithms and an open source Java project. 
We observe that ML classifiers can achieve high accuracy (up to 90%) on this novel predictive problem. 
We also apply an explainable method to better understand the characteristics of code lines that make them more “appealing” to be covered.
Our work opens a research line worth to investigate further, where the focus of the prediction is the code to be tested. 
Our innovative approach contrasts with most predictive problems in software testing, which aim to predict the test case failure probability.


---
If you are interested to give a 15 min + 10 talk or host a 25 min discussion session in one of our next meetings, please contact Carolin Brandt via Mattermost or email.
