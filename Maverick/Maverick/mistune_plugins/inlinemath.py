# -*- coding: utf-8 -*-
"""Math Inline
$ $
"""

import re
import mistune

INLINEMATH_PATTERN = (
    r'\$(.+?)\$'
)


def parse_mathinline(self, m, state):
    match = re.match(INLINEMATH_PATTERN, m.group(0))
    text = match.group(1)
    return 'mathinline', mistune.escape(text)


def render_html_mathinline(text):
    return '$%s$' % (text)


def plugin_mathinline(md):
    md.inline.register_rule('mathinline', INLINEMATH_PATTERN, parse_mathinline)
    md.inline.rules.insert(0, 'mathinline')
    if md.renderer.NAME == 'html':
        md.renderer.register('mathinline', render_html_mathinline)
