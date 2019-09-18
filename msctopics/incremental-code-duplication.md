---
layout: page
title: Incremental code duplication detection
---

#### Project description

Duplication in source code is among the most harmful types of technical debt as it 
increases the size of the codebase and creates implicit dependencies between 
fragments of code. To remove such anti-patterns, the codebase should be refactored.

[SIG](https://www.softwareimprovementgroup.com), a Software Consultancy company located
in Amsterdam, utilizes its Software Analysis Toolkit to detect duplicates by performing 
textual comparison using static analysis of systems' code snapshots.
This approach, unfortunately, is less effective in scenarios where software teams 
use Continuous Integration / Continuous Delivery. In fact, the frequency of integrations 
witnessed in a typical CI/CD pipeline makes the SIG approach less optimal.

SIG envisions a new approach towards detecting code duplication by performing incremental 
code measurements. One such example could be analyzing commits performed on the VCS 
of the system and comparing such changes and the existing corpus of duplicates, 
to detect which code was effectively cloned. The idea is that the above-mentioned 
approach should be faster than comparing whole codebases of software systems, 
and therefore better suited to the ends of integration in scenarios of CI/CD.

Several peer-reviewed works have explored this same concept in the past. 
Most notably, there are several approaches that have investigated incremental clone detection, 
such as token-based clone detection, PDG-based, etc.

In this thesis proposal, the goal is to further explore the above-mentioned ideas,
with the target of producing an artifact that could effectively perform incremental
code clones detection based on textual similarities. Furthermore, we would like to assess 
and validate the practical implication of the project within the context of SIG.

#### Related work
[1] Gode, N. & Koschke, Rainer. (2009). Incremental Clone Detection. Proceedings of the European Conference on Software Maintenance and Reengineering, CSMR. 219 - 228. 10.1109/CSMR.2009.20. 

[2] Nguyen, T. T., Nguyen, H. A., Al-Kofahi, J. M., Pham, N. H., & Nguyen, T. N. (2009, September). Scalable and incremental clone detection for evolving software. In 2009 IEEE International Conference on Software Maintenance (pp. 491-494). IEEE.

[3] Roy, C. K., Zibran, M. F., & Koschke, R. (2014, February). The vision of software clone management: Past, present, and future (keynote paper). In 2014 Software Evolution Week-IEEE Conference on Software Maintenance, Reengineering, and Reverse Engineering (CSMR-WCRE) (pp. 18-33). IEEE.

#### Contacts about the project

* [Marco di Biase](mailto:m.dibiase@sig.eu) (TU Delft / SIG)
