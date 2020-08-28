---
title: Browse by topic
layout: page
active: topic
permalink: /topic/
---

<article class="post">
<p><b>{{ site.posts | size }}</b> fatwas can be found.</p>
{% include search-form.liquid %}

<br/>

<header class="major">
 <span class="date">Recommended for you</span>
</header>

<div class="box">
<h4><a class="icon solid fa fa-folder-open" href="/salah/"> Salah (Prayers)</a></h4>
<ul class="posts">
  {% for post in site.categories.salah | limit:3 %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</div>

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
<h4><a class="icon solid fa fa-folder-open" href="/rulership/"> Rulership / Kingship</a></h4>
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
<h4><a class="icon solid fa fa-folder-open" href="/prophets/"> Prophets & Messengers</a></h4>
<ul class="posts">
  {% for post in site.categories.prophets | limit:3 %}
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
<h4><a class="icon solid fa fa-folder" href="/faq/"> What is Salafiyyah</a></h4>
<h4><a class="icon solid fa fa-folder" href="/sects/"> The sects & groups</a></h4>
<h4><a class="icon solid fa fa-folder" href="/tawassul/"> Tawassul</a></h4>
<h4><a class="icon solid fa fa-folder" href="/funerals/"> Funerals</a></h4>
<h4><a class="icon solid fa fa-folder" href="/refutals/"> Refutals</a></h4>
<h4><a class="icon solid fa fa-folder-open" href="/non-muslims/"> Non-Muslims</a></h4>
</div>

</article>