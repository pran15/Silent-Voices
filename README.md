# SILENT VOICES:
One of the standard sign language techniques is the use of hand gestures. The ability of mute people to communicate with others is highly limited. This project aims to facilitate the diagnosis process of the mute patients via using hand gesture recognition system that housed in a right-hand glove and contain three flex sensors for three finger, converted to audio to help the doctor to make the right diagnosis, The system will compare the identified signal with stored data when it’s matched an mp3 audio file will be played as an output. This recognition system is designed to identify six hand gesture-already familiar to the patients- each of these gestures represent a phrase that is an answer to question asked frequently when seeing the general practitioner.

# HARDWARE REQUIRED:
1. Raspberry Pi Pico (RP 2040)
2. Flex sensor
3. Voice module
4. Jumper wires
5. LCD Display (16x2)
6. PCB Board


# SOFTWARE REQUIRED:
1. Proteus ( To simulate the project before doing hardware connections )
2. Thonny IDE ( Connect your Raspberry Pi to your laptop via USB, then open Thonny and select the appropriate interpreter to access your Raspberry Pi, allowing you to write and execute Python code directly on the Pi through your laptop screen )

# PROGRAMING LANGUAGE:
1. PYTHON

# BLOCK DIAGRAM:
![Block Diagram](https://github.com/user-attachments/assets/62d6d588-acb2-4f03-9b21-e0b346c3a8c2)

The resistance that the sensor outputs changes accordingly to the bend level that exists in the flex sensor.The sensor outputs a resistance that is proportional to the value of bend. In other words, the relationship between resistance and bend in sensor is the following: The greater the bend, the greater the output resistance The lower the bend, the lower the output resistance. The output can be an analog signal (A0) that can be read with an analog input of the raspberry pico or a digital output (D0) that can be read with a digital input of the raspberry pico.



