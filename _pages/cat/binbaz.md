---
layout: blog_by_category
title: "Fatwas of Ibn Baz"
author: "Instagram@Alsalafiyyah"
permalink: /binbaz/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.binbaz %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
