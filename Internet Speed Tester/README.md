## Import the speedtest Module
```py
import speedtest
```
- *This imports the speedtest module to utilize its functions for testing internet speed.*
```py
def bytes_to_mb(bytes):
    KB = 1024
    MB = 1024 * KB
    GB = 1024 * MB
    return int(bytes / MB)
```
- *This function converts the input bytes into megabytes by dividing by the appropriate factor (1024^2).*
### Prompt user to start:
```py
start = input('Press Enter to Start')
```
- *Waits for the user to press Enter to begin the test.*
### - Create a Speedtest Object:
```py
st = speedtest.Speedtest()
```
- *This initializes a Speedtest object, which can be used to perform various speed tests.*
### - Measure Download Speed:
```py
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
```
- *This line measures the download speed in bits per second and stores it in the variable down_speed.*
### - Get Ping Time:
```py
ping = st.results.ping
```
- *This retrieves the ping time (latency) in milliseconds and stores it in the variable ping.*
```py
print('down_speed : {} mb/s'.format(down_speed))
print('up_speed :  {} mb/s'.format(up_speed))
print('ping : {}'.format(ping))

```
- *These lines print the download speed, upload speed, and ping time.*
## output:
```cmd
Press Enter to Start
down_speed : 43 mb/s
up_speed :  48 mb/s
ping : 13.56
```