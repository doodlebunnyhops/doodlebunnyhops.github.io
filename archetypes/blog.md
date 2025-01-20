---
author: ""
date: "{{ .Date }}"
published: "{{ .Date }}"
title: ""
cascade:
  - url: /blog/:filename
archetype: "blog"
imagecust: ""
images: []
description: ""
noindex: false
hidden: true
tags: []
---
<!-- ---
date: '{{ .Date }}'
draft: true
title: '{{ replace .File.ContentBaseName `-` ` ` | title }}'
archetype: "blog"
--- -->