---
layout: event
title: "PhD Defense: More Effective Test Case Generation with Multiple Tribes of AI"
categories: [events, talk]
start: "12:00"
end: "14:30"
speaker: Mitchell Olsthoorn
where: Senaatszaal, TU Delft
---

12:00 - Layman's talk
12:30 - Defense
~14:15 - Reception

**Summary**

Software testing is important to make sure that code works as intended.
Traditionally, this verification process has relied on manual testing, which is not only time-consuming but also susceptible to human errors.
Through the use of automated test case generation techniques, we can automate this process and reduce the time and effort needed to test software.
One of the promising techniques for automated test case generation is Search-Based Software Testing (SBST), which uses search-based metaheuristics to automatically generate test cases.
SBST has been shown to be effective in generating test cases for a variety of programming languages and levels of testing (e.g., unit, integration, and system testing).
However, SBST is not without its challenges.
One of the main challenges is the size of the search space that needs to be explored.

In this thesis, we explore the potential to improve the effectiveness and efficiency of automated test case generation by combining multiple tribes of Artificial Intelligence (AI) to narrow down the search space.
First, we introduce two novel approaches that incorporate domain-specific knowledge into the search process to reduce the search space for automated test case generation.
Then, we present two novel crossover operators.
One uses hierarchical clustering to identify and preserve promising patterns within test cases.
The other combines multiple crossover operators at different levels (i.e., structure and data) to increase the diversity within the population.
Next, we propose a model inference approach that infers dynamic types to allow automated test case generation of dynamically-typed languages.
Finally, we introduce a new testing framework for two languages (Solidity and JavaScript) where no existing tooling existed.

The results of this thesis show that both approaches for incorporating domain-specific knowledge into the search process are effective in reducing the search space for automated test case generation.
Thereby improving the effectiveness and efficiency of automated test case generation and increasing the structural coverage and fault detection capabilities of the generated test cases.
Furthermore, the first crossover operator managed to detect and preserve promising patterns within test cases, thereby maintaining the structure of the test cases throughout the search process.
The results of the second crossover operator show an increase in structural code coverage resulting from an improvement in the diversity of the population.
Moreover, our results show that the model inference approach improves structural code coverage, bringing automated test case generation for dynamically-typed languages one step further.
Finally, our new testing framework has demonstrated to be effective at generating test cases for Solidity and JavaScript.

In summary, this thesis introduced various novel approaches to improve the effectiveness and efficiency of automated test case generation by combining multiple tribes of AI to narrow down the search space.
The results show that these approaches improve upon the state-of-the-art and hopefully are a step towards increasing the adoption of automated test case generation techniques in industry.
