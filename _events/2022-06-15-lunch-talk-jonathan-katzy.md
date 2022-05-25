---
layout: event
title: "SERG talk: Utilizing Lingual Structures to Enhance Transformer Performance in Source Code Completions"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Jonathan B. Katzy
where: Hybrid
---

In this talk, Jonathan will be presenting his master thesis on machine learning-based code completion.

***Abstract***
We explored the effect of augmenting a standard language model’s architecture (BERT) with a structural component base upon the ASTs of source code. We created a universal abstract syntax tree structure that can be applied to multiple languages to enable the model to work in the multilingual setting. We adapted a general graph transformer architecture to function as the structural component of the transformer. Furthermore we extended the ELMO style embeddings to work in a multilingual setting and when working with incomplete source-code. The final results showed that the multilingual setting was beneficial to finding higher quality embeddings and for the
baseline BERT model, however, monolingual models performed better in most cases for the transformer model. The best performing augmented transformer models outperformed the baseline BERT model by 1.5% in Java, 3.5% in Julia and 4.2% in CPP on the test set.