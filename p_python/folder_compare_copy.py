import filecmp
import os

#source_dir = r'C:\A'
#dest_dir = r'C:\B'

source_dir = r'\\tsclient\c\workspace\obs\spotlight'
dest_dir = r'C:\workspace\obs\spotlight_dev'

diff_files = []
suffixes=(".php", "sql", ".kml", ".py", ".js")
for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        if not filename.endswith(suffixes):
            continue
        source_file = os.path.join(dirpath, filename)
        dest_file = os.path.join(dest_dir, os.path.relpath(source_file, source_dir))
        
        if os.path.exists(dest_file):
            if not filecmp.cmp(source_file, dest_file, shallow=False):
                diff_files.append(source_file)
        else:
            diff_files.append(source_file)

print("Different files:")
for file_path in diff_files:
    print(file_path)


print("\n generate copy commands :")
print("****************") 
  
i=len(source_dir)    
for file_path in diff_files:
    print(" copy ", file_path, dest_dir + file_path[i:]) 
