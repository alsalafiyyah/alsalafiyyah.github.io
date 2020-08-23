---
title: Wahhabism
layout: page
active: wahhabism
permalink: /wahhabism/
---

<article class="post">
<p><a class="button small" href="/biography/">His Da'wah and biography</a></p>
<ul class="posts">
  {% for post in site.categories.wahhabism %}
    {% if post.url %}
    <li>
    <article>
      <header>
      <h4><a href="{{ post.url }}">{{ post.title }}</a></h4>
      </header>
    </article>
    </li>
    {% endif %}
  {% endfor %}
</ul>
</article>