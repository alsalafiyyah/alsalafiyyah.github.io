---
title: Categories
layout: page
active: categories
permalink: /categorys/
---

    {% assign tags = site.categories | sort %}
<ul id="tabs">
    {% for tag in tags %}
    <li><a class="nav-link" id="{{category}}" data-toggle="tab" href="#{{ tag[0] | slugify }}">
      <span class="fa fa-folder-open" aria-hidden="true"> 
        {{ tag[0] }} ({{ tag | last | size }})
      </span>
    </a></li>
    {% endfor %}
</ul>

            <div class="tabContent" id="{{ tag[0] | slugify }}">
      <h3 id="{{ tag[0] | slugify }}"> {{ tag[0] }}</h3>
      <p>{{ tag | last | size }} fatwas</p>
        <ul>
         {% for tag in tags %} 
        {% for post in tag[1] %}
          <a href="{{ site.baseurl }}{{ post.url }}">
        <li>
          {{ post.title }}
        </li>
        </a>
        {% endfor %}
        {% endfor %}
        </ul>
            </div>

