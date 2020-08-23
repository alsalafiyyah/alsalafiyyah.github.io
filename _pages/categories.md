---
title: Categories
layout: page
active: categories
permalink: /category/
---

{% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <h4>{{ category_name }}</h4>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></li>
    {% endfor %}
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