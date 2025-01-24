"""App Tasks"""

# Standard Library
import logging

# Third Party
from celery import shared_task

logger = logging.getLogger(__name__)

# Create your tasks here


# ProdOPS Task
@shared_task
def ProdOPS_task():
    """ProdOPS Task"""

    pass
