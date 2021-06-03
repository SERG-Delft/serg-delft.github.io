---
layout: event
title: "SERG Lunch: Ecosystem-Scale Call Graph Construction"
categories: [events, lunch-talks]
start: "12:30"
end: "13:30"
speaker: Mehdi Keshani
where: Online
---

This presentation will be about the FASTEN project and ongoing research that builds the basis of FASTEN.

Slides are available [here](/slides/2020-04-01-lunch-talk-mehdi.pdf).

The main goal of the FASTEN project is to make package management more intelligent. Incidents like leftpad (A significant portion of the Internet has been broken by removing a package from a package manager) proved that the current way of managing packages has some flaws. FASTEN wants to mitigate such flaws by enriching package managers with method-level information. The idea behind FASTEN is to use call graph level information instead of package-level information. In order to provide call graph level information, we use call graph construction tools. However, the existing tools are designed for project-level use cases(e.g. in compilers, etc.) and do not work properly in the ecosystem-scale. In this presentation, I talk about FASTEN, how it works and how do we make call graph construction scalable.
