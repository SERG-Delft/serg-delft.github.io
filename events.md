---
layout: page
title: Upcoming events at SERG
---

We organize research talks and paper reading clubs.
Feel free to join us!
You can also browse through our <a href="past-events.html">past events</a>,
or subscribe to our calendar: 
<a href="https://se.ewi.tudelft.nl/serg-events.ics">https://se.ewi.tudelft.nl/serg-events.ics</a>.

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}


| When | Event       | Speaker | Where           |
|---------|-------|----------------------|------------------------|
{% for event in site.events %}{% capture posttime %}{{event.date | date: '%s'}}{% endcapture %}{% if posttime >= nowunix %}| {{ event.date | date: "%d-%b-%Y" }} {{ event.start }} - {{ event.end }} | <a href="{{ event.url }}">{{ event.title }}</a> | {{ event.speaker }} | {{ event.where }} |
{% endif %}{% endfor %}

