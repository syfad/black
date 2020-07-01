

import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_data = input("input you data:")

    udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.10", 7000))

    udp_socket.close()

if __name__ == "__main__":
    main()