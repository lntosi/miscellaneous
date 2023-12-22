#!/bin/bash

SOURCE_SERVER="192.168.1.x"
SOURCE_DIR="~/Desktop/rsync_test_src/"

DESTINATION_SERVER="192.168.1.y"
DESTINATION_DIR="~/Desktop/rsync_test_dst/"

USER="type_your_user"
PASSWORD="type_your_password"

WAIT_TIME=1m  # Wait time after a failure (e.g., 1 minute)

while true; do
    echo "Checking the availability of the remote server..."
    if sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$USER@$SOURCE_SERVER" "exit"; then
        echo "The remote server is accessible. Initiating synchronization..."
        sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$USER@$SOURCE_SERVER" "time rsync -avz --delete -e 'sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no' $SOURCE_DIR $USER@$DESTINATION_SERVER:$DESTINATION_DIR"
        echo "Synchronization completed. Waiting before the next execution..."
    else
        echo "Failed to check the availability of the remote server. Waiting before trying again..."
    fi
    sleep $WAIT_TIME
done
