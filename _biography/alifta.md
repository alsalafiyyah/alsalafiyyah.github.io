---
layout: post
publisher: alsalafiyyah@icloud.com
title: "Scholars of the Permanent Committee for Scholarly Research and Ifta"
active: biography
summary: "List of the Scholars of the Permanent Committee for Scholarly Research and Ifta or known as Alifta"
scholar_groups:
  - name: "Shaykh Abdul-Aziz ibn Abdullah ibn Baz"
    url: "/biography/binbaz"
  - name: "Shaykh Abdullah al-Ghudayyan"
    url: "/biography/ghudayyan"
  - name: "Shaykh Abdullah ibn Qa'ud"
    url: "/biography/qaud"
  - name: "Shaykh Abdur-Razzaq Afifi"
    url: "/biography/afifi"
  - name: "Shaykh Bakr Abu Zayd"
    url: "/biography/bakr"
  - name: "Shaykh Ibrahim ibn Muhammad Al al-Sheikh"
    url: "/biography/ibrahim"
  - name: "Shaykh Muhammad ibn Ibrahim Al al-Sheikh"
    url: "/biography/abdulaziz"
  - name: "Shaykh Saleh Al-Fawzan"
    url: "/biography/fawzan"
  - name: "Shaykh Abdullah ibn Muni"
    url: "/biography/mani"
---

<ul>
  {% for s in page.scholar_groups %}
    <li><a href="{{ s.url | relative_url }}">{{ s.name }}</a></li>
  {% endfor %}
</ul>
