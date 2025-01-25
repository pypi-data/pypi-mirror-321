import requests
from rich.console import Console

console = Console()

def scan_security_headers(url):
    """
    🔍 فحص رؤوس الأمان (Security Headers) للموقع المستهدف.

    Args:
        url (str): رابط الموقع الذي سيتم فحصه.

    Example:
        scan_security_headers("https://example.com")
    """
    security_headers = {
        "Content-Security-Policy": "يحمي من XSS",
        "Strict-Transport-Security": "يحمي من هجمات Man-in-the-Middle",
        "X-Content-Type-Options": "يحمي من MIME Sniffing",
        "X-Frame-Options": "يحمي من Clickjacking",
        "Referrer-Policy": "يحمي من تسريب معلومات URL",
        "Permissions-Policy": "يحمي من سوء استخدام APIs"
    }

    try:
        response = requests.get(url, timeout=5)
        for header, description in security_headers.items():
            if header in response.headers:
                console.print(f"[green]✅ {header} مفعّل - {description}[/green]")
            else:
                console.print(f"[red]❌ {header} غير مفعّل - {description}[/red]")
    except requests.RequestException:
        console.print(f"[yellow]⚠️ تعذر الوصول إلى: {url}[/yellow]")
