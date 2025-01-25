import requests
from rich.console import Console
from urllib.parse import urljoin

console = Console()

def admin_panel_finder(url, wordlist_path):
    """
    🔍 البحث عن لوحات التحكم الإدارية المكشوفة.

    Args:
        url (str): رابط الموقع الأساسي.
        wordlist_path (str): مسار قائمة الكلمات التي تحتوي على أسماء المسارات المحتملة.

    Example:
        admin_panel_finder("https://example.com", "admin_paths.txt")
    """
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            paths = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print("[red]❌ ملف قائمة المسارات غير موجود![/red]")
        return

    console.print(f"[cyan]🔍 بدء البحث عن لوحات التحكم الإدارية في: {url}[/cyan]")

    found_panels = []
    
    for path in paths:
        full_url = urljoin(url, path)
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                console.print(f"[green][+] تم العثور على لوحة تحكم إدارية في: {full_url}[/green]")
                found_panels.append(full_url)
            elif response.status_code in [403, 401]:
                console.print(f"[yellow][⚠️] لوحة محمية أو محظورة: {full_url}[/yellow]")
        except requests.RequestException:
            console.print(f"[yellow]⚠️ تعذر الوصول إلى: {full_url}[/yellow]")
    if found_panels:
        with open("admin_panels_results.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(found_panels))
        console.print(f"[cyan]📄 تم حفظ النتائج في ملف: [bold]admin_panels_results.txt[/bold][/cyan]")
    else:
        console.print("[red]❌ لم يتم العثور على أي لوحات تحكم إدارية مكشوفة.[/red]")
