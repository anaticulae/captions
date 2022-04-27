# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power

import caption

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = caption.PROCESS
power.setup(caption.ROOT)

RESOURCES = [
    power.DISS266_PDF,
    power.DISS205_PDF,
    power.MASTER116_PDF,
    power.BACHELOR111_PDF,
    power.MASTER099_PDF,
    power.MASTER098_PDF,
    power.todo(
        power.BACHELOR090_PDF,
        caption=True,
    ),
    power.MASTER072_PDF,
    power.MASTER063_PDF,
    power.BACHELOR063_PDF,
    power.BACHELOR051_PDF,
    power.BACHELOR056_PDF,
    power.HOME025_PDF,
    power.DOCU007_PDF,
    power.MASTER031_PDF,
    (power.MASTER110_PDF, '0:60'),
]

WORKER = 4


def pytest_sessionstart(session):  # pylint:disable=W0613
    power.run()


def extract(resources):
    destination = power.generated()
    genex.extract(
        resources,
        destination=destination,
        codero=True,
        figureo=True,
        groupme=True,
        cleanup=True,
        tablero=True,
        worker=WORKER,
        pages=':',
        base=power.REPOSITORY,
    )
