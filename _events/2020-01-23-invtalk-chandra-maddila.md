---
layout: event
title: "Rex: Preventing Bugs and Misconfiguration in Large Services Using Correlated Change Analysis"
categories: [events, talks]
start: "13:00"
end: "14:00"
speaker: Chandra Maddila, Microsoft Research
where: TBD
---

## Abstract

Large services experience extremely frequent changes to code and configuration. In many cases, these changes are correlated across files. For example, an engineer introduces a new feature following which they also change a configuration file to enable the feature only on a small number of experimen- tal machines. This example captures only one of numerous types of correlations that emerge organically in large services. Unfortunately, in almost all such cases, no documentation or specification guides engineers on how to make correlated changes and they often miss making them. Such misses can be vastly disruptive to the service.

We have designed and deployed Rex, a tool that, using a combination of machine-learning and program analysis, learns change-rules that capture such correlations. When an engineer changes only a subset of files in a change-rule, Rex suggests additional changes to the engineer based on the change-rule. Rex has been deployed for 10 months on 260 repositories within Microsoft that hold code and configuration for services such as Office 365 and Azure. Rex has so far positively affected 3283 changes without which, at the very least, code-quality would have degraded and, in some cases, the service would have been severely disrupted.

**Note** This research will be presented at [NSDI 2020](https://www.usenix.org/conference/nsdi20/presentation/mehta)

## Bio

Chandra Maddila is a Senior Research Engineer in Applied Sciences group, Microsoft Research.

His interest areas are at the intersection of Machine Learning, Artificial Intelligence and Software engineering, which has resulted in [various publications](https://dblp.org/pers/hd/m/Maddila:Chandra_Shekhar), including at ICSE 2019, ESEC FSE 2019, the Usenix Annual Conference 2019, and OSDI 2018.

He has finished his masters in Software Systems from [BITS Pilani](https://bits-pilani.ac.in/), India.


