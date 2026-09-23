---
layout: page
title: "Gems"
permalink: /gems/
---

{% for g in site.gems %}
  <article>
   <a href="{{ g.url }}" class="block py-6">
    <p class="mb-2 text-sm text-muted-foreground-1">{{ g.author }}</p>
    <h3>{{ g.title }}</h3>
    <p class="mt-1 text-sm text-muted-foreground-1">{{ g.summary }}</p>
    <p class="mt-1">
      <a class="text-sm text-muted-foreground-1 underline hover:text-primary-hover hover:decoration-2 focus:outline-hidden focus:decoration-2" href="{{ g.url }}">
        Continue reading
      </a>
    </p>
    </a>
  </article>
{% endfor %}
