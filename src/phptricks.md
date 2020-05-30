---
layout: post
title: 一些PHP奇技淫巧
slug: phptricks
date: 2020-5-31 00:27
status: publish
author: ZigZagK
categories:
  - 实用技巧
tags:
  - PHP
---

## 判断PJAX请求

```php
if ($_SERVER['HTTP_X_PJAX']=='true') {}
```

