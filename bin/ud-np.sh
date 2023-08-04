#!/bin/bash
cd $HOME/Code/github/sbaldasty/sbaldasty.github.io
NAME=`date +"%Y-%m-%d"`
hugo new --kind notebook-bundle notebook/$NAME
vim +6 content/notebook/$NAME/index.md

