---
layout: page
title: "Al-Wala' Wal-Bara'"
active: walabara
author: "Instagram@Alsalafiyyah"
permalink: /walabara/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.walabara | limit:5 %}
    {% if post.url %}
    <li>
    <article>
      <header>
      <h4><a href="{{ post.url }}">{{ post.title }}</a></h4>
      </header>
    </article>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>