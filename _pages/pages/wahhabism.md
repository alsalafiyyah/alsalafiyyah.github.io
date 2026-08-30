---
layout: no_sidebar
title: "Wahhabism"
permalink: /wahhabism/
summary: "There is no sect on the face of the earth that calls itself Wahhabi. Rather, innovators and polytheists apply this label to anyone who singles Allah out in worship, follows the Sunnah of the Messenger of Allah ﷺ."
---

<h3 class="mb-3">Who gave the Shaykh's call (Da'wah) the label "Wahhabism"?</h3>

<p class="mb-3">
Wahhabism is the term applied by opponents of Shaykh Muhammad ibn Abdul-Wahhab’s Da'wah to describe his call toward Tawhid and his rejection of shirk (polytheism) and bid'ah (religious innovation).
</p>

<p>The scholar Dr. Muhammad Taqi al-Din al-Hilali, may Allah have mercy on him [a Moroccan scholar and teacher at the Islamic University of Madinah], stated in 'Al-Husam al-Mahiq p.109–110': "There is no sect on the face of the earth that calls itself 'Wahhabi.' Rather, innovators and polytheists apply this label to anyone who singles Allah out in worship, follows the Sunnah of the Messenger of Allah ﷺ, and avoids innovations and newly invented matters—just as the polytheists used to call the Messenger of Allah ﷺ 'Mudhammam (the blamed one, as an insult)'. In fact, the early polytheists were more sensible than these later ones, for they named the Prophet ﷺ with a word denoting blame in their language while they were the blameworthy ones, whereas the Prophet ﷺ was pure and immaculate, untouched by any of their blame. Similarly, those who follow him until the Day of Judgment are pure, upright Muslims, and it does not harm them what their enemies say about them. As for the later polytheists, they are ignorant of words and meanings, like the reciter who read 'So the roof fell down upon them from above them' and was told, 'You have neither reason nor Quran!'. Thus, naming the people of truth 'Wahhabis'— to Al-Wahhab (The Bestower)—is one of the best of names. The Almighty said, recounting the statement of Abraham, the father of the upright monotheists, in Surah Maryam: **"So when he had turned away from them and from those whom they worshipped besides Allah, We gave him Ishaq (Isaac) and Ya‘qub (Jacob), and each one of them We made a Prophet. And We gave them of Our Mercy (a good provision in plenty), and We granted them honour on the tongues (of all the nations, i.e. everybody remembers them with a good praise)."** [Maryam: 49-50]. And Allah made the polytheists utter a word of truth despite themselves, so they named the people of truth with an attribution to 'the Generous Bestower' (Al-Wahhab)."</p>

<p>Imam Ash-Shawkani stated in Al-Badr al-Tali' 1/262: **"The eminent scholar Sheikh Muhammad ibn Abd al-Wahhab, the caller to monotheism [in the lands of Najd], who condemned those holding beliefs regarding the dead... Those lands had been overcome by matters of Jahiliyyah to the point where Islam had become a stranger there. [He called] to monotheism and demolished constructed graves and elevated domes (because they were worshiped by people at that time)."**</p>

<p>Therefore, the Sufis and the Shia—worshippers of graves and saints—hate the call (Da'wah) of Muhammad ibn Abd al-Wahhab, oppose it, and disparage it with alienating labels.</p>

<p>The Prophet, peace and blessings be upon him, used to call to monotheism and Paradise, while the disbelievers spread rumors about him that he was a sorcerer and a madman.</p>
<p>Allah Almighty said: **"Likewise, no Messenger came to those before them but they said: 'A sorcerer or a madman!'"** [al-Dhariyat: 52]</p>

<p>And He Almighty said: **"Thus have We made for every Prophet an enemy among the Mujrimûn (disbelievers, polytheists, criminals). But Sufficient is your Lord as a Guide and Helper.."** [al-Furqan: 31]</p>

<p>The enemies of the messengers are the enemies of the scholars, because scholars are the heirs of the prophets.</p>

<h3 class="mb-3">If you want to know the people of truth, look at where the arrows of the enemy are aimed, especially the Zionist ones :</h3>

<p>This is a truth recognized long ago by the spiteful "Jewish Orientalist" Ignaz Goldziher, who stated in his book 'Vorlesungen über den Islam' or 'Introduction to Islamic theology and law' : ***"Everyone who sets himself up to judge Islamic events must consider the Wahhabis as champions of the Islamic religion in the form established by the Prophet and his Companions. The ultimate goal of the Wahhabis is to restore Islam to what it was."***</p>

<p>Alexei Vassiliev stated in "The History of Saudi Arabia" p. 102: ***"Wahhabism is a designation given to this movement by its opponents or people from outside the Peninsula, and this designation became entrenched in Orientalist publications. As for the followers of Muhammad ibn Abd al-Wahhab, they called themselves 'Muwahiddun' (Monotheists) or simply 'Muslims,' and were never called 'Wahhabis' at all."***</p>

<p>In Encyclopædia Britannica: ***"The emphasis on the principle of Tawhid (Monotheism) in his thought—Muhammad ibn Abd al-Wahhab—led his followers to describe themselves as Muwahhidun (Monotheists)... or 'those who affirm the oneness of God'... following the teachings of the Prophet alone, ignoring everything else... Their followers refer to themselves as Salafis ('followers of the pious Salaf')... The teachings of Abd al-Wahhab were described as... representing the early era—the era of the Salaf—of the Islamic religion, rejecting sources of creed other than the Quran and the Sunnah. The Sheikh took a clear stance against traditions and practices not rooted in these two sources—the Quran and the Sunnah."***</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt3" id="fatwa-container"></div>

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
      "audio": {{ post.mp3 | jsonify }},
      "videoID": {{ post.videoID | jsonify }},
      "summary": {{ post.content | strip_html | truncatewords: 20 | jsonify }}
    }{% unless forloop.last %},{% endunless %}

  {% endfor %}

]
</script>
