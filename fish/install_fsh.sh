#!/bin/bash
WORK_DIR=$PWD
cd /tmp
git clone https://github.com/ashhhleyyy/fsh.git
cd /tmp/fsh
./setup.sh
cd $WORK_DIR
rm -rf /tmp/fsh
