---
layout: muqolat
title: Docs
active: muqolat
date: 2014-09-24 08:48:50 +0530
permalink: /docs/
---

<article>
  {% assign total = 0 %}
  {% for post in site.posts %}
     {% if post.category == "salafism" %}
      {% assign total = total | plus: 1 %}
     {% endif %}
  {% endfor %}
  
<ul>
{% for cat in site.categories %}
    <li>{{ cat[0] }} ({{ cat[1].size }})</li>
{% endfor %}
</ul>

<ol>
{% for post in site.posts %}
 {% if post.path contains 'salafism' %}
  <h3>{{ category[0] | capitalize }} <span> ({{ category[1].size }})</h3>
  <li><a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></li>
 {% endif %}
{% endfor %}  
</ol>

 <p>last modified: {{ site.time | date: "%b %-d, %Y at %r Saudi Arabia Time" }}</p>
 {{ site.time | to_utc | date: "%Y%m%dT%H:%M:%S%:z" }}
 <p>{{ site.time | gregorian.to_hijri | date: "%b %-d, %Y at %r %:z" }}</p>
 <p>{{ page.date | to_hijri | date: "%b %-d, %Y at %r" }}</p>
</article>
