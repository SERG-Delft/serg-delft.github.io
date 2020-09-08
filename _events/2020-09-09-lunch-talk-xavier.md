---
layout: event
title: "SERG talk: Test them all, is it worth it? Testing variability-intensive software systems"
categories: [events, lunch-talks]
start: "14:00"
end: "15:00"
speaker: Xavier Devroey
where: Online
---

Many approaches for testing configurable software systems start from the same assumption: it is impossible to test all configurations. This motivated the definition of variability-aware abstractions and sampling techniques to cope with large configuration spaces. Yet, there is no theoretical barrier that prevents the exhaustive testing of all configurations by enumerating them if the effort required to do so remains acceptable. 
In this talk, I will introduce the different elements currently used to abstract and reason about software variability, and the most common sampling techniques applied to select representative configurations for testing. I will illustrate those elements on an industry-strength, open-source configurable software system: JHipster, a popular code generator for web applications. Additionally, I will answer the question *Test them all, is it worth it?*, based on our endeavor to test all the 26,000+ possible configurations of JHipster using a cluster of 80 machines for 4 nights for a total of 4,376 hours (182 days) CPU time. 

The complete report of the JHipster case study is available in our journal paper (to be presented in the journal first track of [SPLC 2020](http://splc2020.net)):
  * Halin, A., Nuttinck, A., Acher, M., Devroey, X., Perrouin, G. and Baudry, B. (2019). [Test them all, is it worth it? Assessing configuration sampling on the JHipster Web development stack](https://doi.org/10.1007/s10664-018-9635-4). In *Empirical Software Engineering* 24, 2 (Apr. 2019), pp. 674–717. ([open access](https://doi.org/10.1007/s10664-018-9635-4), [dataset](https://doi.org/10.5281/zenodo.3766691))
