---
layout: page
title: "Refutations"
active: refutals
author: "Instagram@Alsalafiyyah"
permalink: /refutals/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.refutals %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>
