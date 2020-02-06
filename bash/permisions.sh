#!/usr/bin/env bash

cd ..

#Change all permisions for directories
echo "Chmoding directories"
find . -type d -exec chmod 755 {} +

#Change all permisions for python files
echo "Chmoding python files"
find . -iname "*.py" -exec chmod +x {} +

#Change all permisions for bash files
echo "Chmoding bash files"
find . -iname "*.sh" -exec chmod +x {} +

#Fix database permissions so apis can write to it. The folder its in also needs to be writable
find . -name '*.db' -exec sh -c 'chmod 757 $(dirname $1)' - {} \;