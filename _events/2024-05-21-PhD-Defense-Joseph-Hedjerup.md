---
layout: event
title: "PhD Defense: Fine-grained Analysis of Software Supply Chains"
categories: [events, talk]
start: "14:30"
end: "16:30"
speaker: Joseph Hejderup 
where: Senaatszaal, TU Delft
---

**Summary**

Developers strategically reuse code to expedite project development and lower maintenance costs. With the advent of software supply chains, integrating open-source libraries into projects has transitioned from a cumbersome, manual task to an automated, streamlined process. However, this ease of integration has downsides; adding just one library can typically bring in multiple others, each following different coding standards and maintenance protocols. This layer of complexity significantly impedes the effective monitoring and evaluation of security vulnerabilities and breaking changes stemming from these external libraries in software projects. To mitigate these challenges, developers use various tools to oversee and react to software supply chain activities. However, these tools frequently result in a high rate of false positives and are often not insightful, primarily because they rely on metadata from build manifests.

This thesis proposes call-based reachability analysis to enhance comprehension and precision by treating source code as first-class citizens in software supply chain analysis. Initially, we generate function call graphs for package releases, forming a call-based dependency network. We then compare such networks with manifest inferred networks to understand better their similarities and differences in approximating package relationships. The next phase of the thesis explores third-party library updates. Here, we examine the extent to which project test suites cover third-party functionality, followed by applying code-based reachability analysis to augment code areas lacking test coverage. Finally, we investigate the reuse of imported third-party library code in software projects, providing insights for developers and organizations to benchmark and question their reliance on imported third-party code over first-party code.

Our results demonstrate that reachability analysis based on build manifest inferred networks often tends to overestimate transitive package relationships compared to call-based networks, overlooking the specific usage patterns of third-party libraries in projects. Software projects typically utilize only a portion of the functionalities from a third-party library, a pattern that also extends to dependent third-party libraries. Tools relying on manifest-inferred data incorrectly infer that projects use all functionalities of imported third-party libraries. This results in false alarms when identifying software supply chain issues like security vulnerabilities. Similarly, tools that automate third-party library updates also assume that project test suites can detect regressions effectively. Project tests often fail to cover all functionalities from a third-party library, leading to approved updates where changes are unchecked. Finally, while most projects are aware of importing a large number of third-party libraries, we observe that the reuse of imported libraries remains relatively low, raising critical questions about how organizations should strategically balance third-party versus first-party code, especially in light of the risks inherent in software supply chains.

**Advisors:** Georgios Gousios, Arie van Deursen
