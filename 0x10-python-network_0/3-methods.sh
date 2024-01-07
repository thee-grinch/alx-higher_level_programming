#!/bin/bash
#displays the availablle option
curl -i $1 2>&1 | grep -i '^allow:' | tr -d '\r'
