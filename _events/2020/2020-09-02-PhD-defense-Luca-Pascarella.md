---
layout: event
title: "PhD Defense: Augmented fine-grained defect prediction for code review"
categories: [events, talk]
start: "10:00"
end: "12:00"
speaker: Luca Pascarella
where: Senaatszaal, TU Delft
---

Summary

Code review is a widely used technique to support software quality. It is a manual activity, often subject to repetitive and tedious tasks that increase the mental load of reviewers and compromise their effectiveness. The developer-centered nature of code review can represent a bottleneck that does not scale in large systems with the consequence of com- promising firms’ profits. This challenge has led to an entire line of research on code review improvement.
In this thesis, we present our results and remarks on the effectiveness of using fine- grained defect prediction in code review while investigating what are the information needs that lead a proper code review. We started reimplementing the state of the art of defect prediction to understand its replicability; then, we evaluated this model in a more realistic scenario that is typically considered. To improve defect prediction techniques, we come up with a fine-grained just-in-time defect prediction model that anticipates the prediction at commit time and reduces the granularity at the file level. After that, we explored how to improve further prediction performance by using alternative sources of information. We conducted a comprehensive investigation of code comments written by both open and closed source developers. Finally, to understand how to improve code review further, we explored from a reviewers’ perspective what is the information that reviewers need to lead a proper code review.
Our findings show that the state of the art of defect prediction, when evaluated in a realistic scenario, cannot be directly used to support code review. Furthermore, we assessed that alternative sets of metrics, anticipated feedback, and fine-grained suggestions represent independent directions to improve prediction performance. Finally, we discovered that research must create intelligent tools that other than predict defects must satisfy actual reviewers’ needs, such as expert selection, splittable changes, realtime communication, and self summarization of changes.

Thesis: [link](https://www.lucapascarella.com/articles/thesis/luca-pascarella-phd-thesis.pdf)

**Advisors:** Alberto Bacchelli, Arie van Deursen
