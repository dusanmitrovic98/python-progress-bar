import time

def progress_bar(label, total, progress):
    bar_length = 30
    filled_length = int(bar_length * progress / total)
