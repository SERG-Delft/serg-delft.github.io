---
layout: page
title: A REPL loop for the CodeFeedr project
categories: [sal-msc-topics]
where: TU Delft
contact: Georgios Gousios
---

#### Project description

[Codefeedr](http://codefeedr.org) is a platform for streaming (software)
analytics. It is built upon Apache Flink, a stream processing platform.
Codefeedr allows users to build pipelines (DAGs) of stream processing steps, by
combining smaller steps and sharing data inputs and outputs.  Using those
pipelines, one can express stream processing queries, such as "find me the
developer that wrote the line that crashes for all stacktraces that show up more
than 5 times per second".

The pipeline abstraction, while useful requires the user to write the program in
Scala, compile it and deploy it on the Flink cluster. This is very inconvenient
when we just want to check a simple query. A better way to do such queries is an
SQL REPL loop. In such a scenario, the SQL REPL loop compiles a user-provided
query down to a CodeFeedr pipeline, deploys it and reads the results back to the
user console.

Several components required for building a Codefeedr REPL loop exist: SQL
parsing is handled by Apache Calcite; Codefeedr automatically exposes live data
types to a centralized location; a way to deploy a Codefeedr program on a Flink
cluster is part of Codefeedr.  The purpose is to combine those existing
components in a high-quality engineering project; the end result will be open
source and of high value to the stream processing community.

#### Contacts about the project:

* Georgios Gousios (TU Delft)

#### Related work

* [The Codefeedr repo](https://github.com/codefeedr)
* [The current CodeFeedr REPL](https://github.com/codefeedr/repl)
