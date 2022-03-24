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
def test_double_caption_master116p101(testdir, monkeypatch):
    source = power.link(power.MASTER116_PDF)
    cmd = f'-i {source} --pages=101 --image --result'
    tests.run(cmd, monkeypatch=monkeypatch)
    figures = iamraw.path.caption_result(testdir.tmpdir)
    figures = serializeraw.load_captions(figures, pages=101)
    figures = utila.flatten_content(figures)
    assert len(figures) == 4
