---
layout: page
title: " Waqf (Endowment)"
author: "Instagram@Alsalafiyyah"
permalink: /waqf/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.waqf %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>There are no <b>fatwas</b> for this category. <a href="/topic">Click here to try to use search form instead</a>.</p>
  {% endfor %}
</ul>
</article>
