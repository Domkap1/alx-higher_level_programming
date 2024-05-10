#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$1" | grep -o "Route 2"
    fi
}
