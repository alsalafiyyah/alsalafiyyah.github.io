#### Post frontmatter
~~~yaml
---
layout: post
publisher: alsalafiyyah@icloud.com
title: Post Title
hijri: Muharram 09, 1445
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
excerpt: "..."
--- 
~~~

#### Custom Variables
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

#### Custom _config.yml
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

#### Display Posts
~~~liquid
// All posts
{% for post in site.posts %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
{% endfor %}
<ol>

{% assign posts = site.posts %}
{% for post in posts %}
 <li><a href="{{ post.url | prepend:site.baseurl }}" title="{{ post.title }}">{{ post.title }}</a></li>
{% endfor %}
</ol>

// pagination post
{% for post in paginator.posts %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
{% endfor %}
{% if paginator.previous_page %}
 <a href="{{ paginator.previous_page_path }}">
 Prev
 </a>
{% else %}
 <span>Prev</span>
{% endif %}
{% if paginator.next_page %}
 <a href="{{ paginator.next_page_path }}">
 Next
 </a>
{% else %}
<span>Next</span>
{% endif %}

// Display post by lang
{% assign posts_en = (site.posts | where: "locale" , "en") %}
{% for post in posts_en %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
{% endfor %}

// Limit post
{% for post in site.posts limit:5 %}
 {% if post.url %}
  <a href="{{ post.url }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
 {% endif %}
{% endfor %}
~~~

___

#### Others
~~~yml
// Date modified
<div id="last-modified"></div>

// posts count
{{ site.posts | size }}
~~~

___

#### Display categories
~~~liquid
{% for category in site.categories %}
 <a href="{{ site.baseurl }}/category/{{ category[0] }}">
  {{ category[0] | capitalize }}
   <span>{{ category[1].size }}</span>
 </a>
{% endfor %}

// select
<select class="browser-default" onchange="document.location.href=this.value">
    <option value="" disabled selected>Categories</option>
    {% for category in site.categories %}
    <option value="{{ site.baseurl }}/category/{{ category[0] }}">{{ category[0] | capitalize }} ({{ category[1].size }})</option>
    {% endfor %}
</select>
~~~
