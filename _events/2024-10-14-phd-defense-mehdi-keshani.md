---
layout: event
title: "PhD Defense: Enhancing the Security of Software Supply Chains: Methods and Practices"
categories: [events, talk]
start: "17:30"
end: "19:00"
speaker: Mehdi Keshani
where: Senaatszaal, TU Delft
---

**Summary**

Software supply chains include the development, management, and delivery of software products. Software ecosystems are essential components of these supply chains and facilitate software reuse and enhance the efficiency of software development. However, they also introduce unique challenges, such as dependency maintenance and security vulnerabilities. The Maven ecosystem is a popular software ecosystem within the Java realm and is used by millions of developers worldwide. This ecosystem faces issues that threaten its security and effectiveness. In this thesis, we aim to tackle these challenges by proposing novel methods and in-depth analyses of the ecosystem.
First, we propose an automated approach for library reproducibility to enhance library security during the deployment phase. We then develop a scalable call graph generation technique to support various use cases, such as method-level vulnerability analysis and change impact analysis, which help mitigate security challenges within the ecosystem. Utilizing the generated call graphs, we explore the impact of libraries on their users. Finally, through empirical research and mining techniques, we investigate the current state of the Maven ecosystem, identify harmful practices, and propose recommendations to address them.

In this thesis, we investigate the reproducibility of Maven artifacts from their source code and demonstrate that a significant portion of the Maven ecosystem could be made reproducible with automation. We then explore the scalability of method-level analysis in examining library interactions using call graphs, achieving significant performance improvements through a summarization-based call graph generation technique.
These enhancements make static analyses more practical. This technique allows us to assess the impact of libraries within Maven. We show a significant concentration of method usage among a small portion of public methods. We also discover that these popular methods experience breaking changes as frequently as methods not utilized by any users, indicating a lack of awareness among library maintainers about their library usage. Lastly, we identifychallenges in packaging practices that pose risks to ecosystem users. These challenges highlight the need for improved governance for the ecosystem and developer awareness
regarding the security and impact of libraries on users.
