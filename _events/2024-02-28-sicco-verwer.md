---
layout: event
title: "Learning state machine models from software logs and how to use them for anomaly detection"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: "Sicco Verwer"
where: "Hybrid"
---

**Abstract:**

I present the main class of algorithms for learning state machine models known as state merging. In my lab, we are actively developing a framework for learning different kinds of these machines from system logs such as host logs, network logs, or anything a developer believed worthwhile to log. Since software tends to be deterministic and sequential in nature, the behavior in such logs can often be succinctly captured by state machine models. Great benefits of learning state machines instead of the increasingly popular neural networks is that they can be learned efficiently, are accurate, interpretable, and can be used for further processing such as verification, or in my case anomaly detection. I have a spin-off where I apply models learned from Windows logs for intrusion detection and incident response. I will demonstrate both our learning framework called FlexFringe, and the application in incident response called APTAnomaly.

