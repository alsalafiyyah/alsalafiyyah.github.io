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
    <article>
      <header>
      <h4><a href="{{ post.url }}">{{ post.title }}</a></h4>
      </header>
    </article>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>