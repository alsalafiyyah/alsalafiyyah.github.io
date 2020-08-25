---
title: Rulership
layout: page
active: rulership
permalink: /rulership/
---

<article class="post">
<ul class="posts">
  {% for post in site.categories.rulership %}
    {% if post.url %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      </header>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>