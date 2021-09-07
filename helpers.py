import struct
import numpy as np
from matplotlib import pyplot as plt
import sllib


def unpack(frame):
    l = len(frame.packet)
    if frame.packetsize != l:
        print('packetsize:', frame.packetsize, len(frame.packet))
        return None
    temp = struct.unpack("i" * (frame.packetsize // 4), frame.packet)
    temp = np.array(temp)
    return temp


def read_echogram(input_file):
    with open(input_file, "rb") as f:
        reader = sllib.Reader(f)
        header = reader.header
        print(header)
        data = []
        for frame in reader:
            data.append(frame.to_dict())
            # the code to unpack the data packet
            temp = unpack(frame)
            if temp is None:
                continue
            try:
                echogram = np.vstack((echogram, temp))
            except NameError:
                echogram = temp
    echogram = echogram.T.astype("float32")
    return data, echogram


def read_xyz(input_file):
    x = []
    y = []
    z = []
    with open(input_file, 'rb') as f:
        reader = sllib.Reader(f)
        last = None
        for frame in reader:
            c = (frame.longitude, frame.latitude)
            if c != last:
                y.append(frame.latitude)
                x.append(frame.longitude)
                z.append(frame.water_depth_m)
                last = c
    return (x,y,z)
      