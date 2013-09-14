#! /bin/sh
# /etc/init.d/flirc

case "$1" in
  start)
    echo "Starting flirc"
    sudo /usr/bin/python /home/pi/Desktop/tech/flirc.py $
  ;;
  stop)
    echo "Stopping flirc"
    killall python
    ;;
  *)
    echo "Usage: /etc/init.d/flirc {start|stop}"
    exit 1
    ;;
esac

exit 0