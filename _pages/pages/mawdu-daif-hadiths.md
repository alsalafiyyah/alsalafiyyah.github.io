---
layout: page
title: "Mawdu' (Fabricated) or Da'if (Weak) Hadiths"
author: "Instagram@Alsalafiyyah"
permalink: /mawdu-daif/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.mawdu-daif %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
    {% else %}
    <p>{{site.data.settings.page.no-fatwas}}</p>
  {% endfor %}
</ul>
</article>
