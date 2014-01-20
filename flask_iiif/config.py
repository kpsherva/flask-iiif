# -*- coding: utf-8 -*-
#
# This file is part of Flask-IIIF
# Copyright (C) 2014 CERN.
#
# Flask-IIIF is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Multimedia configuration."""

# Multimedia Image cache duration
# 60 seconds * 60 minutes (1 hour) * 24 (24 hours) * 2 (2 days) = 172800 secs
# 60 seconds * 60 (1 hour) * 24 (1 day) * 2 (2 days)

MULTIMEDIA_IMAGE_CACHE_TIME = 60 * 60 * 24 * 2

# Supported qualities
MULTIMEDIA_IMAGE_API_QUALITIES = ('default', 'grey', 'bitonal',
                                  'color', 'native')
MULTIMEDIA_IMAGE_API_COVERTERS = '', 'L', '1', '', ''

# Supported multimedia image API formats
MULTIMEDIA_IMAGE_API_SUPPORTED_FORMATS = {
    'gif': 'image/gif',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'pdf': 'application/pdf',
    'png': 'image/png',
}

# Regular expressions to validate each parameter of iiif API v2.0
IIIF_API_VALIDATIONS = {
    "v1": {
        "region": {
            "ignore": "full",
            "validate": "(^full|(pct:)?([\d.]+,){3}([\d.]+))",
        },
        "size": {
            "ignore": "full",
            "validate": ("(^full|[\d.]+,|,[\d.]+|pct:[\d.]+|[\d.]+,"
                         "[\d.]+|![\d.]+,[\d.]+)")
        },
        "rotate": {
            "ignore": "0",
            "validate": "^[\d.]+$"
        },
        "quality": {
            "ignore": "default",
            "validate": "(native|color|grey|bitonal)"
        },
        "image_format": {
            "ignore": "",
            "validate": "(jpg|png|gif|jp2|jpeg|pdf)"
        }
    },
    "v2": {
        "region": {
            "ignore": "full",
            "validate": "(^full|(pct:)?([\d.]+,){3}([\d.]+))",
        },
        "size": {
            "ignore": "full",
            "validate": ("(^full|[\d.]+,|,[\d.]+|pct:[\d.]+|[\d.]+,"
                         "[\d.]+|![\d.]+,[\d.]+)")
        },
        "rotate": {
            "ignore": "0",
            "validate": "^!?[\d.]+$"
        },
        "quality": {
            "ignore": "default",
            "validate": "(default|color|grey|bitonal)"
        },
        "image_format": {
            "ignore": "",
            "validate": "(jpg|png|gif|jp2|jpeg|pdf)"
        }
    }
}

# Qualities per image mode
IIIF_QUALITIES_PER_IMAGE_MODE = {
    '1': ['default', 'bitonal'],
    'L': ['default', 'gray', 'bitonal'],
    'P': ['default', 'gray', 'bitonal'],
    'RGB': ['default', 'color', 'gray', 'bitonal'],
    'RGBA': ['default', 'color', 'gray', 'bitonal'],
    'CMYK': ['default', 'color', 'gray', 'bitonal'],
    'YCbCr': ['default', 'color', 'gray', 'bitonal'],
    'I': ['default', 'color', 'gray', 'bitonal'],
    'F': ['default', 'color', 'gray', 'bitonal']
}
