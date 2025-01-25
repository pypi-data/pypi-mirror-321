#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

### Folder ###

from ..utils.set_logging import get_logger

# Define
logger = get_logger(__name__.split('.')[-1])

# Local
from . import create, update, delete, move, doc, info
from ..utils.show import show_response

def folder(
    params,
)-> None:
    """Folder Management
    - Create, Delete, Update, Get

    Parameters
    ----------
    name : Text
        Folder name
    pfid : Text
        Parent folder ID
    """

    # Greeting
    logger.info("Folder management starts.")

    if params.create:
        url, response = create(params)
    elif params.update:
        url, response = update(params)
    elif params.move:
        url, response = move(params)
    elif params.doc:
        url, response = doc(params)
    elif params.delete:
        url, response = delete(params)
    elif params.get:
        url, response = info(params)
    else:
        logger.error("Please select a function!")
        return

    if url is None or response is None:
        logger.error("Please check the parameters.")
        return

    if params.verbose:
        show_response(
            title="Folder Management",
            url=url,
            response=response,
       )