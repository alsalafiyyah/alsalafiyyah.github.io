---
layout: page
title: "Hajj (pilgrimage) and 'Umrah (lesser pilgrimage)"
author: "Instagram@Alsalafiyyah"
permalink: /hajj-umrah/
---

<article>
<div class="table-wrapper" itemscope itemtype="https://schema.org/Table">
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Title</th>
      </tr>
    </thead>
    <tbody>
      {% for post in site.categories.hajj-umrah %}
      <tr>
        <td>{{ post.hijri }}</td>
        <td>
          {% if post.url %}<a title="{{ post.title }}" href="{{ post.url }}">{{ post.title }}</a>{% endif %}
        </td>
      </tr>
      {% else %}
      <p{{site.data.settings.page.no-fatwas}}</p>
      {% endfor %}
    </tbody>
  </table>
</div>
</article>
