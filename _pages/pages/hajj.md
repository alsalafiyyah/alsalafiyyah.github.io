---
layout: page
title: "Hajj (pilgrimage) and 'Umrah (lesser pilgrimage)"
author: "Instagram@Alsalafiyyah"
permalink: /hajj-umrah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.hajj-umrah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
