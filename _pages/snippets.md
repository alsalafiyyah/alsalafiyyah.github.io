---
layout: Page
title: Snippets
robots: noindex
permalink: /snippets/
---

~~~yaml
// date time
{{ post.date }}
{{ site.time }}
~~~

~~~yaml
// posts count
{{ site.posts | size }}
~~~

~~~yaml
{% if page.locale == 'en' %}
 Hello
 {% elsif page.locale == 'ar' %}
 Marhaba
 {% else %}
 Hello
{% endif %}
~~~


### Custom Frontmatter
~~~yaml
muftis:
  shaykh: 
    - name: Shaykh Salih Al-Fawzan
      url: /biography/fawzan
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

~~~yaml
// boolean
group1 : true
note: true
~~~

