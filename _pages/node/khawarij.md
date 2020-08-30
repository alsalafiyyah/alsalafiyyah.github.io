---
title: Khawarij
layout: page
active: khawarij
permalink: /khawarij/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.khawarij %}
    {% if post.url %}
    <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>