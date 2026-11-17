def parse_ip_port(line):
    return "192.168.1.1", 22

ip, port = parse_ip_port("...")
print(ip, port)

def log_alert(msg):
    print(f"[ALERT] {msg}")

log_alert("SSH brute force")   # выведет [ALERT] SSH brute force
# результат функции — None (аналог undefined в JS)

def scan(host, port=22):
    print(f"Сканирую {host}:{port}")

scan("192.168.1.1")        # port=22 по умолчанию
scan("192.168.1.1", 80)    # port=80

def greet(name):
    return f"Привет, {name}"

result = greet("Админ")
print(result)   # Привет, Админ

for port in [21, 22, 80, 443]:
    if port == 80:
        continue    # пропустить 80, идти дальше
    if port == 443:
        break       # полностью выйти из цикла
    print(port)     # выведет 21, 22

    i = 0
while i < 5:
    print(i)
    i += 1      # ВАЖНО: увеличить, иначе бесконечный цикл


for i in range(5):        # 0, 1, 2, 3, 4  (5 не включается!)
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8  (шаг 2)
    print(i)


    # JS:  for (let port of [21, 22, 80]) { console.log(port) }
# Python:
for port in [21, 22, 80]:
    print(port)