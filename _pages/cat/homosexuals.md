---
layout: page
title: "Homosexuals and lesbianism"
author: "Instagram@Alsalafiyyah"
permalink: /homosexuals/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.homosexuals %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>There are no <b>fatwas</b> for this category. <a href="/topic">Click here to try to use search engine instead</a> or go back to <a href="/">homepage</a>.</p>
  {% endfor %}
</ul>
</article>
