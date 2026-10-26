# TCP Port Scanner

A lightweight Python tool for identifying potentially vulnerable open ports on local networks. Designed for quick auditing of corporate IT environments.

## Features
* Scans targets for high-risk ports (FTP, Telnet, SMB, RDP).
* Uses Python's native `socket` library for TCP connection testing.
* Exports structured findings into a JSON report for further analysis.

## Prerequisites
* Python 3.x
* No external libraries required.

## Usage
Run the script via command line and specify the target IP address:
`python scanner.py -t 192.168.1.100`

The script will generate a `scan_report.json` file in the current directory containing the timestamp, target IP, and identified risks.
