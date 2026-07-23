# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import caption

DESCRIPTION = 'TODO'

CAPTION_DATA = [
    utilo.ResultFile('rawmaker', 'oneline_text_text'),
    utilo.ResultFile('rawmaker', 'oneline_text_positions'),
    utilo.ResultFile('rawmaker', 'border_pages'),
    utilo.ResultFile('groupme', 'footer_footerheader'),
]

WORKPLAN = [
    utilo.create_step(
        name='image',
        inputs=CAPTION_DATA + [
            utilo.Pattern('rawmaker__images_images/*', 'yaml'),
        ],
        output=('caption',),
    ),
    utilo.create_step(
        name='code',
        inputs=CAPTION_DATA + [
            utilo.ResultFile('codero', 'result_result', optional=True),
            utilo.ResultFile(
                producer='cleanup',
                name='oneline_translate_text',
                optional=True,
            ),
        ],
        output=('caption',),
    ),
    utilo.create_step(
        name='table',
        inputs=CAPTION_DATA + [
            utilo.ResultFile('tablero', 'decide_decide', optional=True),
        ],
        output=('caption',),
    ),
    utilo.create_step(
        'result',
        inputs=[
            utilo.ResultFile(caption.PROCESS, 'image_caption', optional=True),
            utilo.ResultFile(caption.PROCESS, 'table_caption', optional=True),
            utilo.ResultFile(caption.PROCESS, 'code_caption', optional=True),
        ],
        output=('result',),
    ),
]


def main():
    utilo.featurepack(
        workplan=WORKPLAN,
        root=caption.ROOT,
        featurepackage='caption.feature',
        config=utilo.FeaturePackConfig(
            description=DESCRIPTION,
            multiprocessed=True,
            name=caption.PROCESS,
            pages=True,
            version=caption.__version__,
        ),
    )
