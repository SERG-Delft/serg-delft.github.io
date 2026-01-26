---
layout: event
title: "PhD Defense: Modeling Effort Estimation and Planning in Large-Scale Agile Software Development"
categories: [events, talk]
start: "14:30"
end: "17:30"
speaker: Elvan Kula
where: Senaatszaal, TU Delft
---

[Link to PhD Dissertation](https://pure.tudelft.nl/ws/portalfiles/portal/241269450/thesis.pdf)
incl. Layman's talk

### Abstract

Late deliveries have been a common problem in the software industry for decades. They
often result from deficiencies in effort estimation and project planning. These deficiencies
arise due to the complexity of software development, where various social and technical
factors affect project effort and scheduling. Variability in human elements, such as team
dynamics and changing user requirements, adds further uncertainty. Since meeting time
and cost estimates is crucial for project success, improving effort estimation and planning
remains a key priority for software organizations. More accurate forecasting enables bet-
ter resource allocation, reduces delays, and enhances customer satisfaction.
Over the past two decades, software organizations have increasingly adopted agile
methods to improve flexibility and responsiveness. However, despite these advantages,
schedule delays remain common, with nearly half of agile projects experiencing overruns
of 25% or more. A key challenge lies in balancing the flexible, short-term planning of small
functionalities (user stories) with the structured, long-term planning required for larger
development units (epics). Current industry practices offer limited support for managing
these complexities, especially in large-scale agile settings.
This thesis presents a novel suite of expert- and data-based strategies to improve effort
estimation and planning in large-scale agile software development. We conduct a series
of case studies at ING, a large Dutch internationally operating bank, to collect and ana-
lyze data from hundreds of agile teams and projects. We identify key factors influencing
delays in epics and user stories and develop models to predict delays at both levels. At
the epic level, we compile our findings into a conceptual framework representing influen-
tial factors and their relationships to on-time delivery. Additionally, we explore dynamic
Bayesian methods to continuously update delay predictions throughout an epic’s devel-
opment life cycle. At the story level, we examine how team characteristics affect the
likelihood of delays. We also investigate how these factors, combined with incremental
learning methods, can improve story delay predictions. Finally, we develop a model that
optimizes sprint plans based on team goals and delivery performance.
Our research identifies 25 factors and their interactions that affect the on-time deliv-
ery of epics. The most influential factors are predominantly social in nature, such as task
dependencies, organizational alignment, and internal politics. These factors interact hi-
erarchically: organizational factors shape team behavior, which in turn affects technical
factors. To capture these complexities, we demonstrate that dynamic Bayesian methods,
using delay patterns as input, effectively update delay predictions as new information be-
comes available. At the story level, our findings suggest that planning in agile settings
can be significantly improved by integrating team-related information and incremental
learning methods into predictive models. Moreover, we find that user story prioritization
depends on a combination of factors that vary by project context. Our sprint plan opti-
mization model effectively addresses this variability and generates plans that deliver more
business value, align more closely with sprint goals, and mitigate delay risks better.
