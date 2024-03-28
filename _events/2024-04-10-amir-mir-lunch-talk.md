---
layout: event
title: "On the Effectiveness of Machine Learning-based Call Graph Pruning: An Empirical Study"
categories: [events,lunch-talks]
start: "11:15"
end: "12:00"
speaker: Amir Mir
where: "Hybrid"
---

**Abstract**

In this SERG lunch talk, I will present our paper, "On the Effectiveness of Machine Learning-based Call Graph Pruning: An Empirical Study", which was recently accepted at the MSR'24 conference.

Static call graph (CG) construction often over-approximates call relations, leading to sound, but imprecise results. Recent research has explored machine learning (ML)-based CG pruning as a means to enhance precision by eliminating false edges. However, current methods suffer from a limited evaluation dataset, imbalanced training data, and reduced recall, which affects practical downstream analyses. Prior results were also not compared with advanced static CG construction techniques yet. This study tackles these issues. We introduce the NYXCorpus, a dataset of real-world Java programs with high test coverage and we collect traces from test executions and build a ground truth of dynamic CGs. We leverage these CGs to explore conservative pruning strategies during the training and inference of ML-based CG pruners. We conduct a comparative analysis of static CGs generated using zero control flow analysis (0-CFA) and those produced by a context-sensitive 1-CFA algorithm, evaluating both with and without pruning. We find that CG pruning is a difficult task for real-world Java projects and substantial improvements in the CG precision (+25%) meet reduced recall (-9%). However, our experiments show promising results: even when we favor recall over precision by using an F2 metric in our experiments, we can show that pruned CGs have comparable quality to a context-sensitive 1-CFA analysis while being computationally less demanding. Resulting CGs are much smaller (69%), and substantially faster (3.5x speed-up), with virtually unchanged results in our downstream analysis.