---
title: Salafiyyah (Salafism)
layout: page
permalink: /salafiyyah/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.salafism %}
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
