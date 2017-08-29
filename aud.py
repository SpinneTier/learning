import wave, struct
file = wave.open("/home/krtk/python/task1.wav")
n = file.getnframes()
data = file.readframes(n)
frames = list(struct.unpack("@{0}h".format(n), data))
longframes=[]
i=0
for frame in frames:
  if i%3==0:
    longframes.append(frame*50)
    longframes.append(frame*50)
  else:
    longframes.append(frame*50)
  i=i+1
loud_data = struct.pack("@{0}h".format(len(longframes)),*longframes)
output_file = wave.open("/home/krtk/python/result.wav", 'w')
output_file.setparams(file.getparams())
output_file.writeframes(loud_data)
output_file.close()
