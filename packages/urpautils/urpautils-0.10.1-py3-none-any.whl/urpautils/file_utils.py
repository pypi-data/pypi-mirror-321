"""Module containing universal functions for file operations that can be used with urpa robots"""

import datetime
import glob
import json
import logging
import os
import shutil
import time
import traceback

from typing import Optional

from .universal import timestamp

logger = logging.getLogger(__name__)


def remove_dir(path: str) -> None:
    """Removes a directory

    :param path:    path
    :return:        None
    """
    if os.path.isdir(path):
        logger.info(f"Removing directory '{path}'")
        shutil.rmtree(path)


def remove(path: str) -> None:
    """Removes a file

    :param path:    path
    :return:        None
    """
    if os.path.isfile(path):
        os.remove(path)


def move(file_path: str, destination: str) -> None:
    """Moves a file

    :param file_path:    path
    :param destination:  destination path
    :return:             None
    """
    if os.path.isfile(file_path):
        shutil.move(file_path, destination)


def copy(src: str, dest: str) -> None:
    """Copies a file

    :param src:   source path
    :param dest:  destination path
    :return: None
    """
    shutil.copyfile(src, dest)


def remove_files_older_than(dir_path: str, days: int) -> None:
    """Removes all files in a directory that are older than 'days' days

    :param dir_path:     path
    :param days:         number of days
    :return:             None
    """
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            # file age in seconds
            file_age = time.time() - os.stat(file_path).st_mtime
            # file age in days
            file_age /= 86400
            if file_age > days:
                logger.info(f"Removing '{file_path}' because it is older than '{days}' days")
                remove(file_path)


def write_txt_file(file_name: str, content: str, mode: str = "w", encoding: str = "utf-8") -> None:
    """Writes a text file

    :param file_name:    path
    :param content:      string to write
    :param mode:         mode of writing (writing, appending, ...)
    :param encoding:     encoding to use
    :return:             None
    """
    possible_modes = ("w", "a", "w+", "a+")
    if not mode in possible_modes:
        raise ValueError(f"Invalid write mode '{mode}'. Please use one of the following: '{possible_modes}'")
    with open(file_name, mode, encoding=encoding) as txt_file:
        txt_file.write(content)


def read_txt_file(file_name: str, encoding: str = "utf-8") -> str:
    """Reads a text file

    :param file_name:    path
    :param encoding:     encoding to use
    :return:             str content
    """
    with open(file_name, "r", encoding=encoding) as txt_file:
        return txt_file.read()


def read_json_file(file_name: str, encoding: str = "utf-8") -> dict:
    """Reads a json file

    :param file_name:    path
    :param encoding:     encoding to use
    :return:             dict content
    """
    with open(file_name, "r", encoding=encoding) as json_file:
        return json.load(json_file)


class Helper:
    """Class for reading and writing helper text files"""

    def __init__(self, file_name: str, init_value: int = 0) -> None:
        """Init. Creates file if it does not exist

        :param file_name:      file name
        """
        self.file_name = file_name
        if not os.path.isfile(file_name):
            logger.info(f"Creating '{file_name}' file")
            self.write(init_value)

    def get(self) -> int:
        """Reads the file and returns its content as integer

        :return:    int
        """
        with open(self.file_name) as helper_file:
            return int(helper_file.read())

    def write(self, value: int) -> None:
        """Writes integer 'value' to the file

        :param value:    integer
        :return:         None
        """
        if not isinstance(value, int):
            logger.error(f"Value '{value}' is not an integer")
            raise ValueError(f"Value '{value}' is not an integer")
        with open(self.file_name, "w") as helper_file:
            helper_file.write(str(value))

    def increment(self, increment: int = 1) -> int:
        """Increments number in file by 'increment'

        :param increment:    how much to increment by
        :return:             number after incrementing
        """
        if not isinstance(increment, int):
            logger.error(f"Value '{increment}' is not an integer")
            raise ValueError(f"Value '{increment}' is not an integer")
        new_value = self.get() + increment
        self.write(new_value)
        return new_value

    def delete(self) -> None:
        """Removes the file

        :return:       None
        """
        os.remove(self.file_name)


