---
layout: page
title: "Hajj (Pilgrimage) and 'Umrah"
author: "Instagram@Alsalafiyyah"
permalink: /hajj/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.hajj %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
