import socket
from datetime import datetime


def check_host(host):
    print(f"\nChecking: {host}")

    # DNS check
    try:
        ip_address = socket.gethostbyname(host)
        dns_status = f"DNS OK - {ip_address}"
    except socket.gaierror:
        dns_status = "DNS FAILED"

    # Reachability check
    try:
        socket.create_connection((host, 80), timeout=3)
        reachability = "Port 80: Open / Reachable"
    except (socket.timeout, ConnectionRefusedError, OSError):
        reachability =  "Port 80: Closed / Not reachable"

    return dns_status, reachability


def main():
    hosts = [
        "google.com",
        "github.com",
        "example.com"
    ]

    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines = [
        "NETWORK HEALTH CHECK REPORT",
        f"Checked at: {report_time}",
        "-" * 50
    ]

    for host in hosts:
        dns_status, reachability = check_host(host)

        report_lines.append(f"Host: {host}")
        report_lines.append(f"DNS: {dns_status}")
        report_lines.append(f"Reachability: {reachability}")
        report_lines.append("-" * 50)

        print(f"DNS: {dns_status}")
        print(f"Reachability: {reachability}")

    with open("network_health_report.txt", "w") as file:
        file.write("\n".join(report_lines))

    print("\nReport saved as network_health_report.txt")


if __name__ == "__main__":
    main()