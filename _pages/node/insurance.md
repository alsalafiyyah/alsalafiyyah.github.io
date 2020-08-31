---
title: Insurance
layout: page
permalink: /insurance/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.insurance %}
    {% if post.url %}
    <li>
    <a class="icon fas fa-feather-alt" href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>