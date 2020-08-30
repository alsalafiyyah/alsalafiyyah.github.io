---
layout: page
title: "Non-Muslims"
author: "Instagram@Alsalafiyyah"
permalink: /non-muslims/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.non-muslims %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
