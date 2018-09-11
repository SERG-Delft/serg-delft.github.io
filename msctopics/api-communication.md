---
layout: page
title: Alternative API evolution communication mechanisms
---

#### Project description

In traditional APIs (not web based), API producers have two ways in which they can communicate with API consumers that the feature that they are using should no longer be used - deprecating the feature and documenting the change in the Javadoc/release notes. API producers prefer to deprecate features to let consumers know that a feature is obsolete, however, it is the only way in which Java allows API producers to throw compiler warnings to explicitly communicate with the consumers. This has led to API producers misusing the deprecation annotation, for example marking beta features as deprecated. Some APIs such as XWiki have found workarounds by introducing their own custom annotations, however, these do not throw compiler warnings or errors. This calls into question as to what other annotations are needed and whether they should throw compiler warnings or errors.

#### Contacts about the project

* [Anand Ashok Sawant](mailto:A.A.Sawant@tudelft.nl) (TU Delft)
* [Arie van Deursen](mailto:Arie.vanDeursen@tudelft.nl) (TU Delft)
