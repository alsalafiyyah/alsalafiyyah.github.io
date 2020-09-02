---
layout: page
title: "Shawm (Fasting)"
author: "Instagram@Alsalafiyyah"
permalink: /shawm/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.fasting %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
