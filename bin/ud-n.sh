#!/bin/bash
cd $HOME/Code/github/sbaldasty/sbaldasty.github.io
DATE=`date +"%Y-%m-%d"`
echo -n "Enter a title: "
read TITLE
FILE=content/notebook/$DATE/$1.md
touch $FILE
echo "---" >> $FILE
echo "title: $TITLE" >> $FILE
echo "topics: []" >> $FILE
echo "---" >> $FILE
echo >> $FILE
echo >> $FILE
vim +6 $FILE
