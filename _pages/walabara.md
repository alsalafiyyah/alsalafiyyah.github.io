---
layout: page
title: "Al-Wala' Wal-Bara'"
active: walabara
author: "Instagram@Alsalafiyyah"
permalink: /walabara/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.walabara %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>
