---
title: Madhabs (Schools of Jurisprudence)
layout: page
active: madhabs
permalink: /madhabs/
---

<article class="post">
<div class="box">
<ul class="posts">
  {% for post in site.categories.madhabs %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>
</article>