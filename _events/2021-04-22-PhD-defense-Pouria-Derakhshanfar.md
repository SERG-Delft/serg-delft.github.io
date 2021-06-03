---
layout: event
title: "PhD Defense: Carving Information Sources to Drive
Search-based Crash Reproduction and Test Case Generation"
categories: [events, talk]
start: "10:00"
end: "12:00"
speaker: Pouria Derakhshanfar
where: Senaatszaal, TU Delft
---

**Summary**

Software testing plays a crucial role in software development to improve the software’s consistency and performance. Since software testing activities demand considerable effort in the development process, many automated techniques have been introduced to aid de- velopers and testers in various testing phases, thereby reducing the costs related to these tasks. One category of these automated approaches seeks to generate software tests auto- matically using different strategies. One of the successful strategies, which is applied to industrial cases, uses metaheuristic search-based approaches for test generation automa- tion. These approaches use various search techniques to produce tests for different levels, such as unit testing and system-level tests. The assessments of these techniques confirm their usefulness in fault detection and debugging practices. However, most of these tech- niques use structural coverage criteria (e.g., line and branch coverage) for test generation. Despite the usefulness of these general criteria, it has been shown that they are not al- ways enough for revealing faults. Previous studies show that these criteria have a fault detection likelihood of about 50%.
This thesis investigates the application of novel search objectives and search-based test generation methods, based on information carved from multiple sources (e.g., source code, hand-written tests, etc.), on search-based test generation. In particular, in the first part of the thesis, we introduce new search objectives and methods to cover an instance of specific software behavior called crash reproduction. Then, we present a new search- based approach for testing integration points between two coupled classes to find class integration-level faults. Finally, we propose new search objectives to generate unit-level tests exercising the software common and uncommon execution patterns observed during the software operation.
Our results regarding the assessment of new search-based crash reproduction strate- gies show that these introduced techniques improve the search process’s effectiveness and efficiency. In other words, these techniques drove the state-of-the-art in search-based crash reproduction to reproduce more crashes and more quickly. Moreover, evaluating the novel search-based class-integration test generation approach indicates that this approach complements the state-of-the-art search-based unit test generation in fault detection. Fi- nally, this thesis reports mixed results for the search objectives introduced for exercising common and uncommon execution patterns. We observed that these objectives improve the mutation score achieved by the generated tests in some cases, while we see the oppo- site in some other cases.
In summary, this thesis introduced new techniques for search-based test generation by looking at the existing knowledge carved from different resources. The results reported in this thesis confirm these approaches’ positive impact on generating tests covering unde- tected bugs and faults with higher efficiency. This thesis is a step towards the development of fully-automated tools helping developers in software testing.

**Advisors:** Arie van Deursen, Annibale Panichella, Andy Zaidman
