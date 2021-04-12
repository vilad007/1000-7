import requests, json, time

token = input('Введите токен: ')
m = 1000
last = False
change_time = 0.2
while True:
    if not last:
        message = m - 7
        change_time = 0.2
    if last:
        message = 'Я ГУЛЬ 😈😈😈'
        change_time = 12
    if m - 7 < 7:
        last = True

    status_data = json.dumps({'custom_status': {'text': f"{m}-7={message}"}})
    r = requests.patch('https://discordapp.com/api/v6/users/@me/settings',
                      headers={'Authorization': token,
                               'Content-Type': 'application/json'},
                      data=status_data)
    print(f"{m} - 7 = {message}", end='\n')
    m -= 7
    if m < 0:
        last = False
        m = 1000
    time.sleep(change_time)
