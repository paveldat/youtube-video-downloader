# Youtube Video Downloader

## How to install
1. Clone this repository on your computer
`https://github.com/paveldat/youtube-video-downloader.git`
2. Install all the requirements
`pip install -r requirements.txt`
3. Run the usage
`python youtube_downloader.py -h`

## Advantages
1. This is an API that can easily be implemented into your project
2. Supports any links from Youtube
3. It has argparse for convenient use from the console
4. Accepts all possible arguments

## Usage `python youtube_downloader.py -h`
```shell
usage: youtube_downloader.py [-h] [-o output_path] [-f filename] [-p filename_prefix] [-s] [-t timeout] [-m max_retries] url

positional arguments:
  url                   URL to the video

options:
  -h, --help            show this help message and exit
  -o output_path, --output-path output_path
                        Output path for writing media file. If one is not specified, defaults to the current working directory.
  -f filename, --filename filename
                        Output filename (stem only) for writing media file. If one is not specified, the default filename is used.
  -p filename_prefix, --filename-prefix filename_prefix
                        A string that will be prepended to the filename. For example a number in a playlist or the name of a series. If one is not specified, nothing will be prepended. This is separate from
                        filename so you can use the default filename but still add a prefix.
  -s, --skip-existing   Skip existing files, defaults to True.
  -t timeout, --timeout timeout
                        Request timeout length in seconds. Uses system default.
  -m max_retries, --max-retries max_retries
                        Number of retries to attempt after socket timeout. Defaults to 0.
```
