#!/bin/bash

jupyter-notebook --no-browser --ip 0.0.0.0 --allow-root &
uvicorn rest:app --reload
