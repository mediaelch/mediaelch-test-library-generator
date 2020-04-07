#!/usr/bin/env python3

import requests
import re
import csv
import argparse
import sys
import os
import json

def stringToBool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def download_movie(url, target_dir):
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    r = requests.get(url=url, headers=headers)
    filename = url.split("/")[-1]
    targetFilename = "{dir}/{name}".format(dir=target_dir, name=filename)
    with open(targetFilename, 'wb') as f:
        f.write(r.content)

def read_samples(filePath):
    with open(filePath) as f:
        samples = json.load(f)
    return samples

def filter_samples(samples, filter):
    filterRegEx = re.compile(filter)
    videos = samples["video"]
    if videos != None:
        videos[:] = [v for v in videos if filterRegEx.search(v["name"]) != None]
    return samples

def print_sample_list(samples):
    videos = samples["video"]
    if videos != None:
        print("Video Files:")
        for video in videos:
            print("{name: <40}: {url}".format(name=video["name"], url=video["url"]))

def main():
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Download sample video files')
    parser.add_argument('--filter',
                        help='filter the list of samples using the name')
    parser.add_argument('--input', default='data/media_samples.json',
                        help='Which sample json file to use (default data/media_samples.json)')
    parser.add_argument('--list', dest='list', action='store_true',
                        help="Only list the files and do not download them")
    parser.add_argument("output", nargs='?', default='media/movies',
                        help="Output directory (default: ./media/movies)")
    args = parser.parse_args()

    # args.output may not exist, yet
    if not os.path.exists(args.output):
        print("Output directory must exist, cannot find: {dir}".format(dir=args.output))
        exit(1)

    samples = read_samples(args.input)
    if args.filter != None:
        print("Using filter: {filter}".format(filter=args.filter))
        samples = filter_samples(samples, args.filter)
    
    if args.list:
        print_sample_list(samples)
        return

    print('Done. Downloaded video files.')

if __name__ == "__main__":
    main()
