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
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
