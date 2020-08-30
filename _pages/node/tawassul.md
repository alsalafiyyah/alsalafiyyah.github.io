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
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
