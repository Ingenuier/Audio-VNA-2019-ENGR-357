import numpy as np
# import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
#Data on recording, etc on: https://python-sounddevice.readthedocs.io/en/0.3.12/usage.html#recording

data, fs = sf.read('reee.wav', dtype='float32')
sd.playrec(data, fs, channels=2)
status = sd.wait()
