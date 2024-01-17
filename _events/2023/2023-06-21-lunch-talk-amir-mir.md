---
layout: event
title: "Machine Learning-based Call Graph Pruning"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Amir M. Mir
where: Hybrid
---

**Abstract:**

Call graph construction plays a significant role in analyzing programs as it records function invocations, but achieving an ideal call graph - both sound and precise - is challenging, particularly with existing tools like WALA and Petablox. These tools have been found to create imprecise call graphs with a significant amount of false positives. Previous approaches for enhancing precision involved improving the context or flow-sensitivity of pointer analysis, the underlying mechanism of many call graph algorithms. However, this often leads to a costly trade-off between scalability and precision. To address these challenges, new machine learning (ML)-based approaches, such as CGPruner and AutoPruner, were developed. These methods prune false edges from call graphs as a post-processing step, improving precision. CGPruner uses a Random Forest classifier model, while AutoPruner leverages a code language model, CodeBERT, to extract semantic features from the source code of caller and callee functions. In this talk, I will describe the strengths and weaknesses of the prior work on ML-based call graph pruning, and then I will discuss possible improvements to these approaches.
