# The name of polybar bar which houses the main spotify module and the control modules.
PARENT_BAR="media"
PARENT_BAR_PID=$(pgrep -a "polybar" | grep "$PARENT_BAR" | cut -d" " -f1)

# Sends $2 as message to all polybar PIDs that are part of $1
update_hooks() {
    while IFS= read -r id
    do
        polybar-msg -p "$id" hook music-play-pause $2 1>/dev/null 2>&1
    done < <(echo "$1")
}

if [ "$1" == "--playing" ]; then
    update_hooks "$PARENT_BAR_PID" 1
elif [ "$1" == "--paused" ]; then
    update_hooks "$PARENT_BAR_PID" 2
else
    echo "Usage: $0 --[playing|paused]"
fi
