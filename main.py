import requests , time

while True:
    cookie = 's%3AoB4XDyXSx541eo1Uh2ROz_YXMslk9eWs.IRa%2BU%2BCkeca2FRqbhgM46okgQjswFA3T5GxMGB%2FLmNo'

    a = requests.get('https://dash.lunarnodes.xyz/a/earn', cookies={'connect.sid': cookie})
    try:
        coin = a.text.split('{earn:{points:')[1].split('}}')[0]

        print(f"Earn coin : +0.3 ({coin})")
    except:
        print("Error idk")
    time.sleep(2.3)