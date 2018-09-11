---
layout: page
title: Alternative API evolution communication mechanisms
---

#### Project description

In traditional APIs (not web based), API producers have two ways in which they can communicate with API consumers that the feature that they are using should no longer be used - deprecating the feature and documenting the change in the Javadoc/release notes. API producers prefer to deprecate features to let consumers know that a feature is obsolete, however, it is the only way in which Java allows API producers to throw compiler warnings to explicitly communicate with the consumers. This has led to API producers misusing the deprecation annotation[1,2], for example marking beta features as deprecated. Some APIs such as XWiki have found workarounds by introducing their own custom annotations, however, these do not throw compiler warnings or errors. This calls into question as to what other annotations are needed and whether they should throw compiler warnings or errors.

This project involves the following steps:

- Investigating all possible misuses of the deprecation annotation. This can be done by either manually investigating API deprecation cases or by interviewing and surveying API producers.

- Implementing new annotations based on API producer needs. These annotations could be part of a Java Specification Request (JSR) or could be implemented and detected using IDE plugins.

- Evaluating the impact and adoption of these new annotations, by creating real world PRs in projects that misuse deprecation and have them try using the new annotations.

#### Related work

[1] Sawant et al., "Understanding Developers’ Needs on Deprecation as a Language Feature", Proceedings of the 40th ACM/IEEE International Conference on Software Engineering (ICSE 2018), in press.

[2] Sawant et al., "Why are features deprecated? An investigation into the motivation behind deprecation", Proceedings of the International Conference on Software Maintenance and Evolution (ICSME 2018), in press.

#### Contacts for the project

* [Anand Ashok Sawant](mailto:A.A.Sawant@tudelft.nl) (TU Delft)
* [Arie van Deursen](mailto:Arie.vanDeursen@tudelft.nl) (TU Delft)
