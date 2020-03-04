#!/bin/zsh

export PATH=$PATH:~/Library/Python/3.7/bin
export FLASK_ENV=development
env FLASK_APP=mtf.py flask run
