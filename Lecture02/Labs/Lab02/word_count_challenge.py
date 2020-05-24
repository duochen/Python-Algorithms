import pathlib
import os

def wordcount(fname):  
     pass

##########################################
current_dir = pathlib.Path(__file__).parent.absolute()
file_name = 'alice.txt'
file_full_path = os.path.join(current_dir, file_name)
count=wordcount(file_full_path) 
filtered={ key:value for key, value in count.items() if value < 20 and value > 18 }
print(filtered)