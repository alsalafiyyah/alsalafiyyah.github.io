---
layout: page
title: "Qur'an Tafsir"
author: "Instagram@Alsalafiyyah"
permalink: /tafsir-quran/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.quran %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
