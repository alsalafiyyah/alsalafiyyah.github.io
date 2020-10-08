---
layout: page
title: "Al-Wala' Wal-Bara' (loyalty and disassociation for Allah's Sake)"
active: walabara
author: "Instagram@Alsalafiyyah"
permalink: /walabara/
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
      {% for post in site.categories.walabara %}
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
