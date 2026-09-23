---
layout: page
title: "Gems"
permalink: /gems/
---

{% for g in site.gems %}
  <article>
  <a href="{{ g.url }}">
    <h2>{{ g.title }}</h2>
    <p>{{ g.author }}</p>
    <p>{{ g.summary }}</p>
   </a>
  </article>
{% endfor %}
