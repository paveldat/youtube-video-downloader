"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import sys
import argparse
from pathlib import Path
from enum import IntEnum
from pytube import YouTube


class DownloaderStatus(IntEnum):
    SUCCESS = 0
    FAILED = 130


class YoutubeDownloader:
    """
    Downloads video from Youtube
    """

    @staticmethod
    def download(url: str,
                 output_path: [str, Path] = None,
                 filename: str = None,
                 filename_prefix: str = None,
                 skip_existing: bool = True,
                 timeout: int = None,
                 max_retries: int = 0) -> int:
        """
        Downloads video from Youtube by url.

        Args:
            * url - URL to the video.
            * output_path - Output path for writing media file. If one is not
                            specified, defaults to the current working
                            directory.
            * filename - Output filename (stem only) for writing media file.
                         If one is not specified, the default filename
                         is used.
            * filename_prefix -
                            A string that will be prepended to the filename.
                            For example a number in a playlist or
                            the name of a series. If one is not specified,
                            nothing will be prepended. This is separate
                            from filename so you can use the default filename
                            but still add a prefix.
            * skip_existing - Skip existing files, defaults to True.
            * timeout - Request timeout length in seconds. Uses system default.
            * max_retries - Number of retries to attempt after socket timeout.
                            Defaults to 0.

        Returns:
            * 0 - Video was downloaded successfuly.
            * 130 - An error has occured.
        """

        try:
            print(f'\033[34m Trying to download video from: {url} \033[0m')
            youtubeObject = YouTube(url)
            youtubeObject = youtubeObject.streams.get_highest_resolution()

            print('\033[34m Using: \033[0m')
            print(f'\033[34m output_path: {output_path} \033[0m')
            print(f'\033[34m filename: {filename} \033[0m')
            print(f'\033[34m filename_prefix: {filename_prefix} \033[0m')
            print(f'\033[34m skip_existing: {skip_existing} \033[0m')
            print(f'\033[34m timeout: {timeout} \033[0m')
            print(f'\033[34m max_retries: {max_retries} \033[0m')

            youtubeObject.download(
                output_path=output_path,
                filename=filename,
                filename_prefix=filename_prefix,
                skip_existing=skip_existing,
                timeout=timeout,
                max_retries=max_retries)
            print('\033[1;91m Downloading completed. \033[1;m')
            return DownloaderStatus.SUCCESS.value
        except Exception as ex:
            print(f'\033[1;91m Exception has occured: {str(ex)} \033[1;m')
            return DownloaderStatus.FAILED.value


def main():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('url', type=str, help='URL to the video.')
    arg_parse.add_argument('-o', '--output-path', metavar='output_path',
                           default=None, type=str,
                           help='Output path for writing media file.\
                                 If one is not specified, defaults\
                                 to the current working directory.'
                           )
    arg_parse.add_argument('-f', '--filename', metavar='filename',
                           default=None, type=str,
                           help='Output filename (stem only) for writing\
                                 media file. If one is not specified, the\
                                 default filename is used.')
    arg_parse.add_argument('-p', '--filename-prefix', type=str,
                           metavar='filename_prefix', default=None,
                           help='A string that will be prepended to the\
                                 filename. For example a number in a\
                                 playlist or the name of a series.\
                                 If one is not specified, nothing\
                                 will be prepended. This is separate\
                                 from filename so you can use the default\
                                 filename but still add a prefix.')
    arg_parse.add_argument('-s', '--skip-existing',
                           action='store_false', default=True,
                           help='Skip existing files, defaults to True.')
    arg_parse.add_argument('-t', '--timeout', metavar='timeout',
                           type=int, default=None,
                           help='Request timeout length in seconds.\
                                 Uses system default.')
    arg_parse.add_argument('-m', '--max-retries', metavar='max_retries',
                           type=int, default=0,
                           help='Number of retries to attempt after\
                                 socket timeout. Defaults to 0.')
    args = arg_parse.parse_args()

    return YoutubeDownloader.download(
                url=args.url,
                output_path=args.output_path,
                filename=args.filename,
                filename_prefix=args.filename_prefix,
                skip_existing=args.skip_existing,
                timeout=args.timeout,
                max_retries=args.max_retries
            )


if __name__ == '__main__':
    sys.exit(main())
