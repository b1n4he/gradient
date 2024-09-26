import os
import json
import random
import string

def random_port():
    return random.randint(40000, 65535)

def random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def filter_and_modify_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if 'inbounds' in data:
                    # 过滤掉 tag 不为 'socks2' 的项
                    data['inbounds'] = [item for item in data['inbounds'] if item.get('tag') == 'socks2']
                    
                    for item in data['inbounds']:
                        if item.get('tag') == 'socks2':
                            # 修改 port 字段为随机值
                            item['port'] = random_port()
                            # 修改 pass 字段为随机的8位字符串
                            item['settings']['accounts'][0]['pass'] = random_password()
            
            # 将修改后的数据写回原文件
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


filter_and_modify_json_files('./node')  

def display_proxies(directory):
    proxies = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if 'inbounds' in data:
                    for item in data['inbounds']:
                        if item.get('tag') == 'socks2':
                            proxy_info = {
                                "ip": "127.0.0.1",
                                "port": item.get('port'),
                                "protocol": item.get('protocol'),
                                "auth": item['settings'].get('auth'),
                                "user": item['settings']['accounts'][0].get('user'),
                                "pass": item['settings']['accounts'][0].get('pass')
                            }
                            proxies.append(proxy_info)

    # 打印代理信息
    for proxy in proxies:
        print(f"IP: {proxy['ip']}, 端口号: {proxy['port']}, 代理协议: {proxy['protocol']}, "
              f"认证方式: {proxy['auth']}, 用户名: {proxy['user']}, 密码: {proxy['pass']}")

# 使用示例
display_proxies('./node')  # 替换为你的目录路径



def create_proxy_batch_file(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as batch_file:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                command = f"start xray.exe -c ./{directory}/{filename}\n"
                batch_file.write(command)

# 使用示例
create_proxy_batch_file('node', 'proxy.bat')  # 替换为你的目录路径

print("\n请保存好代理信息，运行proxy.bat即可打开代理")