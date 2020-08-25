---
title: Funerals
layout: page
active: funerals
permalink: /funerals/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.funerals %}
    {% if post.url %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>