---
layout: page
title: Past events at SERG
---

We organize research talks and paper reading clubs.
Below are the events we organized in the past -- see also our list of
<a href="events.html">upcoming events</a>.

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

| When | Event  | Speaker | 
|--|---|--|
{% for event in site.events reversed %}{% capture posttime %}{{event.date | date: '%s'}}{% endcapture %}{% if posttime <= nowunix %}| {{ event.date | date: "%d-%b-%Y" }} | <a href="{{ event.url }}">{{ event.title }}</a> | {{ event.speaker }} |
{% endif %}{% endfor %}