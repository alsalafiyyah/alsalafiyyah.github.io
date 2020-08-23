---
title: Shi'ah and the rafidah
layout: page
active: shiah
permalink: /shiah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.shiah %}
    {% if post.url %}
    <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>