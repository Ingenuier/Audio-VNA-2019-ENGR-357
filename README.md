# Audio-VNA-2019-ENGR-357
Audio Frequency VNA Project for Engineering Electronics II
Christian Terrado

These are the setup instructions for the Reflection Bridge and Sound Card, these instructions were made with the Windows OS in mind.

Software Instructions:

    -git clone the repository ( https://github.com/Ingenuier/Audio-VNA-2019-ENGR-357.git )
    -Install Python 3.7.2 and your preferred tool for executing code 
        -Tests were done using a text editor and terminal
    -In terminal, import:
        -NumPy
        -matplotlib
        -skrf (had a little trouble with this one)
        -sounddevice
        -soundfile

Hardware Instructions:

    -Plug in a 7.1 Ch Sound Card into your computer
    -Take two male to male 3.5 mm audio jacks and attach the soundcard output (headphones) into the input jack on the PCB
        -Do the same with the sound card input (microphone) and plug it into the output jack on the PCB
        -Top audio plug is input jack and bottom audio plug is output jack 
    -Use the screw terminals to supply the PCB with +/- 15V and a connection to ground on a Power Supply
        -Old physical model did not do a great job at labeling so it would be best to refer to the schematic
        -In my tests I used a HP Triple Output Power Supply
    -Use third male to male jack to connect the Device Under Test to the D.U.T Port on the PCB
        -far right audio jack is the device under test
    -Pick which channel will be tested on the reflection bridge using the jumpers next to the D.U.T Port
        -top jumper is ring, bottom is tip. 
    -Turn on the power and run the code on the PC
