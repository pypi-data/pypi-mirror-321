import requests
from threading import Thread
from queue import Queue
from rich.console import Console

console = Console()

def subdomain_scanner(domain, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print("[red]❌ ملف قائمة النطاقات الفرعية غير موجود.[/red]")
        return

    q = Queue()
    for sub in subdomains:
        q.put(f"http://{sub}.{domain}")
        q.put(f"https://{sub}.{domain}")

    found_subdomains = []

    def check_subdomain():
        while not q.empty():
            subdomain = q.get()
            try:
                response = requests.get(subdomain, timeout=3)
                if response.status_code == 200:
                    console.print(f"[green][+] تم العثور على نطاق فرعي فعال: {subdomain}[/green]")
                    found_subdomains.append(subdomain)
            except requests.RequestException:
                pass
            q.task_done()

    threads = []
    for _ in range(20):
        thread = Thread(target=check_subdomain)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if found_subdomains:
        with open("subdomains_results.txt", "w") as file:
            file.write("\n".join(found_subdomains))
        console.print("[cyan]📄 تم حفظ النتائج في [bold]subdomains_results.txt[/bold][/cyan]")
    else:
        console.print("[yellow]⚠️ لم يتم العثور على نطاقات فرعية نشطة.[/yellow]")
