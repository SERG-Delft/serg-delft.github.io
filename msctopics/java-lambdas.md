---
layout: page
title: Improving Java's Lambda stream debugging 
---

#### Project description

When Java introduced lambdas and streams as a native feature in Java 8, it was expected that there would be widespread adoption of this feature. However, that has not really been the case[1]. One of the principal issues with lambdas in its current implementation is that when something goes wrong inside the stream, the stack trace message is very hard to understand and in many cases is considered to be quite useless[2]. This raises the question as to whether we can change the Java Runtime Environment error messaging when it comes to failures in Java streams.

This project involves the following steps:

- Phase one of this project will involve investigating the different ways in which languages with streams and lambdas actually expose run time errors.

- In phase two, an evaluation (in the form of a controlled user study) will be performed with actual Java developers to see what error message format they find desirable.

- Finally, in phase three, we will implement this in the Java Virtual Machine (JVM) and test its efficacy with real world users.

#### Related work
[1] Mazinanian, Davood, et al. "Understanding the use of lambda expressions in Java." Proceedings of the ACM on Programming Languages (OOPSLA 2017)

[2] https://blog.takipi.com/the-dark-side-of-lambda-expressions-in-java-8/
#### Contacts about the project

* [Anand Ashok Sawant](mailto:A.A.Sawant@tudelft.nl) (TU Delft)
* [Arie van Deursen](mailto:Arie.vanDeursen@tudelft.nl) (TU Delft)
