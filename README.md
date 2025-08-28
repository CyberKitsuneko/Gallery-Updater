# Gallery-Updater
A bash script that updates your downloaded galleries from gallery-dl.

# Dependencies
- python
- gallery-dl
- requests

# Usage
## List creator
It creates a ```gallery_list.kts``` file in the current directory, which you can add to/remove from manually, or using the `list-creator.py` script.
- ```ap [link]``` - add link to list
- ```rm [link]``` - remove link from list
- ```write``` - write list to file
Additionally, you can add custom arguments to each link manually for ```gallery-dl``` to process when updating the links (the separator is `;`)
## Gallery updater
- when prompted to enter your chosen download directory, you can enter ```no``` to download in current directory (do this when running the script from the download directory as well)
