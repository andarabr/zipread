import os
import zipfile
from datetime import datetime

path = 'C:\\Users\\Breygas Andara\\Documents\\Project\\ZIPSHB\\zips'

os.chdir(path)
print('---------------------------------')

for subdir, dirs, files in os.walk(path):
    for file in files:

        with zipfile.ZipFile(file) as z:
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f'Reading File : {file}')
            if len(z.namelist()) < 4:
                print(f'ERR : File count < 4 ({len(z.namelist())})')
            else:
                for filename in z.namelist():
                    print(filename)
        print('---------------------------------')