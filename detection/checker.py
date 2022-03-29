# test
def check_packet(packet) -> bool:
    if '.tgg' not in packet.packet_name:
        return True
    else:
        return False
    # return packet.packet_name.contain('tgg')
