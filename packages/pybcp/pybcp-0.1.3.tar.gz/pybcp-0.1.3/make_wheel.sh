#!/bin/bash

pip install build auditwheel patchelf

python -m build --wheel
auditwheel repair --plat=manylinux_2_34_x86_64 ./dist/pybcp-*.whl
