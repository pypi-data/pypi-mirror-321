# Copyright (C) 2024 qBraid
#
# This file is part of the qBraid-SDK
#
# The qBraid-SDK is free software released under the GNU General Public License v3
# or later. You can redistribute and/or modify it under the terms of the GPL v3.
# See the LICENSE file in the project root or <https://www.gnu.org/licenses/gpl-3.0.html>.
#
# THERE IS NO WARRANTY for the qBraid-SDK, as per Section 15 of the GPL v3.

"""
Amazon Braket AHS conversions

.. currentmodule:: qbraid.transpiler.conversions.braket_ahs

Functions
----------

.. autosummary::
   :toctree: ../stubs/

   bloqade_to_braket_ahs

"""
from .braket_ahs_extras import bloqade_to_braket_ahs

__all__ = ["bloqade_to_braket_ahs"]
