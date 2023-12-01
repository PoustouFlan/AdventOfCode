#! /bin/sh

## Retrieve requested year/day from command-line arguments.
## Uses current year/day if not specified

year=$(date '+%Y')
day=$(date '+%-d')

if [ "$#" -ge 1 ]; then
    day="$1"
fi
if [ "$#" -ge 2 ]; then
    year="$2"
fi

## Creates the directory YEAR/DAY if it does not yet exist

mkdir "$year" 2> /dev/null
mkdir "$year/$day" 2> /dev/null

## Calls the start.py script to retrieve challenge input in background

# Needs the `requests` python package
# nix-shell -p python3Packages.requests -- run "python3 start.py $day $year" &
python3 start.py "$day" "$year" &

## Copies the template and launch the editor

cp template.py "$year/$day/solve.py"
cd "$year/$day"
$EDITOR solve.py
