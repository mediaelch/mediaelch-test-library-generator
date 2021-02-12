#!/usr/bin/env bash

set -Eeuo pipefail
IFS=$'\n\t'

cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1

./download-movie-titles.py --count 1000 --format json --lang en-US ./data/movies_en-US.json
./download-movie-titles.py --count 1000 --format csv --lang en-US ./data/movies_en-US.csv
./download-movie-titles.py --count 1000 --format json --lang de-DE ./data/movies_de-DE.json
./download-movie-titles.py --count 1000 --format csv --lang de-DE ./data/movies_de-DE.csv
