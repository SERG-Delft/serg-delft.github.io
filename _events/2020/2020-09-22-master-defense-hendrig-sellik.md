---
layout: event
title: "Master Thesis Defense on Using Deep Learning to Detect Off-by-One Errors in Java Source Code"
categories: [events, defenses]
start: "10:00"
end: "11:30"
speaker: Hendrig Sellik
where: Zoom
---

Mistakes in binary conditions are a source of error in many software systems. They happen when developers use < or > instead of <= or >=. These boundary mistakes are hard to find for developers and pose a manual labor-intensive work. While researches have been proposing solutions to identify errors in boundary conditions, the problem remains a challenge. Therefore it is necessary to research and develop new techniques to cope with such errors.

In this thesis, we proposed deep learning networks to learn mistakes in boundary conditions and later detect them in code never seen before. We trained our model on approximately 1.6M examples with faults in different boundary conditions. We achieved an accuracy of 85.06\%, a precision of 85.23\% and a recall of 84.82\% on a controlled dataset. Additionally, we performed tests on 41 real-world boundary condition bugs found from GitHub and tried to find bugs from the Java project of Adyen. However, the false-positive rate of the model remains an issue.
