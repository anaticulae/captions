# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import iamraw.path
import serializeraw
import utilo
import utilotest

import tests


@utilotest.requires(hoverpower.BACHELOR051_PDF)
def test_mixed_bachelor51p30(td, mp):
    source = hoverpower.link(hoverpower.BACHELOR051_PDF)
    cmd = f'-i {source} --pages=30'
    tests.run(cmd, mp=mp)

    table = iamraw.path.table_caption(td.tmpdir)
    figure = iamraw.path.image_caption(td.tmpdir)

    table = serializeraw.load_captions(table)
    figure = serializeraw.load_captions(figure)

    figures = utilo.select_content(figure, page=30)
    assert len(figures) == 1, str(figures)
    tables = utilo.select_content(table, page=30)
    assert len(tables) == 1, str(tables)
