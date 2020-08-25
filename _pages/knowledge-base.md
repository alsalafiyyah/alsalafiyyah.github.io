---
title: Recommended
layout: page
active: basic
permalink: /basic/
---

<article class="post">

<div class="box">
<h4><a class="icon solid fa-arrow-right" href="/walabara/"> Al-Wala' wal-Bara' (loyalty and disassociation for Allah’s Sake)</a></h4>
<ul class="posts">
  {% for post in site.categories.walabara | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<h4><a class="icon solid fa-arrow-right" href="/rulership/"> Rulership</a></h4>
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
<h4><a class="icon solid fa-arrow-right" href="/funerals/"> Funerals</a></h4>
<ul class="posts">
  {% for post in site.categories.funerals | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<h4><a class="icon solid fa-arrow-right" href="/wahhabism/"> Wahhabism</a></h4>
<ul class="posts">
  {% for post in site.categories.wahhabism | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<h4><a class="icon solid fa-arrow-right" href="/tafsir-quran/"> Qur'an Tafsir (Exegesis)</a></h4>
<ul class="posts">
  {% for post in site.categories.quran | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<h4><a class="icon solid fa-arrow-right" href="/tawassul/"> Tawassul</a></h4>
<ul class="posts">
  {% for post in site.categories.tawassul | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

<div class="box">
<ul class="posts">
    <li><a class="icon solid fa-arrow-right" href="/sects/"> The sects</a></li>
</ul>
</div>

</article>