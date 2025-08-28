import os

# Current working directory
cwd = os.getcwd()
# Gallery list: file path
gallery_list_path = cwd + "/gallery_list.kts"
# Gallery list: check if file exists
does_gallery_list_exist = os.path.isfile(cwd + "/gallery_list.kts")

if does_gallery_list_exist:
    # Gallery list: read file
    with open(gallery_list_path, 'r') as read_file:
        gallery_list = read_file.read()
        gallery_list_array = gallery_list.split(";")
        # print(gallery_list_array)
        read_file.close()
else:
    # Gallery list: create file
    print("No gallery list found.")
    quit()

download_dir = input("Enter download directory: ")
# Download to directory
if download_dir == "no":
    for gallery in gallery_list_array:
        os.system(f"gallery-dl {gallery}")
else:
    if os.path.isdir(download_dir):
        for gallery in gallery_list_array:
            os.system(f"cd {download_dir} && gallery-dl {gallery}")