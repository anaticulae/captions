# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import power
import pytest
import utila

import tests
import tests.utils


def test_cli_help(mp):
    tests.run('--help', mp=mp)


@pytest.mark.parametrize('page, expected', [
    (18, 1),
    (21, 2),
])
def test_bachelor90px(page, expected, td, mp):
    source = power.BACHELOR090_PDF
    extracted = tests.utils.extract_captions(
        source,
        page,
        td,
        mp,
    )
    content = utila.select_content(extracted, page)
    assert len(content) == expected


def test_bachelor90p80(td, mp):
    source = power.BACHELOR090_PDF
    extracted = tests.utils.extract_captions(
        source,
        80,
        td,
        mp,
        iamraw.path.table_caption,
    )
    tables = extracted[0].content
    assert len(tables) == 1, str(tables)


def test_master116p12(td, mp):
    source = power.MASTER116_PDF
    extracted = tests.utils.extract_captions(
        source,
        12,
        td,
        mp,
        iamraw.path.caption_image,
    )
    figures = extracted[0].content
    assert len(figures) == 2, str(figures)
    caption_2_1 = figures[0]
    assert caption_2_1.line == 4
    assert caption_2_1.lineend == 5
    caption_2_2 = figures[1]
    assert caption_2_2.line == 14
    assert caption_2_2.lineend == 16
