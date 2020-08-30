---
title: Al-Buyu' (Sales) and Transactions
layout: page
permalink: /buyu/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.sales %}
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