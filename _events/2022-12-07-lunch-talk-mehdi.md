---
layout: event
title: "SERG talk: On the Relation of Method Popularity to Breaking Changes in the Maven Ecosystem"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Mehdi Keshani
where: Hybrid
---

***Abstract***
Software reuse is a common practice in modern software engineering, helping
developers save time and energy while accelerating the process of delivering
software products. Dependency managers like Maven offer a large ecosystem of
reusable libraries that build the backbone of software reuse. Breaking changes,
however, are troublesome barriers to this library reuse, i.e., when an update to
a library introduces incompatible changes that break existing client programs.
Semantic Versioning has been proposed as a practice to make it easier for
users to find safe updates by encoding the change impact in the version
number. While this practice is widely studied from the framework perspective,
no detailed insights exist yet into the ecosystem perspective. In this work, we
inspect the commonness of the method-level semantic versioning violations that
occur within the Maven ecosystem. Then we study the popularity of methods
to understand the extent of the effects these violations have on the ecosystem.
We study violations of semantic versioning identified for the 2,766 versions of
384 target versioned packages in a release time frame of 6 months. We also
investigate the method-level effects of breaking changes on 7,190 dependent
versioned packages. We found that 28% of the artifacts introduce at least one
type of semantic versioning violation, either a breaking change or an illegal
API extension. To further understand the effects of breaking changes on the
ecosystem we study their impacts. After building call graphs for all dependents
that reference the target versioned package (directly or transitively), we found
that 87% of the publicly defined methods are never used by the dependents.
Moreover, among methods with at least one usage, a minority of 35% receive
half of all unique dependent calls to the respective library. We also find that the
method’s popularity does not seem to affect stability, as popular methods also
break frequently. Our results suggest that breaking changes might be a sign
of a lack of change-impact awareness on the ecosystem. Overall, we confirm
the previous result that Semantic Versioning is violated repeatedly in practice.
We believe that adequate information about popular framework methods could
improve update strategies and make developers reconsider if breaking changes
to widely used methods are indeed required.