def archivate_file(
    source_file: str,
    destination_path: str,
    prefix_timestamp_format: Optional[str] = None,
    force_rewrite: bool = False,
) -> str:
    """Moves 'source_file' to 'destination_path' and if selected adds timestamp prefix to its name

    :param source_file:              path to file
    :param destination_path:         path to directory
    :param prefix_timestamp_format:  format of the timestamp prefix. If None no prefix is added
    :param force_rewrite:            bool - if destination file already exists it is rewriten if True
    :return:                         string - path to the new file
    """
    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"File '{source_file}' does not exist")

    file_name = os.path.basename(source_file)
    prefix = timestamp(prefix_timestamp_format) if prefix_timestamp_format else ""
    file_name = f"{prefix}{file_name}"
    output_file_path = os.path.join(destination_path, file_name)

    if os.path.isfile(output_file_path):
        if force_rewrite:
            logger.info(f"Rewriting file '{output_file_path}'")
        else:
            raise FileExistsError(
                f"Cannot write file '{output_file_path}' because it already exists. If you want to rewrite it use 'force_rewrite = True'"
            )

    move(source_file, output_file_path)
    return output_file_path


def prepare_dir(dir_name: str) -> None:
    """Creates directory dir_name if it does not exist

    :param dir_name:      path
    :return:              None
    """
    if not os.path.exists(dir_name):
        logger.info(f"Creating new directory '{dir_name}'.")
        os.mkdir(dir_name)


def _get_main_file_name() -> str:
    """Gets name of the main file from stack trace

    :return:    basename of the main file without an extension
    """
    for line in traceback.format_stack():
        if "File" in line and ".py" in line:
            # first line that contains 'File' and '.py' is the main file
            # e.g. 'File "c:\path\to\file.py", line 12, in <module>'
            break
    # parse only the path part from the string
    indexes_of_file_path = [i for i, x in enumerate(line) if x == '"']
    main_file_path = line[indexes_of_file_path[0] + 1 : indexes_of_file_path[1]]
    main_file_name = os.path.basename(main_file_path)
    return os.path.splitext(main_file_name)[0]


def _get_error_screenshot_path(screenshot_format, current_log_dir, offset) -> str:
    """Gets path of latest+offset image in current_log_dir

    :param screenshot_format:    png, or bmp
    :param current_log_dir:      directory containing the screenshots
    :param offset:               which file to copy, starting from last one
    :return:                     str path to file
    """
    if not current_log_dir:
        current_log_dir = os.path.join("log", f"{_get_main_file_name()}_{timestamp('%Y-%m-%d')}")
    # remove dots from screenshot format in case user provided ".png" instead of "png"
    screenshot_format = screenshot_format.replace(".", "")
    error_imgs = sorted(glob.glob(f"{current_log_dir}\\*.{screenshot_format}"), key=os.path.getmtime)
    return error_imgs[-1 - offset]


def copy_error_img(
    output_dir: str,
    output_file_name: Optional[str] = None,
    screenshot_format: str = "png",
    current_log_dir: str = "",
    offset: int = 0,
) -> str:
    r"""Finds 'screenshot_format' file in the 'current_log_dir' and copies it to 'output_dir'.
    'offset' is used to determine which file to copy starting from the last
        offset=0 -> last file, offset=1 -> second last file, ...
    Files are ordered by their age in descending order. Last file (offset 0) is always the newest one

    :param output_dir:           path
    :param output_file_name:     optional name of the copied file. Name of the original is used if none provided
    :param screenshot_format:    png, or bmp
    :param current_log_dir:      directory containing the screenshots. Defaults to 'log\main_module_name_YYYY-MM-DD'
    :param offset:               which file to copy, starting from last one
    :return:                     str path to copied file
    """
    error_img_path_log = _get_error_screenshot_path(screenshot_format, current_log_dir, offset)
    if not output_file_name:
        # if no output file name was provided, use name of the original image
        output_file_name = os.path.basename(error_img_path_log)
    else:
        output_file_name += f".{screenshot_format}"
    error_img_path_output = os.path.join(output_dir, output_file_name)
    shutil.copyfile(error_img_path_log, error_img_path_output)
    return error_img_path_output


def add_timestamp_to_filename(abs_path: str, timestamp_format: str = "%Y-%m-%d") -> str:
    """
    This function takes an absolute file path and a timestamp format as inputs.
    It adds a timestamp to the file name and returns the new absolute file path.

    :param abs_path: The absolute path to the file
    :param timestamp_format: The format of the timestamp to be added (default is '%Y-%m-%d')
    :return: The new absolute path with the timestamp added to the file name
    """
    path, base = os.path.split(abs_path)
    filename, ext = os.path.splitext(base)
    timestamp = datetime.datetime.now().strftime(timestamp_format)
    new_filename = f"{timestamp}_{filename}{ext}"
    return os.path.join(path, new_filename)
