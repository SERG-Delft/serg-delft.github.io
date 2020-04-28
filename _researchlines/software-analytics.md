---
layout: research-line
title: Software Analytics
description: How can we harness the massive data modern development and deployment processes generate, as well as Big Code, to make better software engineering tools?
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

At the Software Analytics lab, we work to make software analytics a core asset for software development teams. Our research touches topics such as computer-supported collaborative work (CSCW), big data systems, software engineering processes, software reliability, software analysis, machine learning and data science.

Currently, we focus on the following 3 research lines, even though we are always open for new ideas:

* **Engineering for (software) analytics**: creating platforms for data ingestion, integration and querying in a streaming fashion. Related projects:

    * [AI4Fintech](https://se.ewi.tudelft.nl/ai4fintech/index.html) Making large software-based organizations more efficient.
    * [Codefeedr](http://codefeedr.org) A platform to ingest and process
      software analytics data in a streaming fashion
    * [GHTorrent](https://ghtorrent.org) Collects all data from the GitHub event API

* **Software ecosystems**: We build ecosystem wide, versioned call graphs out
of package networks to make studies such as precise security vulnerability
tracking, software license tracking, data-based API evolution etc possible.

   * [FASTEN](https://www.fasten-project.eu) A platform for analysing dependency 
    management services at the call graph level granularity

## Researchers

The following people are part of the Software Analytics lab:

* Georgios Gousios (Lab leader)
* Arie van Deursen (Mentor, Leader of the Software Engineering group)

* Ayushi Rastogi (Postdoc, part-time) working on theory building for distributed software development

* Joseph Hejderup (PhD student) working on ecosystem analysis/tics
* Maliheh Izadi (visiting from Sharif University of Techology), working on ML-based software summarization
* Elvan Kula (PhD student, also with ING), working on analytics for software process optimisation
* Mehdi Keshani (PhD student), working on scaling static analyses
* Chandra Maddila (PhD student, also with Microsoft), working on tools for software engineering
* Amir Mir (PhD student), working on making Python better through Machine Learning
* Xunhui Zhang (visiting from NUDT, China), working on analytics for distributed software development

## Collaborators

The lab collaborates with the following people / organizations:

* [Diomidis Spinellis](http://spinellis.gr) (AUEB / TU Delft)
* FaceBook Probable<T> group
* [Software Improvement Group](https://sig.eu)

## Student collaborators

SAL is always open to host briliant MSc/BSc students to work on the exiting
topics we offer. Currently, SAL has the priviledge to host the following
students:

* Wouter Zorgdrager (MSc student). Working on FASTEN, system administration

* Roberta Gismondi (BSc student). Working on ML-based autocompletion for Python
* Ilya Grishkov (BSc student). Working on FASTEN
* Evaldas Latoškinas (BSc student). Working on type prediction for Python
* Mihhail Sokolov (BSc student). Working on FASTEN

## Alumni

The following people were part of the Software Analytics lab:

* Moritz Beller (Postdoc, now at FaceBook)
* Maria Kechagia (Postodoc, now at UCL)
* Jos Kuijpers (BSc student, worked on Codefeedr)

## Funding

The Software Analytics Lab has received funding from:

* NWO
* European Commission
* Microsoft
* Facebook
* ING

## MSc thesis topics

The following list contains a list of indicative master thesis topics. Please contact [Georgios Gousios](mailto:g.gousios@tudelft.nl) for more up to date information.

| Published | Where |  Project Title     |  
|-----------|---------|--------------------|
{% for post in site.posts %}{% if post.categories contains "sal-msc-topics" %}
| {{ post.date | date: "%b-%Y" }} | {{ post.where }}  | <a href="{{ post.url }}">{{ post.title }}</a> |{% endif %}{% endfor %}

