---
layout: page
title: "Prophets and Messengers"
active: prophets
author: "Instagram@Alsalafiyyah"
permalink: /prophets/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.prophets %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>
