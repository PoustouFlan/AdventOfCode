#! /bin/sh

year=$(date '+%Y')
day=$(date '+%-d')

if [ "$#" -ge 1 ]; then
    day="$1"
fi
if [ "$#" -ge 2 ]; then
    year="$2"
fi

mkdir "$year" 2> /dev/null
mkdir "$year/$day" 2> /dev/null
nix-shell -p python310Packages.requests --run "python start.py $day $year &"

cp template.py "$year/$day/solve.py"
cd "$year/$day"
vim solve.py
