# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Wiki/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "ZigZagK's Wiki"
site_logo = "${static_prefix}ZigZagK.png"
site_build_date = "2020-4-8T11:51+08:00"
author = "ZigZagK"
email = "zigzagk@qq.com"
author_homepage = "https://zigzagk.top"
description = "Never give up fighting!"
key_words = ['Maverick', 'ZigZagK', 'Kepler', 'wiki']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "ZigZagK的博客",
        "url": "https://zigzagk.top",
        "brief": "Never give up fighting!"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/ZigZagK",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
