---
layout: default
title: Articles
permalink: /muqolat
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.basic %}
    {% if post.url %}
    <li>
     <a href="{{ post.url }}">{{ post.title }}</a>
     <p>{{ post.content | strip_html | truncatewords: 30 }}</p>
    </li>
    {% endif %}
  {% endfor %}
</ul>
  <hr/>{% include social-share.liquid %}
</article>