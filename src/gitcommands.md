---
layout: post
title: 一些git命令
slug: gitcommands
date: 2020-5-1 23:50
status: publish
author: ZigZagK
categories: 
  - 实用技巧
tags:
  - git
---

## 上传

```shell
git add .
git commit -m "message"
git push
```

## 拉取

```shell
git pull
```

## 删除tag

```shell
git push origin :refs/tags/tagName
```

## 回滚

```shell
git reset --soft HEAD~1
```

回滚一次（回滚到上一个`commit`），本地文件**不变**。

```shell
git reset --hard HEAD~1
```

回滚一次（回滚到上一个`commit`），本地文件**改变**。