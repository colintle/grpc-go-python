#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SERVER_CONTAINER=dbf952016b00  # Replace with the correct server container ID
CLIENT_CONTAINER=aa71b40a5711

LOCAL_SERVER_DIR="$SCRIPT_DIR/server"
LOCAL_CLIENT_DIR="$SCRIPT_DIR/client"

docker cp $SERVER_CONTAINER:/app/. $LOCAL_SERVER_DIR
echo "Server files copied to $LOCAL_SERVER_DIR"
docker cp $CLIENT_CONTAINER:/app/. $LOCAL_CLIENT_DIR
echo "Client files copied to $LOCAL_CLIENT_DIR"
