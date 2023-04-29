import os
import webbrowser
import time

tag = 'penn'
basepath = f'final-project\\data-{tag}\\'
utilpath = f'final-project\\util\\GRACE-{tag}.txt'

# Download all files from the GRACE data website
# Phenomenal caching strategy John
print("downloading files...")
file1 = open(utilpath, 'r')
lines = file1.readlines()
for line in lines:
    url = line.strip()
    webbrowser.open(url)
    time.sleep(1)
print("finished downloading files")

# Wait for the download to finish
time.sleep(5)

# Rename all files in the data folder to .nc4
# stupid fucking circ downloads 
print("renaming files...")
for filename in os.listdir(basepath):
    try:
        filepath = basepath + filename
        base = os.path.splitext(filepath)[0]
        os.rename(filepath, base + '.nc4')
    except:
        pass

print("finished renaming files")