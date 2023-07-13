import time

def progress_bar(label, total, progress):
    bar_length = 30
    filled_length = int(bar_length * progress / total)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f'{label} [{bar}] {progress}/{total}', end='\r')

# Usage:
total_items = 100
for i in range(total_items + 1):
    progress_bar('Progress:', total_items, i)
    time.sleep(0.1)

