#!/usr/bin/env bash

name=0
if [[ -e $name.in || -L $name.in ]] ; then
    i=0
    while [[ -e $i.in || -L $i.in ]] ; do
        let i++
    done
    name=$i
fi
touch -- "$name".in "$name".out