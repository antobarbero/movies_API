#!/bin/sh

# Adds pre-commit hook into git hooks directory
ln -b -f hooks/pre-commit .git/hooks/pre-commit
if [ $? = 0 ]; then
    printf "The hooks have been installed correctly.\n";
fi
