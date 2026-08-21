---
layout: page
title: "Wahhabism?"
permalink: /wahhabism/
summary: "There is no sect on the face of the earth that calls itself Wahhabi. Rather, innovators and polytheists apply this label to anyone who singles Allah out in worship, follows the Sunnah of the Messenger of Allah ﷺ."
---

<p class="mb-3">
Wahhabism is the term applied by opponents of Shaykh Muhammad ibn Abdul-Wahhab’s Da'wah to describe his call toward Tawhid and his rejection of shirk (polytheism) and bid'ah (religious innovation).
</p>

The scholar Dr. Muhammad Taqi al-Din al-Hilali, may Allah have mercy on him [a Moroccan scholar and teacher at the Islamic University of Madinah], stated in 'Al-Husam al-Mahiq p.109–110':

There is no sect on the face of the earth that calls itself 'Wahhabi.' Rather, innovators and polytheists apply this label to anyone who singles Allah out in worship, follows the Sunnah of the Messenger of Allah ﷺ, and avoids innovations and newly invented matters—just as the polytheists used to call the Messenger of Allah ﷺ 'Mudhammam (the blamed one, as an insult)'. In fact, the early polytheists were more sensible than these later ones, for they named the Prophet ﷺ with a word denoting blame in their language while they were the blameworthy ones, whereas the Prophet ﷺ was pure and immaculate, untouched by any of their blame. Similarly, those who follow him until the Day of Judgment are pure, upright Muslims, and it does not harm them what their enemies say about them. As for the later polytheists, they are ignorant of words and meanings, like the reciter who read 'So the roof fell down upon them from above them' and was told, 'You have neither reason nor Quran!'. Thus, naming the people of truth 'Wahhabis'— to Al-Wahhab (The Bestower)—is one of the best of names. The Almighty said, recounting the statement of Abraham, the father of the upright monotheists, in Surah Maryam: **"So when he had turned away from them and from those whom they worshipped besides Allah, We gave him Ishaq (Isaac) and Ya‘qub (Jacob), and each one of them We made a Prophet. And We gave them of Our Mercy (a good provision in plenty), and We granted them honour on the tongues (of all the nations, i.e. everybody remembers them with a good praise)."** [Maryam: 49-50]. And Allah made the polytheists utter a word of truth despite themselves, so they named the people of truth with an attribution to 'the Generous Bestower' (Al-Wahhab).

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
