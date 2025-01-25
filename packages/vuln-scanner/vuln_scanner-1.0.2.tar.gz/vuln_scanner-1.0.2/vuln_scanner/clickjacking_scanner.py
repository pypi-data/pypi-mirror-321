import requests
from rich.console import Console

console = Console()

def scan_clickjacking(url):
    """
    🔍 فحص الحماية من هجمات النقر المخادع (Clickjacking).

    Args:
        url (str): رابط الموقع الذي سيتم فحصه.

    Example:
        scan_clickjacking("https://example.com")
    """
    console.print(f"[cyan]🔍 بدء فحص Clickjacking في: {url}[/cyan]")

    try:
        # إرسال طلب GET إلى الموقع
        response = requests.get(url, timeout=5)

        # التحقق من وجود الرأس X-Frame-Options
        x_frame_options = response.headers.get("X-Frame-Options", "").lower()
        content_security_policy = response.headers.get("Content-Security-Policy", "")

        if "deny" in x_frame_options or "sameorigin" in x_frame_options:
            console.print(f"[green]✅ الموقع محمي برأس X-Frame-Options: {x_frame_options}[/green]")
        elif "frame-ancestors" in content_security_policy:
            console.print(f"[green]✅ الموقع محمي برأس Content-Security-Policy: {content_security_policy}[/green]")
        else:
            console.print(f"[red]❌ الموقع غير محمي ضد Clickjacking: {url}[/red]")
            console.print("[yellow]⚠️ يُنصح باستخدام X-Frame-Options أو Content-Security-Policy لتأمين الموقع.[/yellow]")

    except requests.RequestException as e:
        console.print(f"[red]❌ تعذر الوصول إلى: {url} | الخطأ: {e}[/red]")
