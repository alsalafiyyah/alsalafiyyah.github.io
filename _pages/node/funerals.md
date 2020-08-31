---
title: Funerals
layout: page
active: funerals
permalink: /funerals/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.funerals %}
    {% if post.url %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>

<hr/>

<h4>Inheritance</h4>
<ul class="posts">
  {% for post in site.categories.inheritance %}
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