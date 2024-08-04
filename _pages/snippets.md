---
layout: Page
title: Snippets
robots: noindex
permalink: /snippets/
---

~~~liquid
// date time
{{ post.date }}
{{ site.time }}
~~~

~~~liquid
// posts count
{{ site.posts | size }}
~~~

~~~liquid
{% if page.locale == 'en' %}
 Hello
 {% elsif page.locale == 'ar' %}
 Marhaba
 {% else %}
 Hello
{% endif %}
~~~


### Custom Frontmatter
~~~liquid
muftis:
  shaykh: 
    - name: Shaykh Salih Al-Fawzan
      url: /biography/fawzan
~~~

~~~liquid
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

~~~liquid
// boolean
group1 : true
note: true
~~~

