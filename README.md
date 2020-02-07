# Test Library Generator

Python scripts to generate a media library useful for testing.
Furthermore, pre-downloaded movie titles are listed in `./data`.

## Scripts

### Download Movie Titles from IMDb

```sh
# Requirements
pip3 install --user requests

# Show all options
./download-movie-titles.py --help

# Example
./download-movie-titles.py --count 1000 --lang de-DE --format json data/movies.json
```

### Download Media Files (Samples)
The library generator has the option to copy actual video files when creating a
library instead of create empty video files. We have a list of media files that
you can download which was gathered from the Kodi Wiki page
["Samples"][wiki_samples].

```sh
# TODO
```

[wiki_samples]: https://kodi.wiki/view/Samples
