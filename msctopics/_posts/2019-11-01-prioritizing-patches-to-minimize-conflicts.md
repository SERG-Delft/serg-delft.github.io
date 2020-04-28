---
layout: page
title: Prioritizing patches to minimize conflicts
categories: [sal-msc-topics]
where: TU Delft / JetBrains
contact: Georgios Gousios, Vladimir Kovalenko
---

#### Project description

Large software projects are collective work of hundreds of people.
One way to efficiently work on projects as a large team is the pull-based development model, native to GitHub, where contributors use dedicated branches to make their changes and later request their integration to the main codebase through *pull requests* that are reviewed and integrated into the main trunk by project maintainers. A similar, albeit more old-fashioned, way is to receive external contributions as *patches* that are later applied onto the current state of the codebase by maintainers.

One unpleasant side effect of highly parallel development process is *merge conflicts*, which happen when several conflicting changes happen concurrently over the same code. Each conflict has to be individually resolved, which takes time and poses a risk to introduce a bug in case of an incorrect merge.
Moreover, even if a direct merge conflict doesn't occur, there is still a risk of a *semantic conflict* between changes, e.g. when one of the patches introduces a change in an order of arguments in a function signature, and another one contains invocations assuming the old version.

The goal of this project is to develop an approach to sorting incoming pull requests in an order that minimizes potential conflicts, and integrate it into a real-world software engineering tool.

#### Contacts about the project:

* [Georgios Gousios](mailto:g.gousios@tudelft.nl) (TU Delft)
* [Vladimir Kovalenko](mailto:vladimir.kovalenko@jetbrains.com) (JetBrains N.V.)
