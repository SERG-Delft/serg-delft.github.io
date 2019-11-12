---
layout: page
title: Master thesis projects
---

### Finding a Thesis Project

For students participating in the TU Delft computer science and embedded systems master's programs we have several openings for MSc projects.

All MSc projects are aligned with our research. They often are connected to one of our ongoing [research projects](research.html), but we also frequently use MSc projects to explore new research directions.
Projects can be conducted at:

- TU Delft in our own research labs, in close collaboration with our postdocs and PhD students
- Industry (as part of an internship), usually with companies (in The Netherlands or abroad) with which we have an ongoing research collaboration (e.g. ING, SIG, Adyen, ATOS, XWiki, Microsoft, Google, Facebook, Infotron, JetBrains, ...)
- Other (international) universities -- we have a rich network of academic friends around the world.

<a id="supervisors"></a>
### SERG Supervisors

You can make an appointment with one of the SERG group members to see what projects are currently open, or you can propose your own project, provided there is a clear connection with the research we conduct at our labs. You can contact the following persons for more information:

[theses-mauricio]: https://repository.tudelft.nl/islandora/search/contributor%3Aaniche?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22
[theses-felienne]: https://repository.tudelft.nl/islandora/search/contributor%3A%22hermans%2C%20f%22%20OR%20contributor%3Afelienne%20OR%20contributor%3A%22hermans%2C%20f.f.j%22?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22
[theses-georgios]: https://repository.tudelft.nl/islandora/search/contributor%3Agousios?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22
[theses-annibale]: https://repository.tudelft.nl/islandora/search/contributor%3Apanichella?collection=education
[theses-andy]: https://repository.tudelft.nl/islandora/search/contributor%3Azaidman?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22
[theses-arie]: https://repository.tudelft.nl/islandora/search/contributor%3Adeursen?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22
[theses-rini]: https://repository.tudelft.nl/islandora/search/contributor%3Asolingen?collection=education&f%5B0%5D=mods_genre_s%3A%22master%5C%20thesis%22

Supervisor | Topics | Examples
|---|---|---|
Maurício Aniche | Software maintenance, software refactoring, software testing | [Example theses][theses-mauricio]
Arie van Deursen | Human aspects, software architecture, software testing | [Example theses][theses-arie]
Georgios Gousios | Machine learning for software engineering, repository mining, software analytics | [Example theses][theses-georgios]
Annibale Panichella | Software testing, search-based software engineering, security testing | [Example theses][theses-annibale]
Rini van Solingen | Globally distributed software engineering, agile practices | [Example theses][theses-rini]
Andy Zaidman | Software testing, software evolution, repository mining | [Example theses][theses-andy]

<!-- Maybe add some student papers as well, e.g., ICSE 2018, ICSE SEIP, MSR, TSE, ... -->

<br/>
### Composing your Study Program

If you plan to conduct your MSc project at SERG, you will need to include at least two of the CS [MSc courses](teaching.html#msc) SERG teaches in your IEP (Individual Exam Program). We strongly recommend you to follow our software architecture and software analytics courses.
Besides our own software engineering related courses, when choosing the electives in your program you can consider including courses in such areas as machine learning, data science, compiler construction, distributed systems, or security.

Optionally, you can start your research with a 7-8 week literature survey (IN4306, 10EC). This assignment is concluded with a report containing an overview of the state-of-the-art in a particular branch of research.

<a id="open"></a>

### Open projects

| Published | Where |  Project Title       | SERG contact           |
|---------|-------|----------------------|------------------------|{% for post in site.posts %}{% if post.categories contains "msc-topics" %}
| {{ post.date | date: "%b-%Y" }} | {{ post.where }}  | <a href="{{ post.url }}">{{ post.title }}</a> | {{ post.contact }} |{% endif %}{% endfor %}


<br/>

### Proposing your Own Project

Under certain conditions it can also be possible to propose your own project.
In those cases it is important to 

- Study a number of [existing MSc theses](#supervisors).
- Identify an ongoing [research project](research.html) to which your proposal is connected.
- Study a number of currently [open msc project ideas](#open) and identify the ones that are closest to your idea.

In particular you need to carefully think about the research component of your proposal, and have a clear idea on why your proposal is novel -- it should advance the world's knowledge in software engineering.
If you wish to pursue this route it is advisable to select and contact a possible [supervisor](#supervisor) as early as possible.

### Writing your Thesis

Once you've found your project and your supervisor, we recommend that you start writing as soon as possible: Devise a table of content, and fill in details as you go.

To write your thesis you need to make use of our [MSc Thesis Template](https://github.com/SERG-Delft/thesis-template).
