---
layout: page
title: API documentation generation
---

#### Project description

APIs frequently evolve and deprecate older/obsolete features and replace these features with newer/modern features. This evolution can be particularly tricky to deal with for API consumers, thus resulting in most API consumers not even bothering to react to deprecation[1,2,3]. This can be dangerous behavior as recent research shows that APIs can deprecate a feature for reasons such as: security flaws in the existing feature or functional defects[4], for such reasons a reaction is vital. Another recent study has shown that API consumers definitely find the reason behind deprecation to be important before reacting[4].

Despite the importance given to the reason behind deprecation, API producers do not always mention it in the documentation. Furthermore, if an API consumer wants to track down the reason behind the deprecation, he would have to go through the API release notes, Javadoc, commit history and issue tracker[5]. We propose to lessen this burden on both API producers and consumers by automatically generating the documenation based on all the data available.

This project involves the following steps:

- Investigating all the available sources that might document the reason behind deprecation of a feature.

- Developing a Natural Language Processing (NLP) based technique to understand what text contributes to the rationale behind deprecation and extracting this from the text sources.

- Simultaneously, using other text classification techniques to see whether they perform better at understanding rationale than one of the NLP parsers.

- Based on the selected technique, create a tool that can automatically understand the rationale behind the deprecation of a feature and then augment the existing Javadoc with the same. This approach will be tested by creating real-world PRs and improving API documentation.

#### Related work

[1] Robbes, Lungu and Röthlisberger "How do developers react to API deprecation?: the case of a smalltalk ecosystem", Proceedings 
[2] Sawant, Robbes and Bacchelli, "On the reaction to deprecation of 25,357 clients of 4+ 1 popular Java APIs", Proceedings of 32nd IEEE International Conference on Software Maintenance and Evolution
[3] Sawant, Robbes and Bacchelli, "On the reaction to deprecation of clients of 4+ 1 popular Java APIs and the JDK", Empirical Software Engineering Issue 4 Volume 23 Pages 2158-2197
[4] Sawant, Aniche, van Deursen and Bacchelli, "Understanding Developers’ Needs on Deprecation as a Language Feature", Proceedings of the 40th ACM/IEEE International Conference on Software Engineering (ICSE 2018), in press.
[5] Sawant, Huang, Vilen, Stojkovski and Bacchelli, "Why are features deprecated? An investigation into the motivation behind deprecation", Proceedings of the International Conference on Software Maintenance and Evolution (ICSME 2018), in press.




#### Contact for the project:

* [Anand Ashok Sawant](mailto:A.A.Sawant@tudelft.nl) (TU Delft)
* [Alberto Bacchelli](mailto:bacchelli@ifi.uzh.ch) (UZH)
* [Arie van Deursen](mailto:Arie.vanDeursen@tudelft.nl) (TU Delft)
