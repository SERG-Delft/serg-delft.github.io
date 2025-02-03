---
layout: event
title: "PhD Defense: Machine Learning-assisted Software Analysis"
categories: [events, talk]
start: "15:00"
end: "17:30"
speaker: Amir Mir
where: Senaatszaal, TU Delft
---

[Link to PhD Dissertation](https://research.tudelft.nl/en/publications/machine-learning-assisted-software-analysis)

**Abstract**

Software engineering, fundamental to modern technological advancement,
profoundly influences various aspects of society by enhancing efficiency, accessibility,
and security. This discipline involves systematically applying engineering
principles to software systems' design, development, testing, and maintenance.
Innovations in software engineering have revolutionized industries such as communication,
finance, healthcare, and education, democratizing access to information and connecting
global communities. As software systems become increasingly complex, the need for
efficient, secure, and reliable software analysis tools becomes paramount.

The thesis focuses on improving the actionability and scalability of software
analysis by integrating machine learning (ML) techniques. Traditional static analysis
tools often struggle with large codebases, leading to high false positive rates and
high computational costs. Machine learning, particularly deep learning
architectures like Transformers, offers a promising solution by capturing long-range
dependencies in code and learning hierarchical representations. This capability enables ML
models to automate tasks such as bug detection, source code summarization, and
program repair, providing developers with actionable insights and improving overall
productivity and code quality.

A significant contribution of this thesis is the development of ML-based
techniques for type inference in Python and call graph pruning. An ML-based type
inference approach, namely Type4Py, was proposed, which accurately predicts type
annotations for Python code, enhancing code quality and reducing runtime errors. ML models
with conservative pruning strategies were proposed for call graph pruning, which
learns from dynamic traces obtained by executing programs to identify and eliminate
false edges, thereby minimizing false positives and improving precision.
Additionally, the thesis explores the application of call graphs in vulnerability analysis,
demonstrating that granular assessments provide more accurate and actionable insights than
more straightforward, dependency-level analyses.

In summary, this thesis advances the field of software analysis by harnessing
machine learning to address two important issues related to the actionability and
scalability of software analysis tools. The proposed ML-driven tools and techniques
enhance the precision and reliability of software analysis and support developers in
maintaining robust, secure, and maintainable software systems. These contributions pave
the way for future research in applying ML techniques to various aspects of
software engineering, promising further improvements in software development practices.
