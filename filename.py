abs_path = '/home/apple/Downloads/story.tar.gz'
file_name = abs_path.rsplit('/',1)[1]
directory = abs_path.rsplit('/',1)[0]
extension = file_name.split('.',1)[1]

print("Directory:",directory)
print("File name:",file_name)
print("Extension:", extension)
