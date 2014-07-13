__author__ = 'chris'
import glob
import os

def latest(num=1, path="."):
    files_with_dates = []
    files = glob.glob(os.path.join(path, "*"))
    latest_files = []
    for fn in files:
        files_with_dates.append((os.path.getmtime(fn), os.path.abspath(fn)))
    files_with_dates.sort()
    for file_info in files_with_dates[-num:]:
        latest_files.append(file_info[1])
    latest_files.reverse()
    return latest_files