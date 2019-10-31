---
layout: page
title: Prioritizing patches to minimize conflicts
---

#### Project description
Large software projects are collective work of hundreds of people.
One way to efficiently work on projects as a large team is the pull-based development model, native to GitHub, where contributors use dedicated branches to make their changes and later propose changes to the codebase through *pull requests* that are reviewed and integrated into the main trunk by project maintainers. A similar albeit more old-fashioned way is to receive external contributions as *patches* that are later applied onto the current state of the codebase by the maintainers.

One unpleasant side effect of such highly parallel development process, where multiple people work on the same code, is merge conflicts, which happen when several conflicting changes happen concurrently over the same code. Each conflict has to be individually resolved, which takes time and poses a risk to introduce a bug in case of an incorrect merge.

The goal of this project is to develop an approach to sorting incoming pull requests in an order that minimizes potential conflicts, and integrate it into a real-world software engineering tool.


#### Contacts about the project:

* [Georgios Gousios](mailto:g.gousios@tudelft.nl) (TU Delft)
* [Vladimir Kovalenko](mailto:vladimir.kovalenko@jetbrains.com) (JetBrains N.V.)

