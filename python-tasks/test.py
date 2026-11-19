#!/usr/bin/env python3
# scanner.py - Минималистичный порт-сканer с командной строкой

import socket

def main():
    # Опции CLI через argparse (минимум)
    import sys
    
    if len(sys.argv) > 1:
        host = sys.argv[1]           # Первый параметр - IP адрес
        port_str = "22"              # Если не задан, то по умолчанию порт 22
        
        for arg in sys.argv[2:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                if key == "-p":
                    port_str = value       # Порт через -p
                elif key == "--host":
                    host = value            # IP через --host (опционально)
                else:
                    print(f"❌ Неизвестный параметр: {arg}")
    else:
        host = "192.168.0.1"  # По умолчанию - ваш локальный IP (или IP вашего сканера)
        port_str = "22"         # По умолчанию - порт SSH

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if sock.connect_ex((host, int(port_str))) == 0:
            print(f"✅ {port_str} доступ")
        else:
            print(f"❌ {port_str} недоступен")
            
    except Exception as e:
        print(f"⚠️ Ошибка: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()