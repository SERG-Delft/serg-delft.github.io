---
layout: event
title: "SERG talk: Type4Py (ICSE'22 paper)"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Amir M. Mir
where: Hybrid
---

In this talk, I will be presenting our recent paper, Type4Py, which was accepted at the technical track of ICSE'22. The pre-print of the paper is available on [Arxiv
](https://arxiv.org/abs/2101.04470).

***Abstract***

Dynamic languages, such as Python and Javascript, trade static typing for developer flexibility and productivity. Lack of static typing can cause run-time exceptions and is a major factor for weak IDE support. To alleviate these issues, PEP 484 introduced optional type annotations for Python. As retrofitting types to existing codebases is error-prone and laborious, machine learning (ML)-based approaches have been proposed to enable automatic type inference based on existing, partially annotated codebases. However, previous ML-based approaches are trained and evaluated on human-provided type annotations, which might not always be sound, and hence this may limit the practicality for real-world usage. In this paper, we present Type4Py, a deep similarity learning-based hierarchical neural network model. It learns to discriminate between similar and dissimilar types in a high-dimensional space, which results in clusters of types. Likely types for arguments, variables, and return values can then be inferred through the nearest neighbor search. Unlike previous work, we trained and evaluated our model on a type-checked dataset and used mean reciprocal rank (MRR) to reflect the performance perceived by users. The obtained results show that Type4Py achieves an MRR of 77.1%, which is a substantial improvement of 8.1% and 16.7% over the state-of-the-art approaches Typilus and TypeWriter, respectively. Finally, to aid developers with retrofitting types, we released a Visual Studio Code extension, which uses Type4Py to provide ML-based type auto-completion for Python.