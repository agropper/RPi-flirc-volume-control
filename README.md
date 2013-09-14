RPi-flirc-volume-control
========================

45 lines of python run by a .sh script on Raspberry Pi uses an IR receiver to drive homebrew volume up-down-mute

The IR receiver-to-USB (www.flirc.tv) is configured to listen for 3 of the keys on an Apple Remote and output
3 keyboard chars to a real time kernel based on pygame. RPi.GPIO drives a tiny bit of custom circuitry to 
a motorized ALPS volume control and a FET muting circuit via L272 power opamps.

Here's roughly what I did to configure a bare metal RPi
start with a current Raspbian and do apt-get update and apt-get upgrade
set keyboard to us http://elinux.org/RPi_Beginners
install samba
move the software from the Mac using Finder
init.d shell script http://www.raspberrypi.org/phpBB3/viewtopic.php?t=24884&p=228881
then http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html

