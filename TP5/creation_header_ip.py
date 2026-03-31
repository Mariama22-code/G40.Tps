import socket, sys, time
from struct import *

def create_ip_header(ip_source, ip_dest):
    ip_version   = 4
    ip_ihl       = 5
    ip_tos       = 0
    ip_total_len = 0
    ip_id        = 54321
    ip_frag_off  = 0
    ip_ttl       = 255
    ip_proto     = socket.IPPROTO_TCP
    ip_check     = 0
    ip_saddr     = socket.inet_aton( ip_source )
    ip_daddr     = socket.inet_aton( ip_dest )

    ip_ihl_ver = (ip_version << 4) + ip_ihl

    ip_header = pack('!BBHHHBBH4s4s',
            ip_ihl_ver,
            ip_tos,
            ip_total_len,  # CORRECTION : ip_tot_len → ip_total_len
            ip_id,
            ip_frag_off,
            ip_ttl,
            ip_proto,
            ip_check,
            ip_saddr,
            ip_daddr)

    return ip_header

if __name__ == '__main__':
    ip_source = '127.0.0.1'
    ip_dest   = '127.0.0.1'
    ip_header = create_ip_header(ip_source, ip_dest)
    print(ip_header)