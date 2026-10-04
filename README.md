# Network Health Checker

A Python command-line tool that checks DNS resolution and TCP connectivity for multiple hosts and generates a timestamped network health report.

## Features

- Performs DNS resolution for configured hosts
- Checks TCP connectivity on port 80
- Handles connection timeouts and errors
- Checks multiple hosts
- Generates a timestamped network health report
- Displays results directly in the command line

## Technologies Used

- Python
- Socket programming
- DNS resolution
- TCP networking
- Exception handling
- File handling

## Hosts Checked

The current version checks:

- google.com
- github.com
- example.com

## How to Run

Make sure Python is installed.

Open Command Prompt in the project folder and run:

```bash
python network_health_checker.py


Checking: google.com
DNS: DNS OK - <IP address>
Reachability: Port 80: Open / Reachable

Checking: github.com
DNS: DNS OK - <IP address>
Reachability: Port 80: Open / Reachable

Checking: example.com
DNS: DNS OK - <IP address>
Reachability: Port 80: Open / Reachable

Report saved as network_health_report.txt
