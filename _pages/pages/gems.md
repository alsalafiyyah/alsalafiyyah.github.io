---
layout: page
title: "Gems"
permalink: /gems/
---

  <article>
<!-- List -->
<ul class="space-y-10">
{% for g in site.gems %}
  <li>
    <p class="mb-2 text-sm text-muted-foreground-1">
      {{ g.author }}
    </p>
    <p class="font-medium text-sm text-foreground">
      {{ g.title }}
    </p>
    <p class="mt-1 text-sm text-muted-foreground-1">
      {{ g.summary }}
    </p>
    <p class="mt-1">
      <a class="text-sm text-muted-foreground-1 underline hover:text-primary-hover hover:decoration-2 focus:outline-hidden focus:decoration-2" href="{{ g.url }}">
        Continue reading
      </a>
    </p>
  </li>
{% endfor %}
</ul>
<!-- End List -->
  </article>
