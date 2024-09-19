import random
import string

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


IPV4 = input("请输入服务器的外网IP：")
PROXY_COUNT = input("请输入需要生成的数量：")

for i in range(int(PROXY_COUNT)):
    RANDOM_PASSWORD = generate_random_string()
    DOCKER_COMMAND = f'docker run -d -p {4440+i}:4444 -p {7900+i}:7900 --shm-size="2g" -e SE_VNC_PASSWORD={RANDOM_PASSWORD} -e http_proxy="http://" -e https_proxy="http://" selenium/standalone-chrome:latest'
    LOGIN_VNC = f'http://{IPV4}:{7900+i}?autoconnect=1&resize=scale&password={RANDOM_PASSWORD}'
    print(f'#{i+1}')
    print(DOCKER_COMMAND)
    print(LOGIN_VNC)
    print('\n')
