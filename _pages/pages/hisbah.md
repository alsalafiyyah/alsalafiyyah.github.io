---
layout: page
title: "Hisbah"
author: "Instagram@Alsalafiyyah"
permalink: /hisbah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.hisbah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
