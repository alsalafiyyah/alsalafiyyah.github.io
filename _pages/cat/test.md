---
layout: page
title: "Women, hijab and adornment"
author: "Instagram@Alsalafiyyah"
permalink: /categories/test/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.women %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
