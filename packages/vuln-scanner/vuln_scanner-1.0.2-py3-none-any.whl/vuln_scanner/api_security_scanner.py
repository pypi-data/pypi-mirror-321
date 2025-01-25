import requests
from rich.console import Console

console = Console()

def api_security_scanner(base_url, endpoints, headers=None):
    """
    🔍 فحص أمان واجهات برمجة التطبيقات (API).

    Args:
        base_url (str): الرابط الأساسي للـ API.
        endpoints (list): قائمة بالنقاط النهائية (endpoints) التي سيتم فحصها.
        headers (dict): رؤوس HTTP مخصصة يتم إرسالها مع الطلبات.

    Example:
        api_security_scanner(
            "https://api.example.com",
            ["/login", "/user", "/admin"],
            {"Authorization": "Bearer <token>"}
        )
    """
    if headers is None:
        headers = {}

    console.print(f"[cyan]🔍 بدء فحص أمان واجهات API: {base_url}[/cyan]")

    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url, headers=headers, timeout=5)

            # فحص الاستجابة
            if response.status_code == 200:
                console.print(f"[green][+] الوصول ممكن: {url}[/green]")
            elif response.status_code == 401:
                console.print(f"[yellow][⚠️] يتطلب المصادقة: {url}[/yellow]")
            elif response.status_code == 403:
                console.print(f"[yellow][⚠️] الوصول محظور: {url}[/yellow]")
            else:
                console.print(f"[red][❌] خطأ في الوصول ({response.status_code}): {url}[/red]")

            # تحليل محتوى الرد إذا كان نصياً
            if response.headers.get("Content-Type", "").startswith("application/json"):
                try:
                    json_data = response.json()
                    if isinstance(json_data, dict) and "error" in json_data:
                        console.print(f"[yellow]⚠️ تم الكشف عن خطأ في الرد: {json_data['error']}[/yellow]")
                except ValueError:
                    console.print(f"[yellow]⚠️ لا يمكن تحليل الرد كـ JSON: {url}[/yellow]")

        except requests.RequestException as e:
            console.print(f"[red]❌ فشل الوصول إلى: {url} | الخطأ: {e}[/red]")

