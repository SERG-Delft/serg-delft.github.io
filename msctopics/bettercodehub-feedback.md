---
layout: page
title: What's a good refactoring candidate? Improving code analysis tooling by studying users behavior
---

#### BetterCodeHub

The goal of BetterCodeHub (<https://bettercodehub.com/>) is to provide an environment that allows different types of users (students, CQSD trainees, developers, agile teams) to execute a maintainability inspection from start-to-finish. BetterCodeHub provides a low-threshold, self-service interface to users for delivering, scoping, analyzing and reporting on maintainability according to the SIG/TÜViT ISO 25010 maintainability model.
As for today, BetterCodeHub can count on more than 10,000 users.

#### Project description
One of the recently added features of BetterCodeHub is the ability to snooze an alert. More in detail, when one of the 10 guidelines is violated, BetterCodeHub shows an alert to the user with more information on the violation (_e.g._, what class or method does not comply to the guidelines, and why): with the new feature, a user can snooze the violation, hence indicating that s/he is not willing to solve the problem. 

The aim of the project is to understand in what circumstances the users decide to snooze a violation. The violations analyzed by BetterCodeHub have been deeply studied in the literature, and they are well-known proxies of defect-proneness [1][2][3][4]. However, as previously discussed, sometimes users "accept" the violation and decide not to solve it. The reasons behind this choice can be different: too complex to solve, do not have enough time, etc. Understanding these reasons can be useful for future tools makers, to better provide feedback to users on what is really important to them; furthermore, researchers can also gain from this result, understanding when and why code quality metrics are not useful to users, and how they can solve it.

#### What will the work environment look like for the student?
You will be embedded in the Research team of the Software Improvement Group, with close proximity other stakeholders of the topic. One of SIG's researchers will be appointed as your daily supervisor.
SIG has a lot of experience with hosting and supervising interns doing their Master thesis project. Each year between 5 and 10 interns do their projects with us. Last year the grade average of the Master projects was 8.5.
SIG is a dynamic and demanding working environment that rewards autonomy and curiosity.

#### Related work

[1] Stamelos, Ioannis and Angelis, Lefteris and Oikonomou, Apostolos and Bleris, Georgios L. Code quality analysis in open source software development. Information Systems Journal, 2002.

[2] Zhao, M., Wohlin, C., Ohlsson, N., & Xie, M. (1998). A comparison between software design and code metrics for the prediction of software fault content. Information and Software Technology. http://doi.org/10.1016/S0950-5849(98)00098-6

[3] Rosenberg, L., & Hyatt, L. (1997). Software quality metrics for object-oriented environments. Crosstalk Journal, April. http://doi.org/10.1117/12.732610

[4] Athanasiou, D., Nugroho, A., Visser, J., & Zaidman, A. (2014). Test code quality and its relation to issue handling performance. IEEE Transactions on Software Engineering. http://doi.org/10.1109/TSE.2014.2342227


#### Contact for the project:

* [Davide Spadini](mailto:d.spadini@tudelft.nl) (TU Delft/SIG)
* [Magiel Bruntink](mailto:m.bruntink@sig.eu) (SIG)
* [Alberto Bacchelli](mailto:bacchelli@ifi.uzh.ch) (UZH)
