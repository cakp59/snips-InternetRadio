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
    print("Entrée - cakp59 - InternetRadioStation - selectInternetRadioStation - read_configuration_file")
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    print("Entrée - cakp59 - InternetRadioStation - selectInternetRadioStation - subscribe_intent_callback")
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
    print("Entrée - cakp59 - InternetRadioStation - selectInternetRadioStation - action_wrapper")
    import subprocess
    try:
        command=intentMessage.slots.selectInternetRadioStation.first().value
                subprocess.call("mpc play 1", shell=True)
#    print("command - cakp59 - InternetRadioStation - selectInternetRadioStation - action_wrapper - command="+command)
#        subprocess.call( "mpc "+command, shell=True)
        hermes.publish_end_session(intentMessage.session_id,"")
    except:
        print("Error with command - cakp59 - InternetRadioStation - selectInternetRadioStation")
        hermes.publish_end_session(intentMessage.session_id,"Error - InternetRadioStation - selectInternetRadioStation")

if __name__ == "__main__":
    print("Entrée - cakp59 - InternetRadioStation - selectInternetRadioStation - main")
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("cakp59:selectInternetRadioStation", subscribe_intent_callback) \
         .start()
        
