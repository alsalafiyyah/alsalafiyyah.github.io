---
title: Browse by topic
layout: page
active: topic
permalink: /topic/
---

<article class="post">
<p><b>{{ site.posts | size }}</b> fatwas can be found. Start typing in the search form below and hit enter, e.g. [sufism](/search?q=sufism).</p>
{% include search-form.liquid %}

<br/>

<header class="major">
 <span class="date">Recommended for you</span>
</header>

<div class="box">
<h4><a class="icon solid fa fa-folder-open" href="/walabara/"> Al-Wala' wal-Bara' (loyalty and disassociation for Allah’s Sake)</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/rulership/"> Rulership</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/funerals/"> Funerals</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/wahhabism/"> Wahhabism</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/tafsir-quran/"> Qur'an Tafsir (Exegesis)</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/tawassul/"> Tawassul</a></h4>
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
<h4><a class="icon solid fa fa-folder" href="/faq/"> Questions and answers about Salafiyyah</a></h4>
<h4><a class="icon solid fa fa-folder" href="/sects/"> The sects</a></h4>
</div>

</article>