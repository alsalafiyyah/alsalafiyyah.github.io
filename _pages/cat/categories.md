---
title: Categories
layout: page
active: categories
permalink: /categorys/
---

<div class="nav nav-mytabs" id="myTab" role="tablist">
<div class="box nav-item">
    {% assign tags = site.categories | sort %}
    {% for tag in tags %}
    <a class="nav-link" id="{{category}}" data-toggle="tab" href="#{{ tag[0] | slugify }}">
      <span class="fa fa-folder-open" aria-hidden="true"> 
        {{ tag[0] }} ({{ tag | last | size }})
      </span>
    </a>
    {% endfor %}
</div>
</div>

        <div class="tab-content mytab-content" id="myTabContent">
         {% for tag in tags %} 
            <div class="tab-pane fade show active" id="{{ tag[0] | slugify }}" role="tabpanel" aria-labelledby="home-tab">
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
            </div>
        {% endfor %}
        </div>

