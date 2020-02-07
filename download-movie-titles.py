#!/usr/bin/env python3

import requests
import re
import csv
import argparse
import sys
import os
import json

def process_imdb_list(html):
    # Regex may change if the IMDb source changes
    regex = re.compile('<a href="/title/(tt\d{7,8})/[^"]*"\n>([^<]*)</a>')
    movies = regex.findall(html)
    return list(filter(lambda movie : movie[1] != 'See full summary', movies))

def download_imdb_page(lang, startIndex):
    print("Download next 100 movies in {1} starting at {0}".format(lang, startIndex))
    url = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count={count}&start={start}".format(count=100, start=startIndex)
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept-Language": "{0};{1};q=0.5".format(lang, lang.split('-')[0])
    }
    r = requests.get(url=url, headers=headers)
    return r.text

def download_movie_titles(lang="en-US", numberOfMovies=1000):
    if numberOfMovies > 1000:
        raise Exception("Can't download more than 1000 movies")

    movies = [ ]

    iterations = (numberOfMovies + 99) // 100
    count = 100

    for i in range(iterations):
        start = (i * 100) + 1
        html = download_imdb_page(lang, start)
        movies = movies + process_imdb_list(html)

    return movies

def write_csv(file, movies):
    with open(file, 'w', newline='\n') as outfile:
        w = csv.writer(outfile, delimiter=";")
        w.writerow(["id", "title"])
        for movie in movies:
            w.writerow(movie)

def write_json(file, movies, lang):
    data = {}
    data['lang'] = lang
    data['movies'] = []
    for movie in movies:
        data['movies'].append({
            'imdb_id': movie[0],
            'title': movie[1]
        })

    with open(file, 'w', newline='\n') as outfile:
        json.dump(data, outfile, indent=2)

def main():
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Download list of movies from IMDb')
    parser.add_argument('--count', type=int, default=1000,
                        help='number of movies to download; max 1000')
    parser.add_argument('--format', choices=['csv', 'json'], default='csv',
                        help="Output format (default: csv)")
    parser.add_argument('--lang', default="en-US",
                        help='language for IMDb (format/default: "en-US")')
    parser.add_argument("output", nargs='?', default="movies.csv",
                        help="Output file (default: movies.csv)")
    args = parser.parse_args()
    
    if args.count > 1000:
        print("Cannot download more than 1000 movie titles", file=sys.stderr)
        exit(1)

    # args.output may contain folders that don't yet exist
    basedir = os.path.dirname(args.output)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    movies = download_movie_titles(args.lang, args.count)

    if args.format == "csv":
        write_csv(args.output, movies)
    elif args.format == "json":
        write_json(args.output, movies, args.lang)
    
    print('Done. Movie titles written to "{0}"'.format(args.output))

if __name__ == "__main__":
    main()
