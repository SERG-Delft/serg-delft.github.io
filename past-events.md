---
layout: page
title: Past events at SERG
---

We organize research talks and paper reading clubs.
Below are the events we organized in the past -- see also our list of
<a href="events.html">upcoming events</a>.

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

<!-- 
	Since this table is large, we use HTML tables directly in order to be able to influence the styling.
-->

<table>
	<colgroup>
		<col width="10%"/>
		<col width="60%"/>
		<col width="30%"/>
	</colgroup>
	<thead>
		<tr class="header">
			<th>When</th>
			<th>Event</th>
			<th>Speaker</th>
		</tr>
	</thead>
	<tbody>
		{% for event in site.events reversed %}
			{% capture posttime %}{{event.date | date: '%s'}}{% endcapture %}
			{% if posttime <= nowunix %}
				<tr>
					<td markdown="span">{{ event.date | date: "%d-%b-%Y" }}</td>
					<td markdown="span">[{{ event.title }}]({{ event.url }})</td>
					<td markdown="span">{{ event.speaker }}</td>
				</tr>
			{% endif %}
		{% endfor %}
	</tbody>
</table>