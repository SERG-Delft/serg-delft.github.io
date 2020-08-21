---
layout: event
title: "Master Thesis Defense on Expanding Search-Based Software Modularization to Enterprise-Level Projects: A Case Study at Adyen"
categories: [events, defenses]
start: "10:00"
end: "12:00"
speaker: Casper Schroder
where: Online (zoom/skype)
---

Quality of code structure often degrades while a codebase grows. Counteracting this process or remedying its effects by improving the structure takes lots of effort. Software Modularization is a research topic that has tried to reduce this effort, by developing approaches that can find change suggestions that improve the code structure from the perspective of certain metrics. This topic has been researched for around 25 years and many approaches have been introduced and applied. However, two factors are missing in this research. Modularization has been implied to be scalable, but it has not been applied on large-scale codebases. In addition, the quality of the results is only measured by the metric values for which the problem is optimized.

In this study we construct an approach from existing work which should scale to size, and apply it on the Adyen codebase (5.5M+ lines of code). To handle with the increased emphasis on transitive coupling in larger-scale codebases, we introduce a metric representing weighted transitive coupling, namely the Estimated Build Cost of module Cache Breaks. The suggested code changes resulting from this approach are validated by developers that have worked on that specific piece of code.

The results show that the approach produces similarly promising results from a metric point of view, supporting the assumption that this approach is scalable. However, the validation by developers shows that only 4 out of 13 examined suggestions result in an improvement in the codebase as is. Some changes required significant developer input to form an improvement and some reduced the structural quality of the codebase according to the developers. On the other hand, every examined suggestion showed the reviewing developer flaws in the code structure, and gave them an idea on how to fix it after only 10 minutes. These results imply that the quality of suggestions do not necessarily translate from a metric point of view to reality. Approaches should also be validated in reality to show their potential. They also imply that there is real world value in these solutions, which might be achieved in suggestions if the approaches are developed further with the focus of the real-world quality of the results.

