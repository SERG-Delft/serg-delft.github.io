---
layout: research-line
title: Software Analytics
description: How can we harness the massive data modern development and deployment processes generate, as well as Big Code, to increase development productivity and operational efficiency?
responsible: "Georgios Gousios"
---

## Introduction

Modern software projects are more than just the code that comprises them: teams
follow specific development processes; the code runs on servers or mobile phones
and produces runtime logs; users talk about the software in forums like
StackOverflow and GitHub and rate the product in app stores. The software is
part of a collection of similar applications and depends on external code or
service API’s to deliver its functionality. Modern software teams need data to
make informed decisions that enable continuous, feedback-driven improvement.

At the Software Analytics lab, we work to make software analytics a core asset for software development teams. Our research touches topics such as computer-supported collaborative work (CSCW), big data systems, software engineering processes, software reliability, software analysis, machine learning, and data science.

Currently, we focus on the following 3 research lines, even though we are always open to new ideas:

* **Engineering for (software) analytics**: creating platforms for data ingestion, integration and querying in a streaming fashion. Related projects:

    * [AI4Fintech](https://se.ewi.tudelft.nl/ai4fintech/index.html) Making large software-based organizations more efficient.
    * [Codefeedr](http://codefeedr.org) A platform to ingest and process
      software analytics data in a streaming fashion
    * [GHTorrent](https://ghtorrent.org) Collects all data from the GitHub event API

* **Software ecosystems**: We build ecosystem-wide, versioned call graphs out
of package networks to make studies such as precise security vulnerability
tracking, software license tracking, data-based API evolution, etc possible.

   * [FASTEN](https://www.fasten-project.eu) A platform for analyzing dependency
    management services at the call graph level granularity

## Researchers

<image src="../../img/sal-may-2020.jpg" style="float:center; max-width:100%; max-height:100%;"/>
<br/>

_(Some) Members of the Software Analytics Lab in May 2020. Left to right: Elvan Kula, Georgios Gousios, Maliheh Izadi, Mehdi Keshani, Amir Mir, Joseph Hejderup_

The following people are part of the Software Analytics lab:

* Georgios Gousios (Lab leader)
* Arie van Deursen (Mentor, Leader of the Software Engineering group)

* Ayushi Rastogi (Postdoc, part-time) working on theory building for distributed software development

* Joseph Hejderup (PhD student) working on ecosystem analysis/tics
* Maliheh Izadi (visiting from Sharif University of Technology), working on ML-based software summarization
* Elvan Kula (PhD student, also with ING), working on analytics for software process optimization
* Mehdi Keshani (PhD student), working on scaling static analyses
* Chandra Maddila (PhD student, also with Microsoft), working on tools for software engineering
* Amir Mir (PhD student), working on making Python better through Machine Learning
* Xunhui Zhang (visiting from NUDT, China), working on analytics for distributed software development

## Collaborators

The lab collaborates with the following people / organizations:

* [Diomidis Spinellis](http://spinellis.gr) (AUEB / TU Delft)
* FaceBook Probablity group
* [Software Improvement Group](https://sig.eu)

## Student collaborators

SAL is always open to hosting brilliant MSc/BSc students to work on the exiting
topics we offer. Currently, SAL has the privilege to host the following
students:

* Wouter Zorgdrager (MSc student). Working on FASTEN, system administration

* Roberta Gismondi (BSc student). Working on ML-based auto-completion for Python
* Ilya Grishkov (BSc student). Working on FASTEN
* Evaldas Latoškinas (BSc student). Working on type prediction for Python
* Mihhail Sokolov (BSc student). Working on FASTEN

## Alumni

The following people were part of the Software Analytics lab:

* Enrique Larios (Postdoc)
* Chushu Gao (visitor, now at SIG)
* Moritz Beller (Postdoc, now at Facebook)
* Maria Kechagia (Postdoc, now at UCL)

## Funding

The Software Analytics Lab has received funding from:

* NWO
* European Commission
* Microsoft
* Facebook
* ING

## MSc thesis topics

The following list contains a list of indicative master thesis topics. Please contact [Georgios Gousios](mailto:g.gousios@tudelft.nl) for more up to date information.

| Published | Where |  Project Title       | SERG contact           |
|---------|-------|----------------------|------------------------|{% for post in site.posts %}{% if post.categories contains "sal-msc-topics" %}
| {{ post.date | date: "%b-%Y" }} | {{ post.where }}  | <a href="{{ post.url }}">{{ post.title }}</a> | {{ post.contact }} |{% endif %}{% endfor %}
