#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
<<<<<<< HEAD
curl -s -X DELETE "$1"
=======
curl -s -o /dev/null -w "%{http_code}" -X DELETE "$1" | { read status_code; if [ "$status_code" -eq 200 ]; then echo "route accept DELETE method"; else echo "route doesn’t accept DELETE method"; fi; }
>>>>>>> 50bdb62443836fea8f8c7628a89f459a2b6af681
