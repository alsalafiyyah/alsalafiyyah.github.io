---
title: Categories
layout: page
active: categories
permalink: /category/
---

<article class="post">
{% assign categories = "" | split: '/'%}
{% for page in site.pages %}
{% assign page_cats = page.dir | split:'/' %}
{% if page_cats[1] == site.docs_dir %}
{% assign category = page_cats[2] | strip %}
{% unless category == "" %}
{% unless categories contains category %}
{% assign categories = categories | push: category %}
{% endunless %}
{% endunless %}
{% endif %}
{% endfor %}

<div class="box">
    {% assign tags = site.categories | sort %}
    {% for tag in tags %}
    <a href="#{{ tag[0] | slugify }}">
      <span class="fa fa-folder-open" aria-hidden="true"> 
        {{ tag[0] }} ({{ tag | last | size }})
      </span>
    </a>
    {% endfor %}
</div>

    {% for tag in tags %} 
<div class="box">
      <h3 id="{{ tag[0] | slugify }}"> {{ tag[0] }}</h3>
      <p>{{ tag | last | size }} fatwas</p>
      <ul class="later on">
        {% for post in tag[1] %}
          <a class="post-subtitle" href="{{ site.baseurl }}{{ post.url }}">
        <li>
          {{ post.title }}
        </li>
        </a>
        {% endfor %}
      </ul>
        <a href="#top" class="btn btn-default">
          Back to top
        </a> 
</div>
    {% endfor %}
</article>