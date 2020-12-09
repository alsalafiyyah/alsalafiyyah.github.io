---
layout: default
title: Audios
active: audios
locale: en
permalink: /myaudios/
---

{% for item in site.audios.salah %}
{{ item.title }}
{% endfor %}

{% assign audios_salah = site.audios | where:"grouped_by","salah" %}
<ul>
  {% for salah in audios_salah limit:33 %}
    <li><a href="{{ salah.url | relative_url }}">{{ salah.title }}</a></li>
  {% endfor %}
</ul>
