---
layout: page
title: "Salah (Prayers)"
active: salah
author: "Instagram@Alsalafiyyah"
permalink: /salah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.salah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
