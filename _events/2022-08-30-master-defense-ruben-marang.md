---
layout: event
title: "Master Thesis Defense on Guided Metamorphic Transformations for Testing the
Robustness of Trained Code2Vec Models"
categories: [events, defenses]
start: "14:00"
end: "16:00"
speaker: Ruben Marang
where: Lecture Hall F, EWI
---
***Abstract***
Machine learning models are increasingly being used within software engineering for their predictions. Research shows that these models' performance is increasing with new research. This thesis focuses on models for method name prediction, for which the goal is to have a model that can accurately predict method names. With this thesis, we could create a tool that can suggest method names to software developers, which would assist in improving the quality of the projects.
This research aims to get insight into the robustness vulnerabilities of a method name prediction model. We use a genetic search algorithm that looks for these robustness problems. The main question this thesis tries to answer is to what extent the performance metrics are affected by applying metamorphic transformations to the test set of a trained code2vec model. Besides this, this thesis also proposes an alternative metric called percentage\_MRR, which might better reflect the robustness of a model. The main idea behind this metric is that it penalizes the prediction certainty of a model instead of penalizing the prediction rank.
To answer this research question, a tool is created that runs a genetic algorithm applying these metamorphic transformations to a dataset that a trained model is then evaluating. With this tool, we conducted 22 genetic search experiments on primary metrics and combinations of metrics to see the trade-offs in the Pareto fronts.
The guided search of applying metamorphic transformations on the test set results in an average performance decrease of around $19\%$. This thesis also compares this drop in performance to the performance decrease a random search algorithm would create. Notably, for every transformer added, the average decrease in performance becomes smaller, and there are transformations, e.g., the if-false-else transformation, that have a bigger effect than others. This thesis concludes that the trained model is not robust against metamorphic transformations and has a significant performance drop.

***Info***

The presentation will be 25 minutes, after which the audience can ask 15 minutes of questions.
