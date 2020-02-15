#!/usr/bin/env bash

cd ..

chmod 755 .

#Change all permisions for directories
echo "Chmoding directories"
find . -type d -exec chmod 755 {} +

#Change all permisions for python files in index.py, api, and webfiles
echo "Chmoding python files"
find api -type f -iname "*.py" | xargs chmod 705
find webfiles -type f -iname "*.py" | xargs chmod 705
chmod 705 index.py

#Change all permisions for bash files
echo "Chmoding bash files"
find . -type f -iname "*.sh" -exec chmod +x {} +

#Fix database permissions so apis can write to it. The folder its in also needs to be writable
echo "Chmoding database"
find . -type f -name '*.db' -exec sh -c 'chmod 757 $(dirname $1)' - {} \;

# Change all permissions for html, js, css, png 
for i in {html,js,css,png}; do
  echo "Chmoding $i files"
	find . -type f -iname "*.$i" | xargs chmod 604
done	
