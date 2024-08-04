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

// posts count
{{ site.posts | size }}

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

// boolean
group1 : true
note: true

~~~

