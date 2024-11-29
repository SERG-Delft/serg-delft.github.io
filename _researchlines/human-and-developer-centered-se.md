---
layout: research-line
title: "Human- and Developer-centered Software Engineering"
description: Considering the humans who will use our software and the developers who create it during software engineering processes.
responsible: "Carolin Brandt"
---
The research line of Human- and Developer-centered Software Engineering focuses on strengthening the consideration of the humans impacted by software engineering.
This covers both the developers who are developing software in collaborative environments, as well as the (future) users who will interact with the created software systems.
Lead by Carolin Brandt, we design, evaluate and realize different approaches to more closely consider the reality and needs of the people who will use our software during the software development process.

While we investigate the consideration of users in software development in general, a strong focus of our work are the development of automation tools for software engineers. As more and more powerful developer-supporting tools emerge, like IDE plugins, code and test generation tools, and generative AI, we call for an in-depth consideration on how these advancements impact the daily work of software developers.

## Research Topics:

- **Just-in-Time Test Generation**  
Current state‐of‐the‐art test generation approaches require the code under test to be already complete. On the other hand, developers are taught to create tests directly when they are writing their production code. To support this workflow, we aim to develop a tool that works in close proximity to the developer, proposing new tests whenever the developer completes a new functionality or component.  
Realizing just‐in‐time test generation requires us to first investigate several necessary components: How should we detect coherent, test‐worthy changes made by developers that can be the basis for the test generation process? How do we generate a test that executes and adequately checks the selected change in a short time on the developer’s machine? What is the right moment to contact the developer about our proposed test? And how do we design effective messages to convince the developer of the value of our tests?  
*Previous work:* [Short paper pitching the idea of JIT test generation](https://carolin-brandt.de/works/brandt-smileseng22)

- **Validation and Post-processing Tools for Generative AI**  
With the introduction of powerful generative AI tools, both computer scientists and the public have started to use generated code and text in their day‐to‐day work. This change in our work is not without risks. Moving from writing code to reviewing and editing proposals, comes at the danger of review fatigue, over‐reliance on code proposals, and repeating bad but common coding practices.  
We develop tools to support developers who are evaluating and editing code proposals from generative AI. Such a tools could, e.g., detect hallucinations of the AI, re‐prompt the AI to complete unfinished code proposals, or detect likely to be edited code based on previous edits of code proposals. Focusing on tests, tools could automatically measure and report the additional coverage provided by a proposed test, or evaluate the strength of the generated assertion and nudge the developer to add an oracle or evaluate the provided oracle.  
Potential research questions to investigae are: How can we effectively detect hallucinations in generated code and surface them to the developers for inspection? What parts of AI generated code are most likely edited by developers after accepting a suggestion? What immediate feedback on the quality of AI generated tests or code is helpful for developers? How can we make the following generation of software engineers more critical when using AI?  
*Previous work:* [GitHub Copilot for Test Generation in Python](https://carolin-brandt.de/works/elhaji-ast24)

- **Developer-oriented Code Coverage**  
We regularly teach that aiming for 80% code coverage during automated testing is sufficient. But which are the right 80% of code to cover?  
We are investigating more refined coverage metrics, that also take into account developers' expertise on which code is relevant to be covered by automated tests.  
*Previous work:* [Collaboration with Mozilla on relevant coverage gaps](https://carolin-brandt.de/works/brandt-icseseip24)

- **Human Work vs. (AI) Automation Trade-offs**  
With the rising popularity of generative AI, replacing human work with automatic tools has become a hot topic for companies, workers and students.  
However, automation attempts can also have adverse effects, such as declining quality of the produced work, unintended strengthening of biases or higher costs due to expensive correction or customization of the automation tools.  
We investigate the tradeoffs between leaving or delegating tasks to humans and developers and automating them with AI or other generation techniques.

- **User Requirements Engineering for Software Engineering Tools**  
A variety of software engineering research focuses on automating various tasks of software developers with the aim to alleviate effort and improve quality or productivtiy.  
We approach these automation tools with an interently developer-centric perspective:  
How should we design these tools to support developers in their real day-to-day work? How can we foster an effective collaboration between developers and automation tools that will actually lighten their load or help them develop better software? What needs of developers are under-considered in tool development nowadays?  
*Previous work:* [Test Amplification For and With Developers](https://carolin-brandt.de/works/brandt-phd-thesis), [Fixing CI tests from the IDE](https://carolin-brandt.de/works/boone-icpc22)

- **The Influence of Social and Human Needs on Software Engineering Practices**  
Developing software nowadays is a collaborative effort by diverse teams of software engineers and other professionals. While at the surface this work is centered around technical aspects, we conjecture that human and social factors have a central influence on decisions taken and the reality of software development practices.  
We are investigating and mapping these human and social factors, building theories on how they influence software engineers and projects.

- **Qualitative Methods in Software Engineering Research**  
To capture the diversity and variance of human experience, it is essential to employ qualitative research methods. At the same time, quantiative research methods are dominant in software engineering research because of a variety of factors. To empower qualitative methods and the researchers who use them, we investigate the current use of these methods and publish guidlines and tips on how to effectively study humans in software engineering.  
*Previous work:* [Strategies and Challenges in Recruiting Interview Participants for a Qualitative Evaluation](https://carolin-brandt.de/works/brandt-ropes22)

## Methods and Epistemological Stance:

In the research line of Human- and Developer-centered Software Engineering, we conduct empirical research projects through mixed-method approaches, with an emphasis on qualitative research.  
We take a pragmatist and constructivist epistemiological stance.  
This means that we focus on how we can pragmatically improve the reality of software developers and users in the near future.  
At the same time, we consider software engineering problems to be highly contextual, requiring us to acknowledge the diverse contexts of software projects out there when evaluating our approaches and inferring recommendations.

## How to Get Involved?

We are looking for students enthusiastic to research about considering humans more closely in software engineering. If you like the topic, feel free to contact [Carolin Brandt](https://carolin-brandt.de/).
