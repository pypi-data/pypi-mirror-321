import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from rich.console import Console

console = Console()

def scan_open_redirect(url):
    """
    🔎 فحص ثغرات إعادة التوجيه المفتوح (Open Redirect).
    
    Args:
        url (str): رابط الموقع الذي سيتم فحصه.
    
    Example:
        scan_open_redirect("https://example.com/redirect?url=https://google.com")
    """
    payloads = [
        "https://evil.com",
        "//evil.com",
        "/\\evil.com",
        "https://evil.com%2F..",
        "http://evil.com",
    ]

    try:
        # استخراج باراميترات URL
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # التأكد من وجود باراميترات قد تحتوي على روابط
        vulnerable_params = ["url", "redirect", "next", "dest", "destination", "redir"]
        target_params = [param for param in query_params if param.lower() in vulnerable_params]

        if not target_params:
            console.print(f"[yellow]⚠️ لا توجد باراميترات يُحتمل استغلالها في {url}[/yellow]")
            return

        console.print(f"[cyan]🔍 بدء الفحص على {url}...[/cyan]")

        for param in target_params:
            for payload in payloads:
                # استبدال القيمة الحالية بالـ payload
                modified_params = query_params.copy()
                modified_params[param] = payload

                # إعادة بناء الرابط
                new_query = urlencode(modified_params, doseq=True)
                vulnerable_url = urlunparse(parsed_url._replace(query=new_query))

                try:
                    response = requests.get(vulnerable_url, timeout=5, allow_redirects=False)

                    # التحقق من إذا كان الرابط يقوم بإعادة التوجيه
                    if response.status_code in [301, 302, 303, 307, 308]:
                        location = response.headers.get("Location", "")
                        if payload in location:
                            console.print(f"[red]❌ ثغرة Open Redirect تم اكتشافها في: {vulnerable_url}[/red]")
                        else:
                            console.print(f"[green]✅ الرابط آمن من إعادة التوجيه المفتوح: {vulnerable_url}[/green]")
                    else:
                        console.print(f"[green]✅ الرابط آمن من إعادة التوجيه المفتوح: {vulnerable_url}[/green]")

                except requests.RequestException:
                    console.print(f"[yellow]⚠️ تعذر الوصول إلى: {vulnerable_url}[/yellow]")

    except Exception as e:
        console.print(f"[red]❌ حدث خطأ أثناء الفحص: {e}[/red]")
