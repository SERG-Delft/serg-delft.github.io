---
layout: page
title: Layering Violations in the Linux Kernel
---

#### Project description
Potential violations of architectural layering can be detected when
changes in two separate layers are performed in a single commit;
a proper layering abstraction would not require such contemporary
changes.
As an example, commits to both a driver and the main kernel of Linux can
be detected with the
[following script](http://dx.doi.org/10.1145/3183440.3183469).

```sh
# Obtain ordered list of SHA hashes
area_commits()
{
  git log --pretty='%H' master -- $1 | sort
}
# Count common elements
comm -12 <(area_commits kernel) <(area_commits drivers) | wc -l
```

The study will examine potential violations to answer the following
research questions.

* Why does code change concurrently in two layers?
* What types of layering violations can be discerned?
* What architectural principles or design patterns can be employed to avoid these?

#### Related work

* Marcos César de Oliveira, Davi Freitas, Rodrigo Bonifácio, Gustavo Pinto, and David Lo, [Finding Needles in a Haystack: Leveraging Co-change Dependencies to RecommendRefactorings](https://mcesar.dev/papers/jss2019.pdf) *Journal of Systems and Software*, 2019.
* Diomidis Spinellis and Georgios Gousios. How to analyze Git repositories with command line tools: We're not in Kansas anymore. In *Companion: Proceedings of the 40th International Conference on Software Engineering, ICSE-C '18*, New York, NY, USA, May 2018. Association for Computing Machinery. Technical Briefing. [doi:10.1145/3183440.3183469](http://dx.doi.org/10.1145/3183440.3183469)

#### Contacts about the project

* [Diomidis Spinellis](mailto:D.Spinellis@tudelft.nl) (TU Delft)
