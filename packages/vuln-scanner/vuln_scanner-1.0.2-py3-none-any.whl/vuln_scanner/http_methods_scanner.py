import requests
from rich.console import Console

console = Console()

def scan_http_methods(url):
    """
    🔍 فحص طرق HTTP المفعّلة (GET, POST, PUT, DELETE, OPTIONS).

    Args:
        url (str): رابط الموقع الذي سيتم فحصه.

    Example:
        scan_http_methods("https://example.com")
    """
    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH"]

    console.print(f"[cyan]🔍 بدء فحص HTTP Methods للموقع: {url}[/cyan]")

    for method in methods:
        try:
            response = requests.request(method, url, timeout=5)
            if response.status_code < 400:
                console.print(f"[yellow]⚠️ {method} مفعل في: {url}[/yellow]")
            else:
                console.print(f"[green]✅ {method} غير مفعل في: {url}[/green]")
        except requests.RequestException:
            console.print(f"[red]❌ تعذر استخدام {method} على: {url}[/red]")
