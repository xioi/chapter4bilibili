#!/usr/bin/env python

import os
import re
import sys
import subprocess

def read_chapters(path_to_video):
    try:
        with open(os.devnull, 'w') as tempf:
            subprocess.check_call(["ffprobe", "-h"], stdout=tempf, stderr=tempf)
    except FileNotFoundError:
        raise IOError('ffprobe not found.')
    
    cmd = ["ffprobe", "-show_chapters", path_to_video]
    result = subprocess.run(cmd, capture_output=True)
    chapters_text = result.stdout.decode()

    pattern = re.compile(r"""\[CHAPTER\]
id=\d+
time_base=\d+/\d+
start=\d+
start_time=(\d+)\.\d+
end=\d+
end_time=\d+\.\d+
TAG:title=([^\n]*)
\[/CHAPTER\]""")
    matches = pattern.findall(chapters_text)

    # print()
    # print(matches)
    return matches

def format_time(seconds):
    # 1. 算出小时，和剩下的秒数
    h, remainder = divmod(seconds, 3600)
    # 2. 从剩下的秒数里算出分钟和秒
    m, s = divmod(remainder, 60)
    
    # :02d 确保小时、分钟、秒都是两位数，不足补0
    return f"{h:02d}:{m:02d}:{s:02d}"

def format_and_print(matches):
    for chapter in matches:
        print(format_time(int(chapter[0])), chapter[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error: missing or overwhelmed arguments")
    else:
        # read_chapters(sys.argv[1])
        format_and_print(read_chapters(sys.argv[1]))