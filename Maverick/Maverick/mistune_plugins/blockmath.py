# -*- coding: utf-8 -*-
"""Math Block
$$ $$
"""

import re
import mistune

BLOCKMATH_PATTERN = (
    r'\$\$([\s\S]+?)\$\$'
)


def parse_mathblock(self, m, state):
    match = re.match(BLOCKMATH_PATTERN, m.group(0))
    text = match.group(1)
    return 'mathblock', mistune.escape(text)


def render_html_mathblock(text):
    return '<p>$$%s$$</p>\n' % (text)


def plugin_mathblock(md):
    md.inline.register_rule('mathblock', BLOCKMATH_PATTERN, parse_mathblock)
    md.inline.rules.insert(0, 'mathblock')
    if md.renderer.NAME == 'html':
        md.renderer.register('mathblock', render_html_mathblock)
