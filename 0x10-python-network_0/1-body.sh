#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | xargs -I {} sh -c 'if [ "{}" -eq 200 ]; then curl -s "$1"; fi' dummy | grep "Route 2" | awk '{print $3}'
