---
title: Al-Buyu' (Sales) - Transactions - Riba (Usury) - Loan
layout: page
permalink: /al-buyu/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.al-buyu %}
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
