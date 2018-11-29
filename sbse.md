#### Introduction

The development, maintenance and testing of large software products involve many activities that are complex, expensive and error-prone. For example, complex systems (e.g., autonomous cars) are typically built as a composition of features that tend to interact and impact one another’s behavior in unknown ways. Therefore, detecting feature interaction failures with manual testing becomes infeasible and too expensive when the number and the complexity of the features increase.

Nowadays, researchers and large tech companies use **Artificial Intelligence** (AI) to automate expensive development activities, since more development automation would require less human resources. 
One of the most common ways to make such an automation is the **Search-Based Software Engineering** (SBSE), which reformulates traditional software engineering tasks as search (optimization) problems. Then, **AI algorithms** (e.g., genetic algorithms, genetic programming, simulated annealing) are used to automate the process of discovering (e.g., detecting software defects) and building optimal solutions (e.g., software fixes).

SBSE is not only an academic research area, but it is achieving significant uptake in many industrial sectors. For example, **Facebook** uses multi-objective solvers to automatically design system level test cases for mobile apps [[1]](https://link.springer.com/chapter/10.1007/978-3-319-99241-9_1);  Google uses multi-objective solvers for regression testing [[2]](http://sebase.cs.ucl.ac.uk/fileadmin/crest/sebasepaper/YooNH11_01.pdf). SSBSE techniques has been also applied in the automotive domain (**IEE S.A.** [[3]](https://pure.tudelft.nl/portal/files/45811366/paperASE18N2016pdf.pdf)), in satellite domain (**SES S.A.** [[4]](https://pure.tudelft.nl/admin/files/47344874/main.pdf)) and security testing.

Currently, our research topics include but are not limited to the following **five** research topics:

* **Test Case Generation**: 
Developing tools that automatically synthetize (generate) test cases with high code coverage (e.g., branch coverage) and that reveal faults or trigger crashes. Related projects include [Botsing](https://github.com/STAMP-project/botsing) for crash replication and [EvoSQL](https://github.com/SERG-Delft/evosql) for testing SQL queries. We also actively contribute to the [EvoSuite](https://github.com/EvoSuite/evosuite) framework for unit-level testing [[5]](https://apanichella.github.io/publication/ieee-tse2018b/), [[6]](https://apanichella.github.io/publication/ssbse2018b/), [[7]](https://apanichella.github.io/publication/infsof2018b/).

* **AI-based Penetration Testing**: 
Enterprise web systems use different protection layers (e.g., input sanitization, Web Application Firewalls) against malicious attacks (**code injection**). Since cyber-attacks are increasingly sophisticated, these protection layers become complex and difficult to maintain and test manually. We develop penetration testing tools that use **machine learning** (ML) techniques to identify and predict malicious string patterns that are more likely violating the security layers. For example, we use SBSE in combination with ML to test [[8]](http://orbilu.uni.lu/handle/10993/34224) and repair [[9]](https://apanichella.github.io/publication/issre2018/) vulnerable Web Application Firewalls (WAFs) and the input validation and sanitization procedures in front-end web applications [[10]](https://apanichella.github.io/publication/ieee-tse2018a/). This research line is carried out in collaboration with the SVV lab from the University of Luxembourg.

* **Testing Autonomous Cars**: 
Self-driving cars, and in general automotive systems, are feature-based systems where different units of functionalities (features) work together. To test these complex systems in an automated fashion, we use ML, and SSBSE to find test scenarios (simulation settings) that violate system requirements, hence leading to software failures [[11]](https://apanichella.github.io/publication/ase2018/).

* **Regression Testing**: 
Is your test suite too large for the retes-all approach? Do you want to minimize the cost of regression testing in your DevOps pipelines without losing its fault-detection capability? We use SSBSE techniques to find a minimal yet representative subset of test cases to execute after each commit. We also use SSBSE and ML to prioritize your test cases based on past test execution data [[12]](https://apanichella.github.io/publication/ieee-tse2018f/).

* **Mutation Testing**: 
We work to provide immediate feedback for developers about the quality (effectiveness) of the test suites. To this aim, we use mutation testing as a swiss army knife and ML to reduce the cost of mutation analysis [[13]](https://apanichella.github.io/publication/icst2018/).

#### Collaborators

The lab collaborates with the following people/organizations (reported in alphabetic order):
* SVV Lab - Interdisciplinary Centre for Security, Reliability and Trust, University of Luxemburg
* Andrea De Lucia, University of Salerno
* Fitsum Kifetew, Fondazione Bruno Kessler
* Dario Di Nucci, University of Bruxelles 
* Sebastiano Panichella, Zurich University of Applied Sciences
* Paolo Tonella, Universita' della Svizzera Italiana

#### Master Thesis and Projects
We are looking for excellent and well-motivated master students to work on SSBSE related topics. If you are interested in one of the research topic above, please send an email to Dr. [Annibale Panichella](https://apanichella.github.io). Besides, we are open to new research ideas.
