import os

mpdDir="/var/lib/mpd/playlists/"
config_ini_file="/var/lib/snips/skills/snips-InternetRadio/config.ini"
playlistFileName="snips.playlist.radio.m3u"
#
# Open the file snips.playlist.radio.m3u in write mode
# Directory must have the good rights
#
fi=open(config_ini_file, "rt")
fo = open(mpdDir+playlistFileName, "wt")
fo.write("#EXTM3U"+"\n\n")

for radioRecord in fi:
    if radioRecord[0:5] =="radio":
        radioName=radioRecord[8:radioRecord.find('|',0, len(radioRecord))]
        radioURL=radioRecord[radioRecord.find('|',0, len(radioRecord))+1:len(radioRecord)]
        fo.write("#EXTINF:-1,"+radioName+"\n")
        fo.write(radioURL+"\n")
fi.close()
fo.close()

