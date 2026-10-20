---
layout: event
title: "PhD Defense: The Good, the Bad, and the Adversarial: Multi-Objective Testing for Deep Learning Systems"
categories: [events, talk]
start: "12:30"
end: "13:30"
speaker: Antony Bartlett
where: Senaatszaal, TU Delft
---

[Link to PhD Dissertation](TODO)

[Link to Watch Virtually](https://nmclive.tudelft.nl/mediasite/play/b54d196163be49b0ad4d430d1bfc7eaa1d){:target="_blank"}

Antony will defend his PhD thesis, including a short layman's talk.

On the committee are: Burcu Özkan (TU Delft), Gunel Jahangirova (King’s College London), Aitor Arrieta (Mondragon University), Hans Hellendoorn (TU Delft), Bart van Arem (TU Delft), Annibale Panichella (TU Delft), Cynthia Liem (TU Delft).

### Abstract

Artificial Intelligence (AI)-intensive systems, particularly Computer Vision (CV) models and Deep Reinforcement Learning (DRL) agents, are increasingly deployed in real-world safety-critical systems, such as autonomous vehicles and medical diagnosis. Their inclusion in these domains necessitates rigorous testing to ensure reliability and safety, particularly as we lack clear test oracles, face input fragility, must navigate vast and complex test spaces, and contend with dynamic and stochastic behaviors that defy traditional testing approaches.

In this thesis, we employ a purely black-box testing strategy to more accurately reflect real-world deployment scenarios, where model internals are inaccessible. We develop novel testing methodologies that combine proven search-based software testing (SBST) techniques with approaches harnessing surrogate models and Large Language Models (LLMs). We begin by presenting a pure differential evolution approach for generating minimal adversarial perturbations, extending it to multi-objective testing methods that enable trade-offs between attack effectiveness and imperceptibility to expose a broader range of input vulnerabilities. Building on this foundation, we introduce a multi-objective testing framework for Deep Reinforcement Learning that jointly optimizes for failure detection and test scenario diversity while leveraging lightweight surrogate models; ensuring that discovered faults span a broader spectrum of agent behaviors rather than exploiting only certain parts of a system. We then investigate the use of geometry-based image representations to guide test case selection in autonomous driving test suites, combining convolutional neural networks (CNNs) with optimization techniques for test case selection and prioritization. Finally, we investigate the use of LLMs to automatically resolve build errors in a reproducible testing framework, enabling the correct testing of AI-intensive systems without labor-intensive manual debugging.

The results of our experiments demonstrate that approaches that optimize for multiple objectives are more effective at discovering issues across a broader range of scenarios, while remaining computationally eﬀicient. More importantly, we demonstrate that surrogate models can effectively enhance SBST techniques by approximating the behavior of the original system under test. Surrogate models provide an eﬀicient fitness function based on their predictions to guide the search process, as surrogate models closely approximate model output without expensive evaluations on the original system. Finally, we demonstrate that LLMs can support the testing process by leveraging natural language processing to identify and resolve system build errors, thereby enabling reproducible system validation.

In summary, this thesis contributes novel hybrid search-based approaches for testing AI systems, addressing the challenges inherent to testing CV models and DRL agents. We demonstrate the effectiveness of combining surrogate models and LLMs with existing SBST methodologies, and highlight the critical importance of diversity in generating comprehensive test suites for robust AI systems.
