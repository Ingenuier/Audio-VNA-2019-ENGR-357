# Audio-VNA-2019-ENGR-357
Audio Frequency VNA Project for Engineering Electronics II

These are the setup instructions for the Reflection Bridge and Sound Card, these instructions were made with the Windows OS in mind.

Software Instructions:

    -git clone the repository ( https://github.com/Ingenuier/Audio-VNA-2019-ENGR-357.git )
    -Install Python 3.7.2 and your preferred tool for executing code 
        -In my tests Windows Powershell and JetBrain's PyCharm were used, in this instruction set we'll use PyCharm
    -In PyCharm, import:
        -NumPy
        -matplotlib
        -sounddevice
        -soundfile
    -Configure the VNAMain.py to execute through PyCharm

Hardware Instructions:

    -Plug in a 7.1 Ch Sound Card into your computer
    -Take two male to male 3.5 mm audio jacks and attach the soundcard output (headphones) into the input jack on the PCB
        -Do the same with the sound card input (microphone) and plug it into the output jack on the PCB
    -Use banana jack connectors to supply the PCB with +/- 15V and a connection to ground on a Power Supply
        -In my tests I used a HP Triple Output Power Supply
    -Use third male to male jack to connect the Device Under Test to the D.U.T Port on the PCB
    -Turn on the power and run the code on the PC
