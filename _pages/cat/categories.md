---
title: Categories
layout: page
active: categories
permalink: /categorys/
---

<div class="box">
    {% assign categories = site.categories | sort %}
    {% for category in categories %}
    <a href="#{{ category[0] | slugify }}">
      <span class="fa fa-folder-open" aria-hidden="true"> 
        {{category[0]}} ({{ category | last | size }})
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