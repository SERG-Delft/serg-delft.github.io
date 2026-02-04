---
layout: page
title: Vacancies
description: Open positions at the Software Engineering Research Group
---

The TU Delft Software Engineering Research Group has the following vacancies:

{% assign vacancies = site.vacancies | sort: "order" %}

{% for vacancy in vacancies %}
### [{{ vacancy.title }}]({{ vacancy.url }})

{% if vacancy.summary %}
{{ vacancy.summary | markdownify }}
{% endif %}

{% if vacancy.project %}
- **Project:** {{ vacancy.project }}
{% endif %}
{% if vacancy.position_type %}
- **Role:** {{ vacancy.position_type }}
{% endif %}
{% if vacancy.deadline %}
- **Deadline:** {{ vacancy.deadline }}
{% endif %}
{% if vacancy.contacts %}
- **Contact:** {% for contact in vacancy.contacts %}{% if forloop.first == false %}; {% endif %}{% if contact.url %}[{{ contact.name }}]({{ contact.url }}){% else %}{{ contact.name }}{% endif %}{% if contact.email %} ([{{ contact.email }}](mailto:{{ contact.email }})){% endif %}{% endfor %}
{% endif %}
{% if vacancy.apply_url %}
- **Apply:** [Application website]({{ vacancy.apply_url }})
{% endif %}

{% endfor %}
