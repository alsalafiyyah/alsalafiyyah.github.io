---
title: Categories
layout: page
active: categories
permalink: /categorys/
---

<div class="box">
    {% assign tags = site.categories | sort %}
    {% for tag in tags %}
    <a id="{{category}}" data-toggle="tab" href="#{{ tag[0] | slugify }}">
      <span class="fa fa-folder-open" aria-hidden="true"> 
        {{ tag[0] }} ({{ tag | last | size }})
      </span>
    </a>
    {% endfor %}
</div>


<div id="myTab" role="tablist">
    {% for tag in tags %} 
<div class="tab-content mytab-content" id="myTabContent">
<div class="box tab-pane fade" id="{{ tag[0] | slugify }}" role="tabpanel">
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
</div>
    {% endfor %}
</div>