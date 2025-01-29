import speedtest

def test_speed():
    speed = speedtest.Speedtest()
    speed_down = speed.download()
    speed_down = round(speed_down/10**6,2)
    print("downloading speed in mbps",speed_down)
    
    speed_up = speed.upload()
    speed_up = round(speed_up/10**6,2)
    print("uploading speed in mbps",speed_up)

    ping_network = speed.results.ping
    print("pinging",ping_network)

test_speed()