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
    <i class="fas fa-feather-alt"></i> <a href="{{ post.url }}"> {{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>