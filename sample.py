import numpy as np
import time

def perform_sin_fft(signal_length, frequency, trial_count):    
    start = time.time()
    
    for i in np.arange(1, trial_count+1):
        ramp = np.linspace(0, 2 * np.pi, signal_length)
        noise = np.random.rand(signal_length)    

        input_signal = np.sin(ramp * frequency) + 0.1*noise
        np.fft.fft(input_signal)
    
    computation_time = time.time() - start

    return computation_time

signal_lenghts = [2**10, 2**11, 2**12, 2**13, 2**14]
trial_count = 5000

for signal_length in signal_lenghts:
    frequency = int(signal_length / 4)

    computation_time = perform_sin_fft(signal_length, frequency, trial_count)

    print("Signal length {}, Computation time {:.3f} s".format(signal_length, computation_time))
