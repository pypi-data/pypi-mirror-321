#!/bin/bash
##
## Copyright 2018-2024 Fragment Contributors
## SPDX-License-Identifier: Apache-2.0
##


############ COMMANDS NEEDED TO UPLOAD DATA TO PiPy
# TODO: Integrate this with the CI Pipeline

python -m build

# TESTING
# python3 -m twine upload --repository testpypi dist/*

# PRODUCTION
python -m twine upload --repository pypi dist/*