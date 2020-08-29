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
 <span class="date">//</span>
</header>

<div class="row">
 <div class="col-6 col-12-small">
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
</div>
 <div class="col-6 col-12-small">
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
</div>
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

<div class="row">
 <div class="col-6 col-12-small">
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
</div>

 <div class="col-6 col-12-small">
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
 </div>
</div>

<div class="box">
<h4>More</h4>
<div class="row">
 <div class="col-6 col-12-small">
  <ul>
   <li><a class="icon solid fa fa-folder" href="/walabara/"> {{site.data.settings.chapters.walabara}}</a></li>
   <li><a class="icon solid fa fa-file" href="/faq/"> What is Salafiyyah</a></li>
   <li><a class="icon solid fa fa-folder" href="/madhabs/"> {{site.data.settings.chapters.funeral}}</a></li>
   <li><a class="icon solid fa fa-folder" href="/refutals/"> Refutals</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> Women and Hijab</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> {{site.data.settings.chapters.zina}}</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> {{site.data.settings.chapters.nikah}}</a></li>
  </ul>
 </div>
  <div class="col-6 col-12-small">
  <ul>
   <li><a class="icon solid fa fa-folder" href="/sects/"> {{site.data.settings.chapters.sects}}</a></li>
   <li><a class="icon solid fa fa-folder" href="/tawassul/"> {{site.data.settings.chapters.tawassul}}</a></li>
   <li><a class="icon solid fa fa-folder" href="/funerals/"> {{site.data.settings.chapters.funeral}}</a></li>
   <li><a class="icon solid fa fa-folder" href="/non-muslims/"> {{site.data.settings.chapters.non}}</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> {{site.data.settings.chapters.homo}}</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> {{site.data.settings.chapters.misc}}</a></li>
   <li><a class="icon solid fa fa-folder disabled" href="#"> {{site.data.settings.chapters.talaq}}</a></li>
  </ul>
 </div>
</div>
</div>
</article>