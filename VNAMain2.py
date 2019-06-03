import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import time

# Data on recording, etc on: https://python-sounddevice.readthedocs.io/en/0.3.12/usage.html#recording

# Low Frequencies, Assume No Phase Shift

# fs is sampling frequencies
fs = 96000
# in seconds
T = 1/fs
# pick frequenies to start at 2/(NT) where N is number of points wanting to be tested
N = 9000
frequencies = np.linspace(2/(N*T), (1875)/(N*T), num=35)
timeToSample = 1
# Amplitude of sample
sendAmplitude = .25
magnitudes = []

# number iteration used to get right fft value later in code
niter = 0

# refArray is the reference array that should hold the V+ values
refArray = []

# reflectArray is the reference array that should hold the V- values
reflectArray = [] 

for freq in frequencies:
    # TODO: run fft in every for loop on both left and right channel. 

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
    # print(recData)
    # will only display graph when recording is done?
    sd.wait()

    # Assume for now that left channel is reference bridge    
    # left channel
    leftData = recData[:,0]
    leftInput = data[:,0]
    # This will get highest value in the sin wave
    recordAmplitude = np.amax(leftData)
    # Find first instance where recorded is 50% of it's amplitude
    first = np.argmax(leftData > .5 * recordAmplitude)
    # Find first instance where generated is 50% of it's amplitude
    # Assume generated is all the same
    firstGen = np.argmax(leftInput > .5 * sendAmplitude)
    # This is where the recorded data is being chopped
    leftData = leftData[first:]    
    # Get wanted length of thehow to make matlab plots run simultaneous generated
    wantedLength = len(leftData)
    leftInput = data[:,0][firstGen:firstGen + wantedLength]
    lx = t[firstGen:firstGen + wantedLength]

    # Assume right channel is reflected channel
    # right channel
    rightData = recData[:,1]
    rightInput = data[:,1]
    # This will get highest value in the sin wave
    recordAmplitude = np.amax(rightData)
    # Find first instance where recorded is 50% of it's amplitude
    first = np.argmax(rightData > .5 * recordAmplitude)
    # Find first instance where generated is 50% of it's amplitude
    # Assume generated is all the same
    firstGen = np.argmax(rightInput > .5 * sendAmplitude)
    # This is where the recorded data is being chopped
    rightData = rightData[first:]    
    # Get wanted length of the generated
    wantedLength = len(rightData)
    rightInput = data[:,1][firstGen:firstGen + wantedLength]
    rx = t[firstGen:firstGen + wantedLength]

    # This block of code is to plot the waveforms
    # Discount osciloscope
    plt.figure(1)
    plt.plot(lx, leftData, label='reference')
    plt.plot(rx, rightData, label='reflection')
    plt.legend(loc="lower left")
    plt.title('Reference vs Reflected')
    plt.show()


    # TODO: figure out way to grab only the frequency value that I want   
    # Fast Fourier Transform
    
    # fftshift should shift off the dc 
    reflection = np.fft.fftshift(np.fft.fft(rightData/N))
    reference = np.fft.fftshift(np.fft.fft(leftData/N))

    # The frequency plotter for the fft does not work
    # no clue why, but it was only used for testing so not too worried
    # plt.plot(frequencies,np.abs(reference))
    # plt.show()

    # getting rid of the imaginary part of all elements
    
    # getting the only value that matters in the fft array
    reference = reference[1+niter]
    # getting the magnitude 
    refMax = np.abs(reference)

    # refMax = np.amax(refMax)
    # print("refmax: "),
    # print(refMax)

    # putting all the corrected values back into the array
    refArray.append(refMax)
    print("refarray: "),
    print(refArray)

    # getting the only value that matters in the fft array
    reflection = reflection[1+niter] 
    # getting rid of the imaginary part of all elements
    reflectMax = np.abs(reflection)

    print("reflection: "),
    print(reflection)

    # reflectMax = np.amax(reflectMax)
    print("reflectmax: "),
    print(reflectMax)

    # putting all the corrected values back into array
    reflectArray.append(reflectMax)
    print("reflectarray: "),
    print(reflectArray)

    niter += 1
    break


# reflection/reference angle reflection-reference magnitude
#plt.plot(frequencies, magnitudes)
#plt.show()

gamma = reflectMax/refMax
print("gamma = "),
print(gamma)

# last few lines are used as a discount smith chart
# This value is fixed to the board
Z0 = 1000

ZL = -((gamma+1)*Z0)/(gamma-1)
print("ZL = "),
print(ZL)

