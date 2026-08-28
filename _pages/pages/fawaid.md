---
layout: no_sidebar
title: "Al-Fawaid (The Benefits)"
summary: ""
permalink: /fawaid/
---

<section class="mb-16">
    <div class="bg-white dark:bg-black transition-colors duration-300">
        <!-- Section Header -->
        <div class="flex items-center gap-4 mb-8 text-[10px] font-black uppercase tracking-[0.3em] text-gray-400 italic border-b-2 border-black/10 dark:border-white/10 pb-4">
            <span class="w-2 h-2 rounded-full bg-red-500 flex-shrink-0 mr-2.5"></span>
            <span class="text-black dark:text-white">Latest Posts & Updates</span>
        </div>

        <!-- Posts Grid (3 columns on desktop) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            {% for c in site.fawaid %}
            <article class="flex flex-col justify-between space-y-4 border-l-2 border-red-500 pl-4 py-1 group cursor-pointer">
                <div class="space-y-2">
                    <span class="text-[10px] font-bold opacity-50 block">{{ c.author }}</span>
                    <h3 class="text-xl md:text-2xl font-black uppercase tracking-tighter serif group-hover:underline leading-snug">
                       {{ c.title }}
                    </h3>
                    <p class="text-xs md:text-sm font-medium leading-relaxed opacity-80">
                       {{ c.summary }}
                    </p>
                </div>
                <div class="pt-2">
                    <a href="{{ c.url }}" class="text-[10px] font-black uppercase tracking-widest text-black dark:text-white flex items-center gap-1 group-hover:text-red-500 transition-colors">
                        Read More <span>→</span>
                    </a>
                </div>
            </article>
            {% endfor %}

        </div>
    </div>
</section>