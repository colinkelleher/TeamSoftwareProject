#!/usr/bin/env bash

#Change all permisions for directories
cd ..
echo "Chmoding directories"
find . -type d -exec chmod 755 {} +

#Change all permisions for python files
echo "Chmoding python files"
find . -iname "*.py" -exec chmod +x {} +