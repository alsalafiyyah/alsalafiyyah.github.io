---
title: Funerals
layout: page
active: funerals
permalink: /funerals/
---

<article>
 <a class="button small icon solid" href="/inheritance/">Inheritance</a>
 <hr/>
<div class="table-wrapper" itemscope itemtype="https://schema.org/Table">
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Title</th>
      </tr>
    </thead>
    <tbody>
      {% for post in site.categories.funerals %}
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
