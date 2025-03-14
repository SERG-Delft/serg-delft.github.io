---
title: Software Engineering Research Group at TU Delft
layout: page
carousels:
  - images:
    - image: /img/group_photos/serg-icse-lisbon-2024.jpg
      text: "ICSE 2024 in Lisbon"
    - image: /img/group_photos/faculty-retreat-spring2025.jpeg
      text: "Faculty Retreat Spring 2025"
    - image: /img/group_photos/serg-christmas-foto-2024.jpg
      text: "Christmas 2024"
    - image: /img/group_photos/groupretreat-fall-2023_fixed.jpeg
      text: "Retreat Fall 2023"
    - image: /img/group_photos/icse-2023.jpg
      text: "ICSE 2023"
    - image: /img/group_photos/serg-halloween-2021.jpg
      text: "Halloween 2021"
    - image: /img/group_photos/serg-retreat-antwerpen-2019.jpg
      text: "Retreat Fall 2019 Antwerpen"
    - image: /img/group_photos/serg-retreat-2019.jpg
      text: "Retreat Spring 2019"
description: The Software Engineering Research Group at TU Delft
---

<!-- <image src="img/serg-halloween-2021.jpg" style="float:center; max-width:100%; max-height:100%;"/>
<br/> -->

{% include carousel.html height="38" unit="%" duration="10" number="1" %}

# The Software Engineering Research Group

The mission of the TU Delft Software Engineering Research Group (SERG) is

1. to develop a deep understanding of how people build and evolve software systems;

2. to develop novel methods, techniques, theories, and tools that advance the way in which software is built and adjusted;

3. to ensure that our research results have a lasting impact in software development practice; and

4. to offer students an education that prepares them to take a leading role in complex software development projects.


## Research

The research of the TU Delft Software Engineering Research Group is
characterized by a focus on empirical research, conducted in close collaboration
with software development practice. Topics of interest include software testing,
software architecture, end user programming, software evolution, and
collaborative and distributed software development.

To accomplish our research goals, our research is organized across the following research lines:

<ul>
{% for line in site.researchlines %}
	<li><a href="{{ line.url }}">{{ line.title }}</a>: {{ line.description }}</li>
{% endfor %}
</ul>

We conduct our research in mixed teams, in collaboration with practitioners and
international researchers. We publish our research in the top venues in the
field. Members of SERG actively serve in organizational and program committees
of these conferences and editorial boards of these journals.

We are strong supporters of open science, and self-archive our publications in
the [TU Delft institutional repository](https://pure.tudelft.nl/portal/en/organisations/software-engineering(d40bac4b-3dd0-4427-aa5f-9331cae5d02e)/publications.html) and through 
our Technical Reports series. We aim at sharing our research prototypes as open
source tools whenever possible.

## Education

<image src="img/lecture.jpg" style="float:right; width:300px; border:1px solid #000" alt="A lecture by SERG"/>

We have a passion for teaching and a deep desire to share what we learn about software engineering
with our students. Our [teaching activities](teaching.html) include:

- Undergraduate courses in the TU Delft bachelor in computer science, covering such topics as object-oriented programming, various projects, software testing, big data processing, and software engineering.

- Advanced software engineering courses in the TU Delft master programs in computer science and embedded systems, covering such topics as software architecture, search-based software engineering, psychology of programming, and software analytics.

- Nine-month projects with our MSc students who advance our knowledge in software engineering by participating in our research projects -- often in collaboration with our industrial partners.

- Introductory courses in the TU Delft minor and digital skills programs, offering non-CS students a background in programming, data science, and software engineering;

- On line courses offered through the TU Delft EdX platform, on such topics as data analysis and Scratch programming, which have attracted tens of thousands of students from across the globe.

## Organization

SERG is one of the sections of the [Department of Software Technology][st] (ST).
Together with the [Intelligent Systems][INSY] department INSY, ST is responsible for research and education in computer science and engineering at [Delft University of Technology][tudelft].

SERG and the Department of Software Technology are part of the TU Delft [Faculty of Electrical Engineering, Mathematics, and Computer Science][eemcs].

[eemcs]: https://www.tudelft.nl/en/eemcs/
[st]: https://www.tudelft.nl/en/eemcs/the-faculty/departments/software-technology/
[tudelft]: https://www.tudelft.nl
[insy]: https://www.tudelft.nl/en/eemcs/the-faculty/departments/intelligent-systems/
