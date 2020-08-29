---
layout: page
title: "Tawassul"
active: tawassul
author: "Instagram@Alsalafiyyah"
permalink: /tawassul/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.tawassul %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>
