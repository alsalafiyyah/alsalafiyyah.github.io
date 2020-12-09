---
layout: default
title: Audios
active: audios
uid: myaudios
locale: en
permalink: /myaudios/
---

<ol>
{% assign items = site.audios %}
{% for item in items %}
  {% if not item.path contains '/salah' %}
  <li>
    <a href="{{item.url}}">{{item.title}}</a>
    <ol>
  {% else %}
      <li><a href="{{item.url}}">{{item.title}}</a></li>
  {% endif %}
    </ol>
  </li>
{% endfor %}
<ol>
