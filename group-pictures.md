---
layout: page
title: Group Pictures
description: Group Pictures of the Software Engineering Research Group
---

{% assign grouped = site.group_pictures | group_by: 'year' %}
<!-- after grouping, sort by years (now 'name' as it's the keys), reverse to put new photos first -->
{% assign group_sorted = grouped | sort: 'name' | reverse %} 
{% for item in group_sorted %}
   {% assign sorted = item['items'] | sort: 'month' | reverse %}
   {% if forloop.first %}
      {% assign sorted_pictures = sorted %}
   {% else %}
      {% assign sorted_pictures = sorted_pictures | concat: sorted %}
   {% endif %}
{% endfor %}

{% include group-picture-card-deck.html pictures=sorted_pictures %}
