#! /bin/bash

DAY=0

print_usage() {
   echo "Generate the aws-export and version file"
   echo
   echo "Syntax: add-day [-d|h]"
   echo "options:"
   echo "d     specify day"
   echo "h     Print this Help"
   echo
}

while getopts 'dh' flag; do
  case "${flag}" in
    d) DAY=$2 ;;
    h) print_usage
       exit 1 ;;
  esac
done

echo $DAY
mkdir day${DAY}
cp ./scripts/template-data/dayX-part1.py day${DAY}/day${DAY}-part1.py
cp ./scripts/template-data/dayX-part1.py day${DAY}/day${DAY}-part2.py
cd day${DAY}
touch test.txt