import struct
import os
import numpy as np
from matplotlib import pyplot as plt
import sllib


from tqdm import tqdm_notebook as tqdm
tqdm().pandas()
#from tqdm import tqdm

def unpack(frame):
    l = len(frame.packet)
    if frame.packetsize != l:
        print('packetsize:', frame.packetsize, len(frame.packet))
        return None
    temp = struct.unpack("i" * (frame.packetsize // 4), frame.packet)
    temp = np.array(temp)
    return temp


def read_echogram(input_file, channels=None):
    used = 0
    counter = 0
    filesize = os.path.getsize(input_file)
    pbar = tqdm(total=filesize, unit='B', unit_scale=True)
    info =  {'header': '', 'channels': [0] * 10}
    offset = 0
    with open(input_file, "rb") as f:
        reader = sllib.Reader(f)
        header = reader.header
        info['header'] = f'{header}'
        if channels:
            reader.add_filter(channels=channels)
        data = []
        for frame in reader:
            info['channels'][frame.channel] += 1
            pbar.update(reader.tell()-offset)
            offset = reader.tell()
            
            counter += 1
            data.append(frame.to_dict())
            # the code to unpack the data packet
            temp = unpack(frame)
            if temp is None:
                continue
            try:
                echogram = np.vstack((echogram, temp))
                used +=1
            except NameError:
                echogram = temp
        pbar.update(reader.tell()-offset)
    pbar.close()
    if used == 0:
        raise Exception('no frames used')
    echogram = echogram.T.astype("float32")
    #print(info)
    #print(f'frames used: {used}/{counter}')
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
      