#!/usr/bin/env bash

problem_name=$1
if [ ! -d "$problem_name" ]; then
    mkdir -p $problem_name
    echo "[MAK] creating directory $problem_names"
fi

templates_dir=$PWD/__templates

# add files that should be added as sym link to the problem directory.
declare -a files=("case.sh" "verify.sh")
for template in "${files[@]}"; do
    sym_link=$problem_name/$template
    if [ ! -f "$sym_link" ]; then
        ln -s $templates_dir/$template $sym_link
        echo "[SYM] created symlink for $template"
    fi
done

declare -a files=("solution.py")
for template in "${files[@]}"; do
    cpy_file=$problem_name/$template
    if [ ! -f "$cpy_file" ]; then
        cp $templates_dir/$template $cpy_file
        echo "[COP] copied template file for $template"
    fi
done

echo "boostrapping complete."
