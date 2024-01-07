#!/bin/bash
#display the sizeof the download
curl -s -o /dev/null -w '%{size_download}\n' $1
