---
layout: page
title: Upcoming events at SERG
---

We organize research talks and paper reading clubs.
Feel free to join us!
You can also browse through our <a href="past-events.html">past events</a>,
or subscribe to our calendar: 
<a href="https://se.ewi.tudelft.nl/serg-events.ics">https://se.ewi.tudelft.nl/serg-events.ics</a>.

{% assign fut_events_seen = "no" %}

| When | Event       | Speaker | Where           |
|---------|-------|----------------------|------------------------|
{% for event in site.events -%}
  {%- if event.date > site.time -%}
    | {{ event.date | date: "%d-%b-%Y" }} {{ event.start }} - {{ event.end }} | <a href="{{ event.url }}">{{ event.title }}</a> | {{ event.speaker }} | {{ event.where }} |
    {% assign fut_events_seen = "yes" %}
  {% endif %}
{%- endfor %}
{%- if fut_events_seen == "no" -%}
  | | _No new events scheduled_ | | |
{% endif %}

