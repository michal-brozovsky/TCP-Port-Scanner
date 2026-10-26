import socket
import json
import argparse
from datetime import datetime

VULNERABLE_PORTS = {
    21: "FTP (Unencrypted file transfer)",
    23: "Telnet (Cleartext communication)",
    445: "SMB (Potential EternalBlue vulnerability)",
    3389: "RDP (Prone to brute-force attacks)"
}

def scan_target(ip_address):
    results = {"target": ip_address, "timestamp": str(datetime.now()), "findings": []}
    
    for port, issue in VULNERABLE_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((ip_address, port))
        
        if result == 0:
            results["findings"].append({"port": port, "status": "Open", "risk": issue})
        sock.close()
        
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Network Vulnerability Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    args = parser.parse_args()

    print(f"[*] Scanning {args.target}...")
    report = scan_target(args.target)
    
    with open("scan_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("[+] Scan complete. Results saved to scan_report.json")