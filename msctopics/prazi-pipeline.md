---
layout: page
title: Real-time analysis of dependency networks
---

## Background
At the Software Analytics Lab (SAL), we are developing techniques to construct
precise and fine-grained dependency networks of package repositories such as
[Maven](https://mvnrepository.com/), and
[crates.io](https://crates.io) using methods from program analysis. Typically,
we build dependency networks from dependency descriptors in package metadata
files such as `pom.xml`, `package.json` or `Cargo.toml`, yielding an imprecise
representation as it does not account for how and what portion of dependencies
in a single package are _actually_ being used in the source code.  Recently, we
have developed a systematic approach to creating _call-based dependency
networks_ (CDNs) by inferring the dependency use at the function call level of
packages. Such a representation makes it possible for the first time to perform
analysis such as precise security vulnerability tracking, software license
tracking and data-based API evolution studies on a dependency network.  Our
first evaluation of building a CDN for [crates.io](https://crates.io) has shown
promising results and we are now looking for interested master students to
explore new avenues with this work!

## Problem Statement
To make analyses of a CDN up-to-date and _actionable_, we need to process events
of package repositories in real-time. Many package repositories offer a live
feed tracking of changes made to their repository such as
[npm's](https://www.npmjs.com/) registry
[follower](https://github.com/npm/registry-follower-tutorial). The objective of
this project is to tap into such feeds and create a real-time pipeline of
fetching a new release, building a call graph and integrating it into a CDN.  While it may
sound trivial to add a new release to a CDN, aspects such as dependency
resolution of existing nodes need to be handled.

## Related work

[1] J. Hejderup, A. van Deursen, and G. Gousios, “Software Ecosystem Call Graph for
Dependency Management,” in Proceedings of the 40th International Conference on
Software Engineering: New Ideas and Emerging Results, New York, NY, USA, 2018,
pp. 101–104.
