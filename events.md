---
layout: page
title: Events at SERG
---

We organize research talks and paper reading clubs. Feel free to join us.

Subscribe to our calendar: https://se.ewi.tudelft.nl/serg-events.ics

| When | Event       | Speaker | Where           |
|---------|-------|----------------------|------------------------|
{% for post in site.posts reversed %}{% if post.categories contains "events" %}| {{ post.date | date: "%d-%b-%Y" }} {{ post.start }} - {{ post.end }} | <a href="{{ post.url }}">{{ post.title }}</a> | {{ post.speaker }} | {{ post.where }} |
{% endif %}{% endfor %}
