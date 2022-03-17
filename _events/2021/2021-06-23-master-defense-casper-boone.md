---
layout: event
title: "Master Thesis Defense on TestAxis: Save Time Fixing Broken CI Builds Without Leaving Your IDE"
categories: [events, defenses]
start: "10:00"
end: "12:00"
speaker: Casper Boone
where: Online (YouTube + Zoom)
---
The most common reason for Continuous Integration (CI) build failures is failing tests. When a build fails, a developer often has to scroll through hundreds to thousands of log lines to find which test is failing and why. Finding the issue is a tedious process that relies on a developer's experience and increases the cost of software testing. Providing CI build test results with additional context in the developer's local development environment could help solve failing tests more quickly. We propose TestAxis, a test result inspection tool that brings CI test results to the Integrated Development Environment (IDE) offering an experience similar to running a test locally. Moreover, it surfaces additional information that is too expensive to collect in local development, for example, a unique view of the code under test that was changed leading up to the build failure. We implement TestAxis as a plugin for IntelliJ and conduct a user study to evaluate its usefulness and performance benefits. The participants solve programming assignments evaluating the three main features: the test results overview, the test code editor, and the changed code under test display. We show that TestAxis helps developers fix failing tests 13.4% to 30.4% faster. The participants found the features of TestAxis useful and would incorporate it in their development workflow to save time. With TestAxis we set an important step towards removing the need to manually inspect build logs and bringing CI build results to the IDE, ultimately saving developers time.
