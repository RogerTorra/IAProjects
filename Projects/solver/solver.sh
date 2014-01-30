#!/bin/bash
echo Solver Fu Malik algorithm:
echo ++++++++++++++++++++++++++
ulimit -t $2 python maxSAT.py $1
exit 0