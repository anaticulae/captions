# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw.path
import power
import serializeraw
import utilatest

import tests


def extract_captions(
    source,
    pages: str,
    td,
    mp,
    resultpath=None,
    selected='',
):
    utilatest.fixture_requires(source)
    resultpath = resultpath if resultpath else iamraw.path.image_caption
    source = power.link(source)
    cmd = f'-i {source} --pages={pages} {selected}'
    tests.run(cmd, mp=mp)
    path = resultpath(td.tmpdir)
    loaded = serializeraw.load_captions(path)
    return loaded
