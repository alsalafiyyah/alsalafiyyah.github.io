---
layout: page
title: "Gems"
permalink: /gems/
---

{% for g in site.gems %} 
<article class="border-b border-border last:border-0"> 
  <div class="py-1"> 
    <p class="mb-1 text-sm text-muted-foreground-1">{{ g.author }}</p> 
    <h3 class="text-xl font-bold">
      <a href="{{ g.url }}" class="hover:text-primary-hover hover:underline">
        {{ g.title }}
      </a>
    </h3> 
    <p class="mt-1 text-sm text-muted-foreground-1">{{ g.summary }}</p> 
    <p class="mt-2"> 
      <a class="text-sm text-muted-foreground-1 underline hover:text-primary-hover hover:decoration-2 focus:outline-hidden focus:decoration-2" href="{{ g.url }}"> 
        Continue reading 
      </a> 
    </p> 
  </div> 
</article> 
{% endfor %}

