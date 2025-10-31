import timesync, time

timesync.sync()

_, _, _, hr, _, _, _, _ = time.localtime()
print(hr)
