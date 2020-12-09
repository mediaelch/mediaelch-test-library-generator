**Heavily work in progress!**

# Test Library Generator

Python scripts to generate a media library useful for testing.
Furthermore, pre-downloaded movie titles are listed in `./data`.

## About

Kodi developers must test the application thoroughly.  Having a library to test
Kodi on makes it a lot easier.  This project targets Kodi-, scraper- and media
manager developers to make their life a bit easier by providing scripts to
generate a test ("fake") media library.

The generated library can be configured to follow certain naming conventions,
have non-readable files, minimal or corrupt NFO files, etc.

*Disclaimer:*  
This repository does not contain any media files nor does it contain URLs to
pirated or otherwise illegal movies.

## Setup Development Environment

### Using pipenv (Recommended)
To create the virtual environment:
```sh
pipenv install
```

Subsequently, to activate the virtual environment:
```sh
pipenv shell
```

### Without pipenv
```sh
pip install --user -r requirements.txt
```

## Scripts

This repository consists of 3 main scripts:

 1. `download-movie-titles.py`
 2. `download-video-samples.py`
 3. `create-library.py`

See the following section for further details.

### Download Movie Titles from IMDb

By using IMDb Top 1000 list of movies we can produce CSV and JSON files that
list all of them. The directory `data` already contains the list in some
languages so that you don't have to download the list yourself.

The script `download-movie-titles.py` is rather easy to use:

```sh
# Show all options
./download-movie-titles.py --help

# Example:
# Load all movie titles in German an store them as a JSON file.
./download-movie-titles.py --count 1000 --lang de-DE --format json data/movies.json
```

### Download Media Files (Samples)

The library generator has an option to copy actual video files when creating a
library instead of create empty "fake" video files.  This repository contains a
list of URLs to sample media files that you can download which were gathered
from the Kodi Wiki page ["Samples"][wiki_samples].

Most files are movies from the [Blender Open Movies][blender] project and are
licensed under Creative Commons licenses.

To download sample files, use the script `download-video-samples.py`.

```sh
# Show all options
./download-video-samples --help

# Example:
# Download the sample files and store them in the "common" directory.
./download-video-samples ./media/common/
```

### Generate a Fake Library

```sh
# Show all options
./download-video-samples --help

# Example:
# Download the sample files and store them in the "common" directory.
./download-video-samples ./media/common/
```

[wiki_samples]: https://kodi.wiki/view/Samples
[blender]: https://www.blender.org/about/projects/
