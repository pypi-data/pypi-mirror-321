import requests
from rich.console import Console

console = Console()

def graphql_security_scanner(url, query, headers=None):
    """
    🔍 فحص أمان واجهات GraphQL.

    Args:
        url (str): رابط GraphQL endpoint.
        query (str): طلب GraphQL للاستعلام أو الفحص.
        headers (dict): رؤوس HTTP مخصصة يتم إرسالها مع الطلبات.

    Example:
        graphql_security_scanner(
            "https://example.com/graphql",
            "{ __schema { queryType { name } } }"
        )
    """
    if headers is None:
        headers = {
            "Content-Type": "application/json"
        }

    console.print(f"[cyan]🔍 بدء فحص GraphQL Endpoint: {url}[/cyan]")

    payload = {
        "query": query
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)

        if response.status_code == 200:
            console.print(f"[green][+] الوصول ممكن إلى: {url}[/green]")
            try:
                data = response.json()
                console.print("[green]✅ استجابة GraphQL:[/green]")
                console.print_json(data)
                # كشف مشاكل الأمان
                if "__schema" in data.get("data", {}):
                    console.print(f"[yellow]⚠️ قد تكون واجهة GraphQL تعرض معلومات حساسة ( introspection enabled ).[/yellow]")
            except ValueError:
                console.print(f"[yellow]⚠️ لا يمكن تحليل الاستجابة كـ JSON: {url}[/yellow]")
        elif response.status_code in [403, 401]:
            console.print(f"[yellow][⚠️] الوصول مرفوض أو يتطلب المصادقة: {url}[/yellow]")
        else:
            console.print(f"[red][❌] خطأ في الوصول ({response.status_code}): {url}[/red]")

    except requests.RequestException as e:
        console.print(f"[red]❌ فشل الوصول إلى: {url} | الخطأ: {e}[/red]")
