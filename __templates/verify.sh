#!/usr/bin/env bash


for f in *.in; do
	[ -f "$f" ] || break
	out=$(pypy solution.py $f)
	i="${f%.*}"
	if [[ $(< $i.out) == $out ]]; then
		echo "Test $i...OK"
	else
		echo "Test $i...WRONG (expected: $(<$i.out), actual: $out)"
	fi
done