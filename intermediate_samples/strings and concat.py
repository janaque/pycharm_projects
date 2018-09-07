
import os

location_of_files = 'C:\\Users\\julius.anaque\\PycharmProjects\\pycharmprojects'
file_name = 'samplefile'

#print(location_of_files + '\\' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())




