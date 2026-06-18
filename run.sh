#! /bin/bash
set -e

python -m uvicorn --host 0.0.0.0 main:app
