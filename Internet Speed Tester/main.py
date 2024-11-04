import speedtest

def bytes_to_mb(bytes):
    KB =  1024
    MB  = 1024 * KB
    GB  = 1024 * MB
    return int(bytes / MB)

st = speedtest.Speedtest()

start = input('Press Enter to Start')
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = st.results.ping

print('down_speed : {} mb/s'.format(down_speed))
print('up_speed :  {} mb/s'.format(up_speed))
print('ping : {}'.format(ping))