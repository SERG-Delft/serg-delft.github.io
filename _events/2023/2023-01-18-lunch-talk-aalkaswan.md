---
layout: event
title: "Extending Source Code Pre-Trained Language Models to Summarise Decompiled Binaries"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Ali Al-Kaswan
where: Hybrid
---
In this talk I will present our paper titled "Extending Source Code Pre-Trained 
Language Models to Summarise Decompiled Binaries" which was just accepted to 
[SANER 2023](https://saner2023.must.edu.mo/accepted).

***Abstract***

Reverse engineering binaries is required to understand and analyse programs
for which the source code is unavailable. Decompilers can transform the 
largely unreadable binaries into a more readable source code-like representation. 
However, reverse engineering is time-consuming, much of which is taken up 
by labelling the functions with semantic information.

While the automated summarisation of decompiled code can help Reverse 
Engineers understand and analyse binaries, current work mainly focuses 
on summarising source code, and no suitable dataset exists for this task.

In this work, we extend large pre-trained language models of source code 
to summarise decompiled binary functions. Furthermore, we investigate the 
impact of input and data properties on the performance of such models. 
Our approach consists of two main components; the data and the model.

We first build CAPYBARA, a dataset of 214K decompiled function-documentation 
pairs across various compiler optimisations. We extend CAPYBARA further by 
generating synthetic datasets and deduplicating the data.

Next, we fine-tune the CodeT5 base model with CAPYBARA to create BinT5. 
BinT5 achieves the state-of-the-art BLEU-4 score of 60.83, 58.82, and 44.21 
for summarising source, decompiled, and synthetically stripped decompiled code, 
respectively. This indicates that these models can be extended to decompiled 
binaries successfully.

Finally, we found that the performance of BinT5 is not heavily dependent on 
the dataset size and compiler optimisation level. We recommend future research 
to further investigate transferring knowledge when working with less expressive 
input formats such as stripped binaries.