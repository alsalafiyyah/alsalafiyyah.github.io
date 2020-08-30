---
layout: page
title: "Luqatah (a lost item found by someone else)"
author: "Instagram@Alsalafiyyah"
permalink: /luqatah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.luqatah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
