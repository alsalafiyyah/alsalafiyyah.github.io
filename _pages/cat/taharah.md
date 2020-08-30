---
layout: page
title: "Taharah (Purification)"
author: "Instagram@Alsalafiyyah"
permalink: /taharah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.taharah %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>There are no <b>fatwas</b> for this category. <a href="/topic">Click here to try to use search engine instead</a> or go back to <a href="/">homepage</a>.</p>
  {% endfor %}
</ul>
</article>
