import ssl
import socket
from rich.console import Console

console = Console()

def scan_ssl_tls(domain):
    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                console.print(f"[green]✅ شهادة SSL/TLS صالحة لموقع: {domain}[/green]")
                console.print(f"[cyan]📅 تنتهي في: {cert['notAfter']}[/cyan]")
    except Exception as e:
        console.print(f"[red]❌ مشكلة في SSL/TLS مع الموقع {domain}: {e}[/red]")
