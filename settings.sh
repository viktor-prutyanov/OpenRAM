#!/bin/bash

export OPENRAM_ROOT=$PWD
export OPENRAM_HOME="$PWD/compiler"
export OPENRAM_TECH="$PWD/technology"
export PYTHONPATH=$OPENRAM_HOME
export PYTHONPATH="$OPENRAM_HOME:$OPENRAM_TECH/sky130:$OPENRAM_TECH/sky130/custom"

source miniconda/bin/activate
