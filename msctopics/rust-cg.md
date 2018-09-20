---
layout: page
title: Sound call-graph generation for Rust
---

#### Background

Rust is a new systems programming language developed at Mozilla Research that
combines the speed and low-level hardware control of modern C++ with an
"ownership-based" type system guaranteeing memory safety and threads without
data races. This unique combination allows developers to build software that is
safe by construction. Since the first stable
[release](https://blog.rust-lang.org/2015/05/15/Rust-1.0.html) in 2015, Rust is
becoming increasingly
[popular](https://insights.stackoverflow.com/survey/2018/#most-loved-dreaded-and-wanted)
with a thriving community that has contributed with over 18,000 packages to its
package registry, [crates.io](https://crates.io).

#### Problem Statement

The Rust community lacks the support of a robust static analysis framework to
perform program analysis of Rust packages. In our work of building a call-based
dependency network for Rust, we had to resort to the generic LLVM call graph
generator to infer call graphs of Rust packages. The LLVM call graph algorithm
is only able to infer statically dispatched calls from Rust packages, missing
out on dynamically dispatched calls and other Rust specific details. While Rust
advocates static dispatch in general, dynamically dispatched functions from
implemented template structures are common and should be represented in a call
graph.

The objective of this project is to fill this gap by extending the current
generic LLVM call graph algorithm with techniques to infer a complete
Rust-specific call graph. This includes dealing with _dynamic dispatch_,
_generic function definitions_ and Rust-specific features such as _conditional
compilation_.

#### Related work

[1] https://phasar.org/

#### Contacts about the project:

* [Joseph Hejderup](mailto:j.i.hejderup@tudelft.nl) (TU Delft)
* [Georgios Gousios](mailto:g.gousios@tudelft.nl) (TU Delft)