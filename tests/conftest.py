# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import gennex
import hoverpower
import utilotest
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611

import caption

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = caption.PROCESS
hoverpower.setup(caption.ROOT)

RESOURCES = [
    (hoverpower.MASTER110_PDF, '0:60'),
    hoverpower.BACHELOR051_PDF,
    hoverpower.BACHELOR056_PDF,
    hoverpower.BACHELOR063_PDF,
    hoverpower.BACHELOR090_PDF,
    hoverpower.BACHELOR111_PDF,
    hoverpower.DISS205_PDF,
    hoverpower.DISS266_PDF,
    hoverpower.DOCU007_PDF,
    hoverpower.HOME025_PDF,
    hoverpower.MASTER031_PDF,
    hoverpower.MASTER063_PDF,
    hoverpower.MASTER072_PDF,
    hoverpower.MASTER091B_PDF,
    hoverpower.MASTER098_PDF,
    hoverpower.MASTER099_PDF,
    hoverpower.MASTER116_PDF,
]

WORKER = utilotest.worker_count(5, onci=len(RESOURCES))


def pytest_sessionstart(session):  # pylint:disable=W0613
    hoverpower.run()


def extract(resources):
    gennex.extract(
        resources,
        cleanup=True,
        codero=True,
        # figureo=True,
        footnote=True,
        headnote=True,
        groupme=True,
        pagenumber=True,
        tablero=True,
        worker=WORKER,
        pages=':',
    )
