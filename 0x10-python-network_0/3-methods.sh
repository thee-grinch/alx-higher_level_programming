#!/bin/bash
#displays the availablle option
curl -i $1 | grep -i 'Allow:' | cut -d " " -f 2-
