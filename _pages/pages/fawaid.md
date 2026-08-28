---
layout: json
title: "Al-Fawaid (The Benefits)"
summary: ""
permalink: /fawaid/
---

<section class="mb-16 hidden">
    <div class="bg-white dark:bg-black transition-colors duration-300">

        <!-- Fawaid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            {% for c in site.fawaid %}
            <article class="flex flex-col justify-between space-y-4 border-l-2 border-red-500 pl-4 py-1 group cursor-pointer">
                <a href="{{ c.url }}" class="space-y-2">
                    <span class="text-[10px] font-bold opacity-50 block">Fawaid</span>
                    <h3 class="text-xl md:text-2xl font-black uppercase tracking-tighter serif group-hover:underline leading-snug">
                       {{ c.title }}
                    </h3>
                    <p class="text-xs md:text-sm font-medium leading-relaxed opacity-80">
                       {{ c.summary }}
                    </p>
                </div>
                <div class="pt-2">
                    <p class="text-[10px] font-black uppercase tracking-widest text-black dark:text-white flex items-center gap-1 group-hover:text-red-500 transition-colors">
                        {{ c.author }}
                    </p>
                </a>
            </article>
            {% endfor %}

        </div>
    </div>
</section>