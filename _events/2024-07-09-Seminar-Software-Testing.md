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
