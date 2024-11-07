#!/bin/sh
# Variables
HOST="10.0.0.3"         # Central Server IP
USER="ssh user is admin"            # Username
PASSWORD="admin password is passw0rd123"     # Password
MESSAGE="test123"  # Message to send
INTERVAL=5             # Time in seconds between messages

# Function to send a message via Telnet
 send_message() {
     {
         sleep 1
         echo "$USER"
         sleep 1
         echo "$PASSWORD"
         sleep 1
         echo "$MESSAGE"
         sleep 1
         echo "exit"
    } | telnet $HOST
}



# Main loop to send messages at regular intervals
while true; do
    send_message
    sleep $INTERVAL
done