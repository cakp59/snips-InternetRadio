#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)

def action_wrapper(hermes, intentMessage, conf):
    """ Write the body of the function that will be executed once the intent is recognized.
    In your scope, you have the following objects :
    - intentMessage : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
    - conf : a dictionary that holds the skills parameters you defined.
      To access global parameters use conf['global']['parameterName']. For end-user parameters use conf['secret']['parameterName']

    Refer to the documentation for further details.
    """
    import subprocess
    import os

    try:
        command="--????--"
        command=intentMessage.slots.RadioStationToLoad.first().value
        if command == "recharge les radios internet":
            mpdDirPlaylist="/var/lib/mpd/playlists"
            playlistFileName="snips.playlist.radio.m3u"
            subprocess.call("mpc clear", shell=True)
#            subprocess.call("mpc rm snips.playlist.radio", shell=True)  
            radioNumber=conf['secret'][RadioNumber]
#
# Open the file snips.playlist.radio.m3u in write mode
# !!!! mpdDirPlaylist directory must have the good rights
#
            os.remove(mpdDirPlaylist+"/"+playlistFileName)
            fo = open(mpdDirPlaylist+"/"+playlistFileName, "w")
            fo.write("#EXTM3U"+"\n\n")
            for i in range(radioNumber): 
                radioNum='%(aa)s%(number)02d' %{'aa': "radio", "number": i+1}
                radioRecord=conf['secret'][radioNum]
                radioName=radioRecord[8:radioRecord.find('|',0, len(radioRecord))]
                radioURL=radioRecord[radioRecord.find('|',0, len(radioRecord))+1:len(radioRe$                
                fo.write("#EXTINF:0,"+radioName+"\n")
                fo.write(radioURL+"\n\n")
            fo.close()
                        
#                radioNum='%(aa)s%(number)02d' %{'aa': "radio", "number": i+1}
#                command="mpc add "+radioURL
#                subprocess.call(command, shell=True)
#            subprocess.call("mpc save snips.playlist.radio", shell=True)
        else:
            ErrMess="snips-InternetRadio - command KO - loadInternetRadioStation - command="+command
            hermes.publish_end_session(intentMessage.session_id,ErrMess)
    except:
        ErrMess="snips-InternetRadio - command KO - SelectedStation - command= "+command
        hermes.publish_end_session(intentMessage.session_id,ErrMess)

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("cakp59:loadInternetRadioStation", subscribe_intent_callback) \
         .start()
        
