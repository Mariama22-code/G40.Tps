import socket, sys, time
from struct import *

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i+1] if i+1 < len(msg) else 0)
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

def create_tcp_header(message, ip_source, ip_dest):
    tcp_source   = 1234
    tcp_dest     = 80
    tcp_seq      = 454
    tcp_ack_seq  = 0
    tcp_doff     = 5
    tcp_fin      = 0
    tcp_syn      = 1
    tcp_rst      = 0
    tcp_psh      = 0
    tcp_ack      = 0
    tcp_urg      = 0
    tcp_window   = socket.htons(5840)
    tcp_check    = 0
    tcp_urg_ptr  = 0

    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + \
        (tcp_syn << 1) + (tcp_rst << 2) + \
        (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5)

    tcp_header = pack('!HHLLBBHHH', tcp_source,
        tcp_dest, tcp_seq, tcp_ack_seq,
        tcp_offset_res, tcp_flags, tcp_window,
        tcp_check, tcp_urg_ptr)

    source_address = socket.inet_aton( ip_source )
    dest_address   = socket.inet_aton( ip_dest )
    placeholder    = 0
    protocol       = socket.IPPROTO_TCP
    tcp_length     = len(tcp_header) + len(message)

    psh = pack('!4s4sBBH', source_address, dest_address,
        placeholder, protocol, tcp_length)

    tcp_check = checksum( psh )

    tcp_header = pack('!HHLLBBH', tcp_source, tcp_dest,
        tcp_seq, tcp_ack_seq, tcp_offset_res,
        tcp_flags, tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_ptr)

    return tcp_header

if __name__ == '__main__':
    ip_source  = '127.0.0.1'
    ip_dest    = '127.0.0.1'
    message    = 'Hello, how are you'
    tcp_header = create_tcp_header(message, ip_source, ip_dest)
    print(tcp_header)