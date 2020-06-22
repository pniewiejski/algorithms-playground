#!/bin/sh
# I'm using prettier https://prettier.io
# you can install it by: npm install -g prettier 
set -xe
if [ $# -eq 0 ]; then
    prettier --print-width 100 --prose-wrap always --write "./**/*.md"
    echo $?
else
    prettier --print-width 100 --prose-wrap always --check "./**/*.md"
fi
