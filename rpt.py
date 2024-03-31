import os
import random

from datetime import timedelta
from tinytag import TinyTag


def random_time(duration):
    time_in_seconds = random.uniform(0, duration.total_seconds())
    return duration - timedelta(seconds=time_in_seconds)


def format_time_from_timedelta(timedelta_string):
    parts = timedelta_string.split(":")
    return f"{int(parts[1])}:{int(parts[2].split('.')[0]):02d}"


def get_files():
    music_files_directory = os.path.join(os.getcwd(), "files")

    for root, _, files in os.walk(music_files_directory):
        for name in files:

            music_file = TinyTag.get(os.path.join(root, name))

            m, s = divmod(music_file.duration, 60)
            random_time_choice = random_time(timedelta(minutes=m, seconds=s))
            play_from_this_time = format_time_from_timedelta(str(random_time_choice))

            print(f"[{music_file.title}, Duration: {'%d:%02d' % (m, s)}, Play from: {play_from_this_time}]")


if __name__ == '__main__':
    get_files()
