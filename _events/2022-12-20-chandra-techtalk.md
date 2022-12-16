---
layout: event
title: "SERG talk: Recommenders for DevOps"
categories: [events, lunch-talks]
start: "11:00"
end: "12:00"
speaker: Chandra Maddila (Meta)
where: Zoom & Social Data Lab
---

Chandra Maddila is presently a senior engineer at Meta. Previously he was Microsoft Research.

In this techtalk, Chandra Maddilla will present two results from his work at Microsoft Research, that he presented last month at ESEC/FSE in Singapore:

- ConE: A Concurrent Edit Detection Tool for Large Scale Software Development ([link](https://2022.esec-fse.org/details/fse-2022-journal-first/21/ConE-A-Concurrent-Edit-Detection-Tool-for-Large-Scale-Software-Development))

- “Nalanda: A Socio-technical Graph Platform for Building Software Analytics Tools at Enterprise Scale”. ([link](https://2022.esec-fse.org/details/fse-2022-industry/11/Nalanda-A-Socio-technical-Graph-Platform-for-Building-Software-Analytics-Tools-at-En))

**ConE: A Concurrent Edit Detection Tool for Large Scale Software Development**

Modern, complex software systems are being continuously extended and adjusted. The developers responsible for this may come from different teams or organizations, and may be distributed over the world. This may make it difficult to keep track of what other developers are doing, which may result in multiple developers concurrently editing the same code areas. This, in turn, may lead to hard-to-merge changes or even merge conflicts, logical bugs that are difficult to detect, duplication of work, and wasted developer productivity. To address this, we explore the extent of this problem in the pull request based software development model. We study half a year of changes made to six large repositories in Microsoft in which at least 1,000 pull requests are created each month. We find that files concurrently edited in different pull requests are more likely to introduce bugs. Motivated by these findings, we design, implement, and deploy a service named ConE (Concurrent Edit Detector) that proactively detects pull requests containing concurrent edits, to help mitigate the problems caused by them. ConE has been designed to scale, and to minimize false alarms while still flagging relevant concurrently edited files. Key concepts of ConE include the detection of the Extent of Overlap between pull requests, and the identification of Rarely Concurrently Edited Files. To evaluate ConE, we report on its operational deployment on 234 repositories inside Microsoft. ConE assessed 26,000 pull requests and made 775 recommendations about conflicting changes, which were rated as useful in over 70% (554) of the cases. From interviews with 48 users we learned that they believed ConE would save time in conflict resolution and avoiding duplicate work, and that over 90% intend to keep using the service on a daily basis.

**Nalanda: A Socio-technical Graph Platform for Building Software Analytics Tools at Enterprise Scale**

Software development is information-dense knowledge work that requires collaboration with other developers and awareness of artifacts such as work items, pull requests, and file changes. With the speed of development increasing, information overload and information discovery are challenges for people developing and maintaining these systems. Finding information about similar code changes and experts is difficult for software engineers, especially when they work in large software systems or have just recently joined a project. In this paper, we build a large scale data platform named Nalanda platform to address the challenges of information overload and discovery. Nalanda contains two subsystems: (1) a large scale socio-technical graph system, named Nalanda graph system, and (2) a large scale index system, named Nalanda index system that aims at satisfying the information needs of software developers. To show the versatility of the Nalanda platform, we built two applications: (1) a software analytics application with a news feed named MyNalanda that has Daily Active Users (DAU) of 290 and Monthly Active Users (MAU) of 590, and (2) a recommendation system for related work items and pull requests that accomplished similar tasks (artifact recommendation) and a recommendation system for subject matter experts (expert recommendation), augmented by the Nalanda socio-technical graph. Initial studies of the two applications found that developers and engineering managers are favorable toward continued use of the news feed application for information discovery. The studies also found that developers agreed that a system like Nalanda artifact and expert recommendation application could reduce the time spent and the number of places needed to visit to find information.