# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from datetime import datetime
import glob
import inspect
import json
import logging
import os
import sys
import time

from fabric.api import task, local


FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)


# ##############################################################
# # Common
# ##############################################################
# def get_version():
#     logger.info('Get version')
#     with open('package.json') as fin:
#         config = json.load(fin)

#         version = config['version']

#         return version


# ##############################################################
# # Docker
# ##############################################################
# PRIVATE_REGISTRY_URL = ''
# DOCKER_IMAGE = 'freqtrade'

DOCKERFILE = 'Dockerfile'
# # DOCKERFILE_DEV = 'Dockerfile.dev'
DOCKERFILE_DEV = 'Dockerfile'


# def get_docker_image_path():
#     version = get_version()
#     docker_image_path = \
#         '{PRIVATE_REGISTRY_URL}/{DOCKER_IMAGE}:{VERSION}'.format(
#             PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL,
#             DOCKER_IMAGE=DOCKER_IMAGE,
#             VERSION=version
#         )

#     return docker_image_path


# def get_docker_image_path_dev():
#     # version = get_version()
#     version = 0.1
#     version = '{}-dev'.format(version)
#     docker_image_path = '{DOCKER_IMAGE}:{VERSION}'.format(
#         DOCKER_IMAGE=DOCKER_IMAGE,
#         VERSION=version
#     )

#     return docker_image_path


@task
def docker_build_dev():
    logger.info('Build Docker Image')
    # docker_image_path = get_docker_image_path_dev()
    docker_image_path = 'freqtrade'

    build_command = \
        'docker build --tag={DOCKER_IMAGE_PATH} --file={DOCKERFILE} .'.format(
            DOCKER_IMAGE_PATH=docker_image_path,
            DOCKERFILE=DOCKERFILE_DEV
        )

    local(build_command)


# ##############################################################
# # Dev
# ##############################################################
@task
def start_freqtrade_dev():
    command = """docker run -it --rm \
        --name freqtrade \
        -v `pwd`/data/config.json:/freqtrade/config.json \
        -v `pwd`/data/tradesv3.sqlite:/freqtrade/tradesv3.sqlite \
        freqtrade
        """

    local(command)

