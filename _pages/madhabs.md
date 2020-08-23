---
title: Madhabs (Schools of Jurisprudence)
layout: page
active: madhabs
permalink: /madhabs/
---

<article class="post">

<div class="box">
<h4>Hanabilah (Hanbalis)</h4>
<ul class="posts">
  {% for post in site.categories.hanbalis | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/sufism/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Shafi'iyyah (Shafi'is)</h4>
<ul class="posts">
  {% for post in site.categories.shafiis | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/shiah/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Hanafiyyah (Hanafis)</h4>
<ul class="posts">
  {% for post in site.categories.hanafis | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><i class="fas fa-arrow-right"></i> <a href="/khawarij/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Malikiyyah (Malikis)</h4>
<ul class="posts">
  {% for post in site.categories.malikis | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

</article>