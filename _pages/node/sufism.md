---
title: Sufism
layout: page
active: sufism
permalink: /sufism/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.sufism %}
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
