#!/usr/bin/env python3

import argparse
import sys
import os
import json
import random
from pathlib import Path
import shutil

def randomize_movie_title(title):
    # Neither performant or nice but we simply replace one whitespace with
    # another character randomly.
    for i in range(5):
        r = random.randrange(0, 4)
        if r == 0:
            title = title.replace(' ', '.', 1)
        if r == 1:
            title = title.replace(' ', '_', 1)
        if r == 2:
            title = title.replace(' ', '-', 1)
        if r == 3:
            pass
    return title

def read_movies_from_json(file):
    with open(file, 'r') as f:
        movies = json.load(f)
    return movies

def create_movie_files(title):
    # TODO: Actually copy files or use ln -s
    Path(os.path.join(title, "movie.mov")).touch()

def create_movie_library(basedir, movies):
    for movie in movies['movies']:
        movie_dir = os.path.join(basedir, '' + movie['title'])
        movie_dir = randomize_movie_title(movie_dir)

        if not os.path.exists(movie_dir):
            os.makedirs(movie_dir)

        create_movie_files(movie_dir)

def main():
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Create a fake library for testing purposes')
    parser.add_argument('--movies',
                        help='Which movie list to use')
    parser.add_argument("output", default="library/movies",
                        help="Output folder")
    parser.add_argument('--clean', dest='clean', action='store_true',
                        help="Clean the folder before generating movie files")
    parser.set_defaults(feature=False)
    args = parser.parse_args()
    
    if args.movies == "":        
        print("Require a movie JSON file", file=sys.stderr)
        exit(1)

    basedir = args.output
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    elif args.clean:
        shutil.rmtree(basedir, ignore_errors=True)
        os.makedirs(basedir)

    movies = read_movies_from_json(args.movies)
    create_movie_library(basedir, movies)

    print('Done. Created movie library in "{0}"'.format(args.output))

if __name__ == "__main__":
    main()
