#!/bin/sh

# get the file name from the argument list
FILE=$1

# change the extension from md to html
HTML_FILE=${FILE%.md}.html 

pandoc \
    ${FILE} \
    -H ./iub_style.html \
    -c "//assets.iu.edu/web/3.3.x/css/iu-framework.min.css" \
    --standalone \
    --mathjax \
    -o ./${HTML_FILE}

#    --mathjax=http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML \
