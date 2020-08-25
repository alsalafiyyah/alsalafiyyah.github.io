---
layout: default
title: Articles
active: muqolat
permalink: /muqolat/
---

<article class="post">
<header class="major">
 <span class="date">{{ page.title }}</span>
</header>
<ul class="posts">
  {% for post in site.categories.basic %}
    {% if post.url %}
    <li>
     <a href="{{ post.url }}"><b>{{ post.title }}</b></a>
     <p>{{ post.content | strip_html | truncatewords: 30 }}</p>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>