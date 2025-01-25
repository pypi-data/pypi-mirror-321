import requests
from rich.console import Console

console = Console()

def scan_cors(target_url, origin_url):
    """
    🔎 فحص إعدادات CORS للموقع المستهدف مع Origin مخصص.

    Args:
        target_url (str): رابط الموقع الذي سيتم فحصه.
        origin_url (str): رابط Origin الذي سيتم استخدامه في الطلب.

    Example:
        scan_cors("https://example.com", "http://test.com")
    """
    headers = {
        "Origin": origin_url
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        
        # فحص إعدادات Access-Control-Allow-Origin
        if 'Access-Control-Allow-Origin' in response.headers:
            allowed_origin = response.headers['Access-Control-Allow-Origin']
            if allowed_origin == '*':
                console.print(f"[red]❌ إعدادات CORS غير آمنة في: {target_url}[/red]")
            elif allowed_origin == origin_url:
                console.print(f"[yellow]⚠️ إعدادات CORS تسمح بـ Origin المحدد: {origin_url} في {target_url}[/yellow]")
            else:
                console.print(f"[green]✅ إعدادات CORS آمنة في: {target_url}[/green]")
        else:
            console.print(f"[green]✅ إعدادات CORS آمنة في: {target_url}[/green]")

        # فحص Access-Control-Allow-Credentials
        if 'Access-Control-Allow-Credentials' in response.headers:
            console.print(f"[yellow]⚠️ الموقع يسمح بإرسال Cookies عبر CORS في: {target_url}[/yellow]")

    except requests.RequestException:
        console.print(f"[yellow]⚠️ تعذر الوصول إلى: {target_url}[/yellow]")
