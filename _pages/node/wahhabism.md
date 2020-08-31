---
title: Wahhabism
layout: page
active: wahhabism
permalink: /wahhabism/
---

<article class="post">
<p><a class="button small" href="/biographies/muhammad-al-wahhab/">His Da'wah and biography</a></p>
<ul class="posts">
  {% for post in site.categories.wahhabism %}
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
