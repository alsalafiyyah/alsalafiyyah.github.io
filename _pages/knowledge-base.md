---
title: Recommended
layout: page
active: basic
permalink: /basic/
---

<article class="post">

<div class="box">
<h4>Al-Wala' wal-Bara' (loyalty and disassociation for Allah’s Sake)</h4>
<ul class="posts">
  {% for post in site.categories.walabara | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a class="button small icon solid fa-arrow-right" href="/walabara/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Rulership</h4>
<ul class="posts">
  {% for post in site.categories.rulership | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<h4>Funerals</h4>
<ul class="posts">
  {% for post in site.categories.funerals | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a class="button small icon solid fa-arrow-right" href="/funerals/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Wahhabism</h4>
<ul class="posts">
  {% for post in site.categories.wahhabism | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a class="button small icon solid fa-arrow-right" href="/wahhabism/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Qur'an Tafsir (Exegesis)</h4>
<ul class="posts">
  {% for post in site.categories.quran | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a class="button small icon solid fa-arrow-right" href="/tafsir-quran/">View all</a></p>
</ul>
</div>

<div class="box">
<h4>Tawassul</h4>
<ul class="posts">
  {% for post in site.categories.tawassul | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
  <p><a class="button small icon solid fa-arrow-right" href="/tawassul/">View all</a></p>
</ul>
</div>

<div class="box">
<ul class="posts">
    <li><a href="/sects/">The sects</a></li>
</ul>
</div>

</article>