import scipy.io.wavfile
import matplotlib.pyplot as plt


samplerate, data = scipy.io.wavfile.read("file1")



plt.figure()
plt.plot(data)
print len(data)
plt.show()