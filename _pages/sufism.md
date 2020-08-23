---
title: Sufism
layout: page
active: sufism
permalink: /sufism/
---

<article class="post">
<h2>Sufism</h2>
<ul class="posts">
  {% for post in site.categories.sufism %}
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