---
layout: event
title: "Master Thesis Defense on Utilizing Lingual Structures to Enhance Transformer Performance in Source Code Completions"
categories: [events, defenses]
start: "13:30"
end: "15:30"
speaker: Jonathan Katzy
where: Room Hilbert, 2nd floor, CS building 
---

***Abstract***
We explored the effect of augmenting a standard language model’s architecture (BERT) with a structural component based on the Abstract Syntax Trees (ASTs) of the source code. We created a universal abstract syntax tree structure that can be applied to multiple languages to enable the model to work in a multilingual setting. We adapted the general graph transformer architecture  to function as the structural component of the transformer. Furthermore, we extended the Embeddings from Language Models (ELMo) style embeddings to work in a multilingual setting when working with incomplete source code. The final results showed that the multilingual setting was beneficial to achieving higher quality embeddings for the embedding model, however, monolingual models performed better in most cases for the transformer model. The addition of ASTs resulted in increased performance in the best performing models on all languages, while also reducing the need for a pretraining task to achieve the best performance. The largest increase in performance for a Java model compared to its baseline counterpart was 3.0% on average on the test set, the largest increase in performance for a Julia model compared to its baseline counterpart was 1.1% on average on the test set, and the largest increase in performance of a CPP model compared to its baseline counterpart was 5.7% on average on the test set.