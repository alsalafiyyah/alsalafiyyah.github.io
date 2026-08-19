---
layout: page
title: "Wahhabism?"
permalink: /wahhabism/
summary: "Refuting the Slander against the Shaykh Muhammad ibn Abdul-Wahhab"
---
<p class="mb-3">
Wahhabism is the term applied by opponents of Shaykh Muhammad ibn Abdul-Wahhab’s Da'wah to describe his call toward Tawhid and his rejection of shirk (polytheism) and bid'ah (religious innovation).
</p>

<div id="fatwa-container"></div>
<nav id="pagination-nav" class="flex items-center justify-between border-t-4 border-black dark:border-white pt-12 mt-12 mb-24">
    <a id="prev-link" href="#" class="text-sm font-black uppercase tracking-widest hover:line-through invisible">← Newer</a>
    
    <div class="text-sm font-black uppercase tracking-widest tabular-nums">
        Page <span id="current-page-display">01</span> of <span id="total-pages-display">01</span>
    </div>
    
    <a id="next-link" href="#" class="text-sm font-black uppercase tracking-widest hover:line-through invisible">Older →</a>
</nav>
<script id="fatwa-data" type="application/json">
[
  {% assign posts = site.posts | where_exp: "post", "post.categories contains 'wahhabism'" %}
  {% for post in posts %}
    {
      "title": {{ post.title | jsonify }},
      "url": {{ post.url | jsonify }},
      "date": {{ post.date | date: "%Y-%m-%d" | jsonify }},
      "hijri": {{ post.hijri | jsonify }},
      "summary": {{ post.content | strip_html | truncatewords: 20 | jsonify }}
    }{% unless forloop.last %},{% endunless %}
  {% endfor %}
]
</script>
