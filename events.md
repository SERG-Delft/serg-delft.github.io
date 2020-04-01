---
layout: page
title: Events at SERG
---

We organize research talks and paper reading clubs. Feel free to join us.

Subscribe to our calendar: https://se.ewi.tudelft.nl/serg-events.ics

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}


| When | Event       | Speaker | Where           |
|---------|-------|----------------------|------------------------|
{% for event in site.events %}{% capture posttime %}{{event.date | date: '%s'}}{% endcapture %}{% if posttime >= nowunix %}| {{ event.date | date: "%d-%b-%Y" }} {{ event.start }} - {{ event.end }} | <a href="{{ event.url }}">{{ event.title }}</a> | {{ event.speaker }} | {{ event.where }} |
{% endif %}{% endfor %}

## Past events

| When | Event       | Speaker | Where           |
|---------|-------|----------------------|------------------------|
{% for event in site.events reversed %}{% capture posttime %}{{event.date | date: '%s'}}{% endcapture %}{% if posttime <= nowunix %}| {{ event.date | date: "%d-%b-%Y" }} {{ event.start }} - {{ event.end }} | <a href="{{ event.url }}">{{ event.title }}</a> | {{ event.speaker }} | {{ event.where }} |
{% endif %}{% endfor %}