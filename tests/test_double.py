# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw.path
import power
import serializeraw
import utila
import utilatest

import tests


@utilatest.requires(power.MASTER116_PDF)
def test_double_caption_master116p101(td, mp):
    source = power.link(power.MASTER116_PDF)
    cmd = f'-i {source} --pages=101 --image --result'
    tests.run(cmd, mp=mp)
    figures = iamraw.path.caption_result(td.tmpdir)
    figures = serializeraw.load_captions(figures, pages=101)
    figures = utila.flatten_content(figures)
    assert len(figures) == 4


# yapf:disable
EXPECTED = utila.splitlines("""\
Strecke Behala 1400 - Logarithmische Häufigkeitsverteilung der Traktionsleistung.
Strecke Chemiepark - Logarithmische Häufigkeitsverteilung der Traktionsleistung.
Strecke Behala 1800 - Logarithmische Häufigkeitsverteilung der Traktionsleistung.
Strecke Referenzzyklus - Logarithmische Häufigkeitsverteilung der Traktionsleistung.
""", lowers=False)
# yapf:enable


@utilatest.requires(power.MASTER116_PDF)
def test_double_caption_master116p34(td, mp):
    source = power.link(power.MASTER116_PDF)
    cmd = f'-i {source} --pages=34 --image --result'
    tests.run(cmd, mp=mp)
    figures = iamraw.path.caption_result(td.tmpdir)
    figures = serializeraw.load_captions(figures, pages=34)
    figures = utila.flatten_content(figures)
    assert len(figures) == 4
    current = set(item.text for item in figures)
    assert current == EXPECTED
