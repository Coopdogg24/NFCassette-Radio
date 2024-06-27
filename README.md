# Description
The **NFC**assette Tape Radio project aim to create a portable hand-held radio capable of reading NFC powered cassette tapes and playing tracks through Spotify.   

The RFID receiver is connected to a Raspberry Pi, which is then connected to a speaker. The Raspberry Pi runs [Raspotify](https://github.com/dtcooper/raspotify) and [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/), two python libraries that allow the Raspberry Pi to interact with the Spotify API. 

When a cassette tape is placed into the radio, the RFID receiver sends the stored data to the Raspberry Pi, which then plays the corresponding album from Spotify. Additionally, the project includes 3D-printed cassette tapes, which can be customized to display artwork from favourite albums.


# Hardware Setup
The RFID reader that is being used in this project is the RFID RC522 (MFRC522). The MFRC522 is a highly integrated reader/writer IC for contactless communication at 13.56 MHz and supports ISO/IEC 14443 A/MIFARE mode.

Using the below diagram, connect the RFID RC522 to the raspberry pi. 

> Note: In my studies I found that there are multiple version of the RFID RC522, mainly a Red and a Blue version. I have no idea why, but they are slightly different. The naming of the pins is very similar, but they are out of order to the below diagram - make sure to read the labels of the pins you are connecting


![Pasted image 20240627133531](https://github.com/Coopdogg24/NFCassette-Radio/assets/29032843/666b2192-76ad-4dc8-94c8-b13a1dc9d50b)
![Raspberry Pi GPIO Pinout Diagram](https://github.com/Coopdogg24/NFCassette-Radio/assets/29032843/00817fdb-9548-408b-ab3b-c01a595ccd25)


## Testing of Hardware
To test the hardware, consider running the below scripts and writing / reading from a NFC tag
### Write
```python
# Import Libraries
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Define the RFID Reader
reader = SimpleMFRC522()

# User Input of data you wish to Write 
text = input('New data: ')

# Writing to NFC Tag
print("Now place your tag to write")
reader.write(text)
print("Written")
```
### Read
```python
# Import Libraries
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Define the RFID Reader
reader = SimpleMFRC522()

# Reading of an NFC Tag
print("Place card to read")
print(reader.read())
```


# Software Setup
[...]


# Future Plans
1) Animal Crossing Soundtrack that changes based on the hour
2) Home Assistant integration to tailor the music taste to the people currently home
3) WebUI to control the radio, and write new cassette tapes
