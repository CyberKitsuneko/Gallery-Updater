import os
import requests

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
    print("No gallery list found. Creating file...", end="")
    with open(gallery_list_path, "w") as new_file:
        new_file.close()
    print("done.")
    # Gallery list: read file
    with open(gallery_list_path, 'r') as read_file:
        gallery_list = read_file.read()
        gallery_list_array = gallery_list.split(";")
        # print(gallery_list_array)
        read_file.close()

# Remove empty items
for gallery in gallery_list_array:
    if gallery == "":
        gallery_list_array.remove(gallery)
    # print(gallery_list_array)

os.system("clear")
# Loop: add items to gallery list
while True:
    print("Current list: ")
    print(gallery_list_array)
    gallery_item = input("Gallery link: ")
    # Add item
    if gallery_item.startswith("ap "):
        gallery_item = gallery_item[3:]

        # Check if link exists
        try:
            response = requests.get(gallery_item).status_code
            if response == 404:
                print("404: page not found")
            elif response == 200:
                gallery_list_array.append(gallery_item)
                os.system("clear")
                print("Success.")
        except requests.exceptions.MissingSchema:
            os.system("clear")
            print("That does not seem like a link.")
        # except Exception as e:
        #     print(e)
    # Remove item
    elif gallery_item.startswith("rm "):
        gallery_item = gallery_item[3:]
        try:
            gallery_list_array.remove(gallery_item)
            os.system("clear")
        except ValueError:
            os.system("clear")
            continue
    # Write to file
    elif gallery_item == "write":
        with open(gallery_list_path, 'w') as write_file:
            for gallery in gallery_list_array:
                write_file.write(gallery + ",")
            write_file.close()
            break
    # Error
    else:
        os.system("clear")
        print("Unknown operation.")