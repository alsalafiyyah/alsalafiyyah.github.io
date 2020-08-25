---
title: Recommended
layout: page
active: basic
permalink: /basic/
---

<article class="post">
<div class="box">
<ul class="posts">
  {% for post in site.categories.basic | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a href="/general/">View all <i class="fas fa-arrow-right"></i> </a></p>
</ul>
</div>

<div class="box">
<h4>Al-Wala' wal-Bara' (loyalty and disassociation for Allah’s Sake)</h4>
<ul class="posts">
  {% for post in site.categories.walabara | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a href="/walabara/">View all <i class="fas fa-arrow-right"></i> </a></p>
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
  <p><a href="/funerals/">View all <i class="fas fa-arrow-right"></i></a></p>
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
  <p><a href="/wahhabism/">View all <i class="fas fa-arrow-right"></i></a></p>
</ul>
</div>

<div class="box">
<h4>Qur'an Tafsir (Exegesis)</h4>
<ul class="posts">
  {% for post in site.categories.quran | limit:5 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<ul class="posts">
    <li><a href="/sects/">The sects</a></li>
</ul>
</div>

</article>