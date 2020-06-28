---
layout: post
title: FFmpeg部分操作
slug: ffmpeg
date: 2020-6-28 12:17
status: publish
author: ZigZagK
categories:
  - 实用技巧
tags:
  - 命令行工具
---

## 合并音频和视频

```plain
ffmpeg -i video.mp4 -i audio.mp3 -codec copy output.mp4
```

将`video.mp4`和`audio.mp3`合并为`output.mp4`。

`video.mp4`不能有音频，否则会出现奇怪的问题。

## 去掉视频中的音频

```plain
ffmpeg -i video.mp4 -an output.mp4
```

将`video.mp4`中的音频去除，得到`output.mp4`。