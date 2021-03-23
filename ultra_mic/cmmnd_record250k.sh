#!/bin/sh

# arecord option descriptions
# -t : data type, ex) -t raw, -t wav
# -D : record device infomation, ex) card 1, 0 dev = -D hw:1,0 [plughw : various sampling rate / hw : 250k only]
# -c : channel, ex) 2 = stereo, 1 = mono
# -r : sampling rate 250k = 250000
# -f : format ex) signed 16-bit PCM = S16_LE
# -d : duration, ex) -d 10 = 10 sec
###############################################################################################################
# cat /proc/asound/cards , sound card hardware info
# ex)
# 0 [Headphones     ]: bcm2835_headphonbcm2835 Headphones - bcm2835 Headphones
#                      bcm2835 Headphones
# 1 [r4             ]: USB-Audio - UltraMic 250K 16 bit r4
#                      DODOTRONIC Technology   . UltraMic 250K 16 bit r4 at usb-0000:01:00.0-1.2, full
###############################################################################################################
# raw data, mono, 16bit 250k record (ultrasonic)
# ex) arecord -t raw -c 1 -D hw:1,0 -f S16_LE -d 10 -r 250000 filename.pcm 

#duration="10"
#read -e -i "$duration" -p "duration(sec) : " input
#duration="${input:-$duration}"

arecord -t raw -c 1 -D hw:1,0 -f S16_LE -d 3 -r 250000 "cmmnd_pcm250k_$(date +"%Y_%m_%d__%H_%M_%S").pcm"
