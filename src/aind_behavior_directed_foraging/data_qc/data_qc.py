"""Data quality check definitions for the directed-foraging task."""

import logging
from typing import List

from contraqctor import contract, qc

logger = logging.getLogger(__name__)


def make_qc_runner(dataset: contract.Dataset) -> qc.Runner:
    """
    Create a QC runner with checks specific to the directed-foraging task.

    Args:
        dataset: The loaded dataset to run QC checks on.

    Returns:
        A configured QC runner with all registered checks.
    """
    _runner = qc.Runner()
    # TODO : Add qc tests here

    return _runner
