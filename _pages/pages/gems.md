---
layout: page
title: "Gems"
permalink: /gems/
---

{% for g in site.gems %}
  <article>
  <a href="{{ g.url }}">
    <h3>{{ g.title }}</h3>
    <p>{{ g.author }}</p>
    <p>{{ g.summary }}</p>
   </a>
  </article>
{% endfor %}
