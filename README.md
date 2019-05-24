# Generated Snips skill

This is a generated Python 3 snips app, using the `snips-template` tool.
It is compatible with the format expected by the `snips-skill-server`

## Setup

This app requires some python dependencies to work properly, these are
listed in the `requirements.txt`. You can use the `setup.sh` script to
create a python virtualenv that will be recognized by the skill server
and install them in it.

## Executables

This dir contains a number of python executables named `action-*.py`.
One such file is generated per intent supported. These are standalone
executables and will perform a connection to MQTT and register on the
given intent using the `hermes-python` helper lib.

# Principe
This project is used by the snips project "InternetRadioStation"
It skill enables the creation of a playlist for mpc () in order to listen internet radio stations on a rpi.
1 - execute snips-InternetRadioStation-1.sh to install mpd / mpc
2 - execute snips-InternetRadioStation-2.sh to generate the playlist snips.playlist.radio.m3u for mpc in the folder /var/mpd/playlists. This script uses :
    - /var/lib/snips/skills/snips-InternetRadio/config.ini which contains the list of internet radio stations
    - the python2 file snips-InternetRadioStation-3.py that execute the generaton of snips.playlist.radio.m3u from config.ini
    
To add / remove / update your internet radio stations, modify the config.ini file according to the format. Execute again snips-InternetRadioStation-2.sh shell.
