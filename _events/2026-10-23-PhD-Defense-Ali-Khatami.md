---
layout: event
title: "PhD Defense: Understanding Software Quality Assurance in Open-Source Communities: Awareness, Adoption, and Tool Utilization"
categories: [events, talk]
start: "12:30"
end: "13:30"
speaker: Ali Khatami
where: Senaatszaal, TU Delft
---

[Link to PhD Dissertation](TODO)

Ali will defend his PhD thesis, including a short layman's talk.

On the committee are:
Tom Mens (University of Mons)
Shane McIntosh (University of Waterloo)
Gregorio Robles (Universidad Rey Juan Carlos)
Diomidis Spinellis (TU Delft + Athens University of Economics and Business)
Matthijs Spaan (TU Delft)
Carolin Brandt (TU Delft)
Andy Zaidman (TU Delft)

### Abstract
Today’s software development ecosystem offers an unprecedented array of quality assurance mechanisms. Continuous integration platforms, automated testing frameworks,
automated static analysis tools, and code review systems are now readily available to
developers, particularly in open-source software projects hosted on platforms like GitHub.
Yet this abundance does not automatically translate into effective adoption. Instead, it
introduces a new challenge: the rapid expansion of Software Quality Assurance (SQA)
practices and tools has created a complex decision space where teams should determine
which practices to adopt, how to configure them effectively, how to integrate them into
development workflows, and how to design processes that are relevant for their specific
project context. This dissertation aims to construct a holistic understanding of software
quality assurance by bringing together different aspects of open-source SQA practices that
can inform future decision-making.
We begin by establishing an empirical understanding of how SQA practices are currently
employed in the OSS world. What emerges is: projects tend to adopt practices in isolation
rather than as components of a cohesive quality assurance system, and only the most
mature projects invest holistically across most dimensions. This raises a deeper question
about whether developers actually understand the mechanisms already present in their
projects. Our survey of open-source maintainers and contributors confirms this concern,
uncovering an awareness gap: while developers broadly know that practices such as CI and
testing are in place, their understanding becomes shallow when asked for specific details.
To address the awareness gap, we design and evaluate RepoInsights, a software
quality assurance analytics dashboard consolidating data from testing, code review, and
automated workflow activities. While participants value the overview, they express a need
for richer and fine-grained contextual information. This motivates a deeper investigation
into GitHub Actions (GHA), a platform deeply integrated into the GitHub ecosystem
and a promising source of such contextual depth. We investigate GitHub Actions
through two complementary lenses, which uncovers two additional gaps: workflow
configurations suffer from recurring quality issues that require active maintenance, and
configured workflows are not necessarily used in practice, as presence does not imply
adoption.
Taken together, our five studies contribute toward a deeper understanding of how
software quality assurance operates in open-source software development on GitHub. The
empirical foundations and theoretical contributions of this dissertation, including but not
limited to, the awareness gap, the configuration-usage gap, and the GHA workflow failure
response theory, build toward the kind of understanding needed to navigate the complex
SQA decision space in open-source software development.
