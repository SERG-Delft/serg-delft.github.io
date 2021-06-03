---
layout: event
title: "Master Thesis Defense on Language-agnostic Incremental Code Clone Detection"
categories: [events, defenses]
start: "10:00"
end: "12:00"
speaker: Stavrangelos Gamvrinos
where: Zoom
---

Code duplication is a form of technical debt frequently observed in software systems. Its existence negatively affects the maintainability of a system in numerous ways. In order to tackle the issues that come with it, various automated clone detection techniques have been proposed throughout the years. However, the vast majority of them operate using the entire codebase as input, resulting in redundant calculations and undesirable delays when this process is repeated for every new revision of a project. On the other hand, newer incremental techniques address this by storing intermediate information that can be reused across revisions. However, all these approaches are language-specific, utilizing language parsers to generate more sophisticated source code representations, in an attempt to detect more complex types of clones. As a result, less popular languages, for which finding or building a parser is challenging, are unfortunately not supported. 

In this study we propose LIICD, a language-agnostic incremental clone detector, capable of detecting exact-match clones. We assess its performance and compare it with a state-of-the-art commercial-grade detector, found within the Software Improvement Group (SIG). Furthermore, we use a similarity estimation technique called Locality Sensitive Hashing (LSH) in an attempt to extend and improve the original approach. Our experiments result in some interesting findings. Firstly, the proposed incremental detector is very efficient and able to scale well for larger codebases. Additionally, it provides a significant improvement compared to a non-incremental commercial-grade detector. Lastly, our LSH-based extension proves to have difficulties matching our original approach's performance. However, future suggestions indicate how the potential of the technique can be further investigated.
