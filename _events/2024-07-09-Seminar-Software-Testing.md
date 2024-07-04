---
layout: event
title: "Seminar Software Testing"
categories: [events, talk]
start: "10:00"
end: "11:30"
speaker: Andreas Zeller, Xavier Devroey
where: Social Data Lab, Ground Floor VMB, TU Delft
---

The two travelling members of Caro's PhD committee, Andreas Zeller and Xavier Devroey, will give talks about their recent research.

Topics to be announced!


## Learning Program Behavioral Models from Synthesized Input-Output Pairs
**Andreas Zeller, CISPA Helmholtz Center for Information Security**

We introduce Modelizer – a novel framework that, given a black-box program, learns a model for its input/output behavior using neural machine translation. The resulting model mocks the original program: Given an input, the model predicts the output that would have been produced by the program. However, the model is also reversible – that is, the model can predict the input that would have produced a given output. Finally, the model is differentiable and can be efficiently restricted to predict only a certain aspect of the program behavior.
Modelizer uses grammars to synthesize inputs and to parse the resulting outputs, allowing it to learn sequence-to-sequence associations between token streams.
Other than input and output grammars, Modelizer only requires the ability to execute the program.
The resulting models are small, requiring less than 6.3 million parameters for languages such as Markdown or HTML; and they are accurate, achieving up to 95.4% accuracy and a BLEU score of 0.98 with standard error 0.04 in mocking real-world applications.
We foresee several applications of these models, especially as the output of the program can be any aspect of program behavior. Besides mocking and predicting program behavior, the model can also synthesize inputs that are likely to produce a particular behavior, such as failures or coverage.

*Joint work with Tural Mammadov, Dietrich Klakow, and Alexander Koller. Funded by the European Union (ERC, S3, 101093186). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. Neither the European Union nor the granting authority can be held responsible for them.*

Andreas Zeller is faculty at the [CISPA Helmholtz Center for Information Security](https://www.cispa.de) and professor for Software Engineering at [Saarland University](https://saarland-informatics-campus.de/en/). His [research](https://scholar.google.com/citations?user=-Qytr_YAAAAJ&hl=en&oi=ao) on automated debugging, mining software archives, specification mining, and security testing has proven [highly influential](https://andreas-zeller.info/assets/ZellerCV.pdf). Zeller is one of the few researchers to have received two [ERC Advanced Grants](https://erc.europa.eu/apply-grant/advanced-grant), most recently for his [S3 project](https://www.cispa.de/s3/). Zeller is an [ACM Fellow](https://awards.acm.org/fellows) and holds an [ACM SIGSOFT Outstanding Research Award](https://www.sigsoft.org/awards/outstandingResearchAward.html).


## From technical to socio-technical test case generation
**Xavier Devroey, University of Namur**

At its core, software engineering is a socio-technical activity that combines automated tools like continuous delivery with developer skills and team organization to sustain continuous software development and operation. Such activities are carried out in a DevOps loop, relying on highly automated tools and enabling the software to adapt to its moving expectations and infrastructures. However, despite software engineering’s growth over the past five decades, failures persist. The rapid development of new technologies and the profound transformation of software engineering processes over the last decade, bringing new challenges for industry and research, can partially explain those numbers. This talk advocates a holistic approach to software testing, considering a broad view of software development and operation practices as a source of information for objectives identification and test case generation. It places humans at the heart of concerns, reconciling social and technical aspects and making socio-technical testing the next step in achieving high reliability for modern software systems.

[Xavier Devroey](https://xdevroey.be/) is an assistant professor of software engineering at the [University of Namur](https://www.unamur.be), where, together with Benoît Vanderose, he co-leads the [SNAIL Team](https://snail.info.unamur.be). His research goal is to ease software testing by exploring new paths to achieve a high level of automation for test case design, generation, selection, and prioritization. His main research interests include search-based and model-based software testing, test suite augmentation, DevOps, and variability-intensive systems.
