---
layout: page
title: "Al-Wala' Wal-Bara' (loyalty and disassociation for Allah's Sake)"
active: walabara
author: "Instagram@Alsalafiyyah"
permalink: /walabara/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.walabara %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
