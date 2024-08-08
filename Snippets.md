#### Post frontmatter
~~~yaml
---
layout: post
publisher: alsalafiyyah@icloud.com
published: true
title: Post Title
hijri: Muharram 09, 1445
date: 2023-06-27
source: 
locale: en
note: false
group1: true
group2: false
group3: false
group4: false
group5: false
category: [islam, sunnah, ...]
excerpt: "..."
---

// embed audio
---
layout: page
publisher: alsalafiyyah@icloud.com
published: true
title: Post Title
hijri: Muharram 09, 1445
date: 2023-06-27
source: 
locale: en
note: false
category: [islam, sunnah, audios]
output: html_document
excerpt: "..."
shaykhs: 
 - Shaykh Ibn Baz
---
<audio controls>
 <source src="file.mp3" type="audio/mpeg"/><p>Your browser does not support the audio element.</p>
</audio>

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
 - Sh. Ibn Baz
 - Sh. Abdullah ibn Ghudayyan
 - Sh. Abdul-Razzaq Al-Afifi
~~~

~~~yaml
muftis:
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
___

#### _config.yml boolean
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
layout: page
title: Page Title
active: docs
locale: en
excerpt: "..."
permalink: /docs/
---
~~~

___

#### Display Posts
~~~yml
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

// Limit post
{% for post in site.posts limit:5 %}
 {% if post.url %}
  <a href="{{ post.url }}">{{ post.title }}</a>
  <p>{{ post.excerpt }}</p>
  <date>{{ post.hijri }}</date>
 {% endif %}
{% endfor %}

// _posts/bidah
{% for post in site.posts %}
{% assign first_dir = post.path | remove_first: "_posts/" | split: "/" | first %}
 <a href="{{ post.url }}">{{ post.title }}</a>
 <time>{{ post.date | date: "%b %d, %Y" }}</time>
 <p>{{ post.excerpt }}</p>
 {% if first_dir == 'bidah' %}
 {% endif %}
{% endfor %}

// Categories
  {% if post %}
    {% assign category = post.categories %}
  {% else %}
    {% assign category = page.categories %}
  {% endif %}
  {% for category in categories %}
  <a href="{{site.baseurl}}/category/{{category|slugize}}">{{category}}</a>
  {% unless forloop.last %}&nbsp;{% endunless %}
  {% endfor %}

// Post Category loop
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'Foo'" %}
{% for post in posts %}
  {{ post.title }}
{% endfor %}

~~~

___

#### Others
~~~yaml
// Date modified
<div id="last-modified"></div>

// posts count
{{ site.posts | size }}

{% if page.locale == 'en' %}
 Hello
 {% elsif page.locale == 'ar' %}
 Marhaba
 {% else %}
 Hello
{% endif %}

{% if page.locale == 'ar' %}
 dir=rtl
{% endif %}

{% for item in site.data.myData %}
 <li><{{ item.title }}/li>
{% endfor %}

{% for item in site.data.myData %}
{{ forloop.index }} //auto numbering
{{ item.title }}
{% endfor %}

~~~

___

#### Display categories
~~~yaml
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

// tags
{% for tag in post.tags %}
<a href="{{ site.baseurl }}/tag/{{ tag | slugify }}">
{{ tag }}
</a>
{% unless forloop.last %}, {% endunless %}
{% endfor %}
~~~

___

#### Diplay pagination in a content collection
~~~yaml

// Muqolat collection
{% for c in site.muqolat %}
{% if c.title == page.title %}
  {% assign thisPost = c %}
  {% if forloop.index == 1 %}
    {% assign prevflag = 0 %}
    {% assign nextflag = 1 %}
  {% elsif forloop.index == forloop.length %}
    {% assign prevflag = 1 %}
    {% assign nextflag = 0 %}
  {% else %}
    {% assign prevflag = 1 %}
    {% assign nextflag = 1 %}
  {% endif %}  
{% endif %}
{% endfor %}

{% for c in site.muqolat %}
  {% if c.title == page.title %}
    {% assign prevflag = 0 %}
  {% endif %}
  {% if prevflag == 1 %}
    {% assign prevPost = c %}
    {% assign page.previous = c %}
  {% endif %}
{% endfor %}

{% if nextflag == 1 %}
  {% for c in site.muqolat %}
    {% if foundPost == 1 %}
      {% assign getNext = 1 %}
    {% endif %}
    {% if c.title == page.title %}
      {% assign foundPost = 1 %}        
    {% endif %}
    {% if getNext == 1%}
      {% assign nextPost = c %}
      {% assign page.next = c %}
      {% assign foundPost = 0 %}
      {% assign getNext = 0 %}
    {% endif %}
  {% endfor %}
{% endif %}

<article>
  <h3>{{ page.title }}</h3>
  {{ content }}
</article>

<div>    
{% if prevPost.url %}
<a rel="prev" href="{{prevPost.url}}">
 <span>&lt; {{prevPost.title}}</span>
</a> 
{% endif %}
{% if nextPost.url %} 
<a rel="next" href="{{nextPost.url}}">
 <span>{{nextPost.title}} &gt;</span>
</a> 
{% endif %}
</div>

~~~
