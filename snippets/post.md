---
layout: null
---

#### Posts
Default Front-matter
~~~yaml
---
layout: post
publisher: alsalafiyyah@icloud.com
title: 
hijri: Muharram 09, 1445AH
date: July 27, 2023
source: 
lang: en/ar
note: true/false
group1: true/false
group2: true/false
group3: true/false
group4: true/false
group5: true/false
category: [islam, sunnah]
excerpt: ""
--- 
~~~

###### Custom Variables
~~~yaml
article_taken_from: 
  taken_from:
    - web_title: 
      web_url: 
~~~

~~~yaml
muftis:
  shaykh: 
    - name: Shaykh Salih Al-Fawzan
      url: /biography/fawzan
~~~

~~~yaml
shaykhs: 
 - Shaykh Ibn Baz
 - Shaykh Abdullah ibn Ghudayyan
 - Shaykh Abdul-Razzaq Al-Afifi
~~~

___

###### _config.yml
Group1
~~~yaml
group1:
  chairman: 
    - name: Shaykh Ibn Baz
      url: /biography/binbaz
  deputy_chairman:
    - name: Shaykh Abdul-Razzaq Afifi
      url: /biography/afifi
  members: 
    - name: Shaykh Abdullah ibn Ghudayyan
      url: /biography/ghudayyan
    - name: Shaykh Abdullah ibn Qa'ud
      url: /biography/qaud
~~~

Group 2
~~~yaml
group2:
  chairman: 
    - name: Shaykh Ibn Baz
      url: /biography/binbaz
  deputy_chairman:
    - name: Shaykh Abdul-Aziz Aal Al-Shaykh
      url: /biography/abdulaziz
  members: 
    - name: Shaykh Abdullah ibn Ghudayyan
      url: /biography/ghudayyan
    - name: Shaykh Salih Al-Fawzan
      url: /biography/fawzan
    - name: Shaykh Bakr Abu Zayd
      url: /biography/bakr
~~~

Group 3
~~~yaml
group3:
  chairman: 
    - name: Shaykh Ibn Baz
      url: /biography/binbaz
  deputy_chairman:
    - name: Shaykh Abdul-Razzaq Afifi
      url: /biography/afifi
  members: 
    - name: Shaykh Abdullah ibn Ghudayyan
      url: /biography/ghudayyan
    - name: Shaykh Abdullah ibn Mani'
      url: /biography/mani
~~~

Group 4
~~~yaml
group4:
  chairman: 
    - name: Shaykh Abdul-Razzaq Afifi
      url: /biography/afifi
  members: 
    - name: Shaykh Abdullah ibn Ghudayyan
      url: /biography/ghudayyan
    - name: Shaykh Abdullah ibn Mani'
      url: /biography/mani
~~~
      
___

#### Page Front Matter
~~~yaml
---
layout: default/page
title: 
active: 
lang: en/ar
permalink: 
---
~~~

___

#### Posts
~~~yaml
// All posts
{% for post in site.posts %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
{% endfor %}

// Display post by language
{% assign posts_en = (site.posts | where: "locale" , "en") %}
{% for post in posts_en %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
{% endfor %}

// Limit Posts
{% for post in site.posts limit:5 %}
 {% if post.url %}
  <a href="{{ post.url }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
 {% endif %}
{% endfor %}
~~~
