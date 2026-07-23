# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import hoverpower
import iamraw
import pytest
import serializeraw
import utilo
import utilotest

import caption
import tests

ARCHIVE = utilo.join(caption.ROOT, 'tests/expected', exist=True)


@pytest.mark.parametrize('source, expected', [
    pytest.param(hoverpower.BACHELOR051_PDF, 'bachelor051', id='bachelor051'),
    pytest.param(hoverpower.BACHELOR056_PDF, 'bachelor056', id='bachelor056'),
    pytest.param(hoverpower.BACHELOR063_PDF, 'bachelor063', id='bachelor063'),
    pytest.param(hoverpower.BACHELOR090_PDF, 'bachelor090', id='bachelor090'),
    pytest.param(hoverpower.BACHELOR111_PDF, 'bachelor111', id='bachelor111'),
    pytest.param(hoverpower.DISS205_PDF, 'diss205', id='diss205'),
    pytest.param(hoverpower.DISS266_PDF, 'diss266', id='diss266'),
    pytest.param(hoverpower.DOCU007_PDF, 'docu007', id='docu007'),
    pytest.param(hoverpower.HOME025_PDF, 'home025', id='home025'),
    pytest.param(hoverpower.MASTER031_PDF, 'master031', id='master031'),
    pytest.param(hoverpower.MASTER063_PDF, 'master063', id='master063'),
    pytest.param(hoverpower.MASTER072_PDF, 'master072', id='master072'),
    pytest.param(hoverpower.MASTER091B_PDF, 'master091b', id='master091b'),
    pytest.param(hoverpower.MASTER098_PDF, 'master098', id='master098'),
    pytest.param(hoverpower.MASTER099_PDF, 'master099', id='master099'),
    pytest.param(hoverpower.MASTER110_PDF, 'master110', id='master110'),
    pytest.param(hoverpower.MASTER116_PDF, 'master116', id='master116'),
])
@utilotest.longrun
def test_validate(source, expected, td, mp):
    utilotest.fixture_requires(source)
    Evaluate(
        source=source,
        pages=':',
        expected=expected,
        workdir=td.tmpdir,
        mp=mp,
    ).evaluate()


class Evaluate(utilotest.BaseLiner):

    def __init__(self, source, pages, expected, workdir, mp):
        super().__init__(
            program=functools.partial(
                tests.run,
                mp=mp,
            ),
            step=None,
            pages=pages,
            source=hoverpower.link(source),
            workdir=workdir,
            archive=ARCHIVE,
            loader=self.frompath,
            convert_source=False,
            index=expected,
        )
        self.headlines = hoverpower.link(source)

    def frompath(self, path):  # pylint:disable=R0201
        path = iamraw.path.caption_result(path)
        return serializeraw.load_captions(path)

    def raw(self, value) -> str:
        value = utilo.flatten_content(value)
        collected = [
            utilo.normalize_text(
                item.raw,
                normalize_spaces=True,
            ) for item in value
        ]
        collected = sorted(collected, key=utilo.alphabetically)
        result = utilo.NEWLINE.join(collected)
        return result
