#!/bin/bash

# settings
DIR=$(dirname $(readlink -f $0))
SCREEN_NAME="discord-mcc-bot"

# functions

# determine if the specified named screen session is running
# by searching for it in the screen -ls
# TODO: make this more efficient
no_screen_yet() {
	local SCREEN_PID=$(screen -ls | awk -v pat="\\\.$SCREEN_NAME\\\t" '$0~pat {print strtonum($1)}')
	if [ -n "$SCREEN_PID" ]
	then
		false
	else
		true
	fi
}

create_screen() {
    screen -dm $SCREEN_NAME
}

send() {
	local cmd=$1
	screen -S $SCREEN_NAME -X stuff "$cmd^M"
}

# main script
if no_screen_yet; then
    create_screen
	echo "created screen $SCREEN_NAME"
	sleep 1s
fi
send "cd $DIR"
sleep 1s
send "pipenv shell"
sleep 3s
send "python3 ./bot.py"
echo "Start command for discord mcc bot was sent to $SCREEN_NAME"