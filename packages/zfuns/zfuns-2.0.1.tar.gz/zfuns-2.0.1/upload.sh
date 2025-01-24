#!/bin/bash

git add .
git commit -m $1

python -m pip install --upgrade pip setuptools wheel twine ez_setup
python setup.py sdist
python -m twine upload dist/*
git push --tags

rm -rf dist
rm -rf build
rm -rf zfuns.egg-info