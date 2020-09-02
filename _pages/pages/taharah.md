---
layout: page
title: "Taharah (Purification)"
author: "Instagram@Alsalafiyyah"
permalink: /taharah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.taharah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
