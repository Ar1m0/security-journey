def check_port(port):
    if port in [22, 80, 443]:
        return True
    else:
        return False
print(check_port(23))

def check_port(port):
    return port in [22, 80, 443]

print(check_port(22))

ports = [22, 80, 443]

for i in ports:
    status = "opened" if check_port(i) else "closed"
    print(f"Порт {i}: {status}")


def scan_range(start, end):
    for i in range(start, end):
        print(f"Проверяю 192.168.1.{i}")

scan_range(-1,3)

def count_open(ports):
    count = 0
    for port in ports:
        if port == 22:
            continue
        if check_port(port):
            count += 1
    return count
result = count_open([21, 22, 23, 80, 443, 8080])
print(f"Открытых портов: {result}")


