import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import time

# Data on recording, etc on: https://python-sounddevice.readthedocs.io/en/0.3.12/usage.html#recording

# Low Frequencies, Assume No Phase Shift

# frequencies = np.arange(20, 5000, )
frequencies = np.linspace(20, 20000, num=50)
# fs is sampling frequencies
fs = 96000
# in seconds
timeToSample = 1
sendAmplitude = .25

magnitudes = []

for freq in frequencies:
    freq = 1000
    # Record starts a while after playback for some unknown reason
    # It usually starts about .07 seconds after playback, so...
    # We have to record for at least .07 seconds and then chop it off
    # We'll go to .1 second just to be safe, keep in mind each frequency
    # we want will take over a second... unforutantly
    # TODO: Fix that issue cuase it's stupid
    # np.arange(start, stop, step, dtype = none)
    t = np.arange(0, timeToSample, 1 / fs)
    # data = sendAmplitude * np.sin(2 * np.pi * freq * t)
    
    data = np.array([np.array([1,1]) * sendAmplitude * np.sin(2 * np.pi * freq * m) for m in t])
    
    
    # playrec plays and records data
    recData = sd.playrec(data, fs, channels=2)
    print(recData)
    # will only display graph when recording is done?
    sd.wait()
    
    # left channel
    leftData = recData[:,0]
    # This will get highest value in the sin wave
    recordAmplitude = np.amax(leftData)
    # Find first instance where recorded is 50% of it's amplitude
    first = np.argmax(leftData > .5 * recordAmplitude)
    # Find first instance where generated is 50% of it's amplitude
    # Assume generated is all the same
    firstGen = np.argmax(leftData > .5 * sendAmplitude)
    # This is where the recorded data is being chopped
    leftData = leftData[first:]    
    # Get wanted length of the generated
    wantedLength = len(leftData)
    leftInput = data[:,0][firstGen:firstGen + wantedLength]
    lx = t[firstGen:firstGen + wantedLength]
    # This block of code is to plot the waveforms
    #Used for troubleshooting
    plt.plot(lx, leftData, label='recorded')
    plt.plot(lx, leftInput, label='sent')
    plt.legend(loc="lower left")
    plt.title('left channlke')
    plt.show()
    
    
    print(recData)
    # right channel
    rightData = recData[:,1]
    # This will get highest value in the sin wave
    recordAmplitude = np.amax(rightData)
    # Find first instance where recorded is 50% of it's amplitude
    first = np.argmax(rightData > .5 * recordAmplitude)
    # Find first instance where generated is 50% of it's amplitude
    # Assume generated is all the same
    firstGen = np.argmax(rightData > .5 * sendAmplitude)
    # This is where the recorded data is being chopped
    rightData = rightData[first:]    
    # Get wanted length of the generated
    wantedLength = len(rightData)
    rightInput = data[:,1][firstGen:firstGen + wantedLength]
    rx = t[firstGen:firstGen + wantedLength]
    # This block of code is to plot the waveforms
    #Used for troubleshooting
    plt.plot(rx, rightData, label='recorded')
    plt.plot(rx, rightInput, label='sent')
    plt.legend(loc="lower left")
    plt.title('rigt channel mang')
    plt.show()
    
    
    # TODO: make sure this is correct/ fix in post
    # TODO: to debug run through one of these loops setting loop 1 to low 1 to high
    mag = np.average([np.abs(recData[i] / data[i]) for i in range(len(recData)) if np.abs(data[i]) > .5 * sendAmplitude and np.abs(recData[i]) > .5 * recordAmplitude])
    magnitudes.append(20 * np.log10(mag))
    #    print('mag for freq of ' + str(freq))
    #    print(mag)
    
    break

plt.plot(frequencies, magnitudes)
plt.show()

