---
title: Recommended
layout: page
active: basic
permalink: /basic/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.basic %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

<div class="box">
<h4>Al-Wala' wal-Bara'</h4>
<ul class="posts">
  {% for post in site.categories.walabara | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/walabara/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Funerals</h4>
<ul class="posts">
  {% for post in site.categories.funerals | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/funerals/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Wahhabism</h4>
<ul class="posts">
  {% for post in site.categories.wahhabism | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/wahhabism/">View all</a></p>
</ul>
</div>

</article>