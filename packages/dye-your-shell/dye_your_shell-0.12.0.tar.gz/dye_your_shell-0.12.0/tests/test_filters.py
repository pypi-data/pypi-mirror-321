#
# Copyright (c) 2025 Jared Crapo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# pylint: disable=protected-access, missing-function-docstring, redefined-outer-name
# pylint: disable=missing-module-docstring, unused-variable
"""test all the jinja filters

test all the filters for functionality and that the list of all filters
has everything in it
"""

import pytest

from dye.filters import jinja_filters
from dye.pattern import Pattern

#
# jinja_filters()
#
ALL_FILTERS = [
    "fg_hex",
    "fg_hex_no_hash",
    "fg_rgb",
    "bg_hex",
    "bg_hex_no_hash",
    "bg_rgb",
    "ansi_on",
    "ansi_off",
]


def test_filter_list():
    # we don't care about the order, but we need to make
    # sure we have them all and no extras
    # ensuring we have no extras will prompt to write
    # more tests if a filter is added but there are no
    # tests for it
    f = list(jinja_filters().keys())
    assert f.sort() == ALL_FILTERS.sort()


TEMPLATES = [
    # fg_hex
    ("{{styles.dark_orange|fg_hex}}", "#ff6c1c"),
    ("{{styles.pink|fg_hex}}", "#df769b"),
    ("{{styles.cyan|fg_hex}}", "#09ecff"),
    ("{{styles.default|fg_hex}}", ""),
    ("{{styles.nothing|fg_hex}}", ""),
    ("{{variables.something|fg_hex}}", "Hello There."),
    # fg_hex_no_hash
    ("{{styles.dark_orange|fg_hex_no_hash}}", "ff6c1c"),
    ("{{styles.pink|fg_hex_no_hash}}", "df769b"),
    ("{{styles.cyan|fg_hex_no_hash}}", "09ecff"),
    ("{{styles.default|fg_hex_no_hash}}", ""),
    ("{{styles.nothing|fg_hex_no_hash}}", ""),
    ("{{variables.something|fg_hex_no_hash}}", "Hello There."),
    # fg_rgb
    ("{{styles.dark_orange|fg_rgb}}", "rgb(255,108,28)"),
    ("{{styles.pink|fg_rgb}}", "rgb(223,118,155)"),
    ("{{styles.cyan|fg_rgb}}", "rgb(9,236,255)"),
    ("{{styles.default|fg_rgb}}", ""),
    ("{{styles.nothing|fg_rgb}}", ""),
    ("{{variables.something|fg_rgb}}", "Hello There."),
    # bg_hex
    ("{{styles.dark_orange|bg_hex}}", "#222222"),
    ("{{styles.pink|bg_hex}}", ""),
    ("{{styles.cyan|bg_hex}}", ""),
    ("{{styles.default|bg_hex}}", ""),
    ("{{styles.nothing|bg_hex}}", ""),
    ("{{variables.something|bg_hex}}", "Hello There."),
    # bg_hex_no_hash
    ("{{styles.dark_orange|bg_hex_no_hash}}", "222222"),
    ("{{styles.pink|bg_hex_no_hash}}", ""),
    ("{{styles.cyan|bg_hex_no_hash}}", ""),
    ("{{styles.default|bg_hex_no_hash}}", ""),
    ("{{styles.nothing|bg_hex_no_hash}}", ""),
    ("{{variables.something|bg_hex_no_hash}}", "Hello There."),
    # bg_rgb
    ("{{styles.dark_orange|bg_rgb}}", "rgb(34,34,34)"),
    ("{{styles.pink|bg_rgb}}", ""),
    ("{{styles.cyan|bg_rgb}}", ""),
    ("{{styles.default|bg_rgb}}", ""),
    ("{{styles.nothing|bg_rgb}}", ""),
    ("{{variables.something|bg_rgb}}", "Hello There."),
    # ansi_on
    ("{{variables.something|ansi_on}}", "Hello There."),
    # ansi_off
    ("{{variables.something|ansi_off}}", "Hello There."),
]


@pytest.mark.parametrize("template, rendered", TEMPLATES)
def test_filters(template, rendered):
    pattern_str = f"""
        [styles]
        dark_orange = "#ff6c1c on #222222"
        pink = "bold #df769b"
        cyan = "#09ecff on default"
        default = "default"
        nothing = ""

        [variables]
        something = "Hello There."
        output = "echo {template}"
    """
    pattern = Pattern.loads(pattern_str)
    assert pattern.variables["output"] == f"echo {rendered}"


def test_ansi_on_off():
    """
    pattern_str has two kinds of embedded processing

    First, the python f-string takes the template argument
    and puts it where {template} is

    Second, jinja is going to process the whole string and pick up the
    {{ colors.background }} thing
    """
    pattern_str = """
        [styles]
        orng = "#ff6c1c on #222222"
        pink = "bold #df769b"
        cyan = "#09ecff on default"
        default = "default"
        nothing = ""

        [variables]
        something = "Hello There."
        opts = "--prompt={{styles.orng|ansi_on}}>>{{styles.orng|ansi_off}}"
    """
    pattern = Pattern.loads(pattern_str)
    expected_plaintext = 'export OPTS="--prompt=>>"\n'
    assert len(pattern.variables["opts"]) > len(expected_plaintext)
