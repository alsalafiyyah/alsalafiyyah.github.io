---
layout: no_sidebar
title: "Al-Fawaid (The Benefits)"
summary: ""
permalink: /fawaid/
---

{% for c in site.fawaid %}
  <h2>{{ c.title }}</h2>
  <p>{{ c.content }}</p>
{% endfor %}