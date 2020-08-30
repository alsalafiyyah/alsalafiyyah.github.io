---
layout: page
title: "Hadiths Explanation"
active: hadiths
author: "Instagram@Alsalafiyyah"
permalink: /hadiths/
---

<article class="post">
<a class="button small icon solid" href="/mawdu-daif/">Fabricated and weak Hadiths</a>
<hr/>
<ul class="posts">
  {% for post in site.categories.hadiths %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>
