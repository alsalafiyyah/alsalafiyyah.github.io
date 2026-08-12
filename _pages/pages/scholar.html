---
layout: no_sidebar
title: "Scholars"
summary: ""
permalink: /scholar/
---

{% assign folder_path = "_pages/scholar" %}
{% assign target_files = site.pages | where_exp: "item", "item.path contains folder_path" | where_exp: "item", "item.url != page.url" %}

<p class="text-sm font-semibold uppercase tracking-widest text-gray-400 dark:text-zinc-500 mb-6">
    Total Scholars: {{ target_files.size }}
</p>

<section class="mt-12 space-y-0">
  {% for file in target_files %}
    {% assign scholar_slug = file.name | replace: ".md", "" | replace: ".html", "" %}
    {% assign scholar_posts_path = "_posts/" | append: scholar_slug | append: "/" %}
    {% assign scholar_post_count = site.posts | where_exp: "post", "post.path contains scholar_posts_path" | size %}
        
    <!-- Individual Scholar Row -->
    <div class="group py-10 border-b border-gray-200 dark:border-zinc-800 grid grid-cols-1 md:grid-cols-12 gap-6 items-center transition-colors duration-200">
        
        <!-- Metadata & Heading -->
        <div class="md:col-span-8 space-y-1">
            <span class="inline-block text-[11px] font-black uppercase tracking-widest text-gray-400 dark:text-zinc-500">
                {{ scholar_post_count }} Entries
            </span>
            <h3 class="text-3xl md:text-3xl font-black uppercase tracking-tighter font-serif text-gray-900 dark:text-white transition-all">
                <a href="{{ file.url | relative_url }}" class="group-hover:text-blue-600 dark:group-hover:text-blue-400 group-hover:underline decoration-2 underline-offset-4 transition-all">
                    {{ file.title | default: file.name }}
                </a>
            </h3>
        </div>

        <!-- Action Links -->
        <div class="md:col-span-4 flex md:flex-col items-start md:items-end justify-between md:justify-center space-y-0 md:space-y-2">
            <!-- Primary Action: Read Biography -->
            {% if file.bio_url %}
            <div>
                <a href="{{ file.bio_url }}" class="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-gray-900 dark:text-zinc-200 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                    <span>Read Biography</span>
                    <svg class="w-3.5 h-3.5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path>
                    </svg>
                </a>
            </div>
            {% endif %}

            <!-- Official Website -->
            {% if file.official_web %}
            <div>
                <a href="{{ file.official_web }}" class="text-[11px] font-semibold uppercase tracking-widest tabular-nums text-gray-400 dark:text-zinc-500 hover:text-gray-600 dark:hover:text-zinc-300 transition-colors" target="_blank" rel="noopener noreferrer">
                    Official Website ↗
                </a>
            </div>
            {% endif %}
        </div>

    </div>
  {% endfor %}
</section>