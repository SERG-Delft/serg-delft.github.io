---
layout: event
title: "Investigating dependency code reuse using callgraphs"
categories: [events, defenses]
start: "9:00"
end: "11:00"
speaker: Algirdas Jokubauskas
where: Online (Zoom)
---

Software development is more and more reliant on external code. This external code is developed, bundled into packages and shared using package repositories like crates.io or npm. Reusing shared code bundles greatly improves development speed but without proper care and knowledge of included external code it can cause issues as well. Over-reliance on simple trivial packages that can be easily implemented locally can cause severe consequences like not being able to build if the package is no longer available. Furthermore, including large packages when only a small amount of it is being used can cause software projects become bloated with unnecessary code. This thesis proposes several metrics: leanness index, software composition index and utilization index that quantify how software projects reuse their dependencies or how much of the dependencies are utilized by their dependents. All three of the metrics are based on full function callgraph of the applications. Computation of these metrics was implemented for Rust and applied on every package in Rust package repository crates.io. General findings showed that dependency leanness was rather low: 21.7% of all packages in crates.io used less than 5% of their included dependencies while 95% of all crates used less than 62.4%. Another discovery revealed that packages in crates.io tend to consist mostly of code from external dependencies as opposed to local code: on average 91% of lines of code come from external dependencies. Lastly, using utilization index functions that were never used by any other crate in crates.io were identified: in 95% of packages, 71% of their callgraphs are never used.