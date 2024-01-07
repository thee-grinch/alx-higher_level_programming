#!/usr/bin/bash
# display the sizeof the download

curl -s -w -'%{size_download}' $1
