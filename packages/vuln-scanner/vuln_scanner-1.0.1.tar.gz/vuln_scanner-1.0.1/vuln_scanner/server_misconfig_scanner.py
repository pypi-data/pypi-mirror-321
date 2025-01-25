import requests
from rich.console import Console

console = Console()

def scan_server_misconfig(url):
    sensitive_paths = [
        "/.git/", "/backup/", "/admin/", "/config/", "/db/", "/logs/",
        "/test/", "/tmp/", "/uploads/", "/phpinfo.php"
    ]

    for path in sensitive_paths:
        target_url = url + path
        try:
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                console.print(f"[red]❌ تم العثور على ملف حساس: {target_url}[/red]")
            elif response.status_code == 403:
                console.print(f"[yellow]⚠️ الوصول مرفوض لكنه موجود: {target_url}[/yellow]")
        except requests.RequestException:
            pass
