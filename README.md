# pi-version
Stop Googling "how to check Raspberry Pi model", vaguely remembering how to find the revision number, then Googling the revision number.

#### If you don't care about executing arbitrary code from the internet  

In your terminal:  


``` curl -s https://raw.githubusercontent.com/tobymurray/pi-version/master/pi-version.py | python ```

#### If you do care, or you want to keep the script  

1. ```curl -O https://raw.githubusercontent.com/tobymurray/pi-version/master/pi-version.py```
1. Look at the script if you're curious
1. ```python pi-version.py```

All information taken from http://elinux.org/RPi_HardwareHistory 