---
layout: page
title: "Gems"
permalink: /gems/
---
{% for g in site.gems %}
<article class="group block border-b border-black/10 dark:border-white/10 hover:border-black dark:hover:border-white transition-colors duration-300 py-4 first:pt-0 last:border-b-0">
    <a href="{{ g.url | relative_url }}" class="flex flex-col gap-1 w-full">
        
        <!-- Author / Metadata Line -->
        {% if g.author %}
        <div class="text-[10px] font-black uppercase tracking-[0.2em] text-zinc-400 dark:text-zinc-500">
            {{ g.author }}
        </div>
        {% endif %}

        <!-- Title -->
        <h3 class="text-lg md:text-xl font-black uppercase tracking-tighter serif text-black dark:text-white group-hover:underline decoration-2 underline-offset-4 leading-tight">
            {{ g.title }}
        </h3>

        <!-- Summary -->
        <p class="text-xs md:text-sm font-medium leading-relaxed text-zinc-500 dark:text-zinc-400 line-clamp-2">
            {{ g.summary }}
        </p>

        <!-- Continue Reading Link -->
        <div class="pt-1">
            <span class="text-[10px] font-black uppercase tracking-widest text-black dark:text-white flex items-center gap-1 group-hover:text-red-500 transition-colors">
                Continue Reading →
            </span>
        </div>

    </a>
</article>
{% endfor %}

