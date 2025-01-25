import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import threading
from queue import Queue
from rich.console import Console
import re

console = Console()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# ✅ دالة لتصحيح الروابط
def fix_url(url):
    parsed = urlparse(url)
    fixed_path = re.sub(r'/{2,}', '/', parsed.path)
    return f"{parsed.scheme}://{parsed.netloc}{fixed_path}"

# 🔍 فحص الملفات الحساسة
def check_sensitive_files(url):
    sensitive_paths = [
        "/robots.txt", "/sitemap.xml", "/.well-known/security.txt",
        "/admin/", "/login/", "/dashboard/", "/config/", "/database/",
        "/backup/", "/uploads/", "/includes/", "/private/", "/hidden/",
        "/.git/", "/.env", "/.htaccess", "/server-status",
        "/phpinfo.php", "/test.php", "/info.php",
        "/dev/", "/staging/", "/temp/", "/logs/",
        "/data/", "/db/", "/core/", "/old/",
        "/backup.zip", "/backup.tar.gz", "/db.sql", "/config.php.bak"
    ]
    
    found_files = []
    for path in sensitive_paths:
        full_url = urljoin(url, path)
        fixed_url = fix_url(full_url)
        try:
            response = requests.get(fixed_url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                console.print(f"[green][+] تم العثور على: {fixed_url}[/green]")
                found_files.append(fixed_url)
        except requests.exceptions.RequestException:
            pass
    return found_files

# 🔐 Bruteforce للمجلدات
def brute_force_dirs(url, wordlist):
    try:
        with open(wordlist, 'r', encoding='utf-8') as file:
            directories = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print("[red]❌ ملف قائمة الكلمات غير موجود.[/red]")
        return []

    q = Queue()
    for directory in directories:
        q.put(directory)

    found_dirs = []

    def check_directory():
        while not q.empty():
            directory = q.get()
            full_url = urljoin(url, directory)
            fixed_url = fix_url(full_url)
            try:
                response = requests.get(fixed_url, headers=HEADERS, timeout=5)
                if response.status_code == 200:
                    console.print(f"[green][+] تم العثور على: {fixed_url}[/green]")
                    found_dirs.append(fixed_url)
            except:
                pass
            q.task_done()

    threads = []
    for _ in range(30):
        thread = threading.Thread(target=check_directory)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return found_dirs

# 🕷️ استخراج الروابط من الصفحة
def extract_links(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()

        for tag in soup.find_all(["a", "link", "script", "img"]):
            href = tag.get("href") or tag.get("src")
            if href:
                full_url = urljoin(url, href)
                fixed_url = fix_url(full_url)
                if urlparse(fixed_url).netloc == urlparse(url).netloc:
                    links.add(fixed_url)
        return links
    except requests.exceptions.RequestException:
        return set()

# 🔍 دالة الفحص الرئيسية
def hidden_link_finder(url, wordlist):
    console.print(f"[yellow]🔍 بدء البحث عن الروابط الحساسة في {url}...[/yellow]")

    all_links = set()

    # 📂 فحص الملفات الحساسة
    console.print("[cyan]📂 فحص الملفات الحساسة...[/cyan]")
    sensitive_files = check_sensitive_files(url)
    all_links.update(sensitive_files)

    # 🕷️ استخراج الروابط من الصفحة
    console.print("[cyan]🕷️ تحليل الموقع لاستخراج الروابط...[/cyan]")
    page_links = extract_links(url)
    all_links.update(page_links)

    # 🛠️ Bruteforce
    console.print("[cyan]🛠️ تشغيل Bruteforce...[/cyan]")
    brute_dirs = brute_force_dirs(url, wordlist)
    all_links.update(brute_dirs)

    # ✅ عرض النتائج
    if all_links:
        console.print(f"\n[bold green]✅ الروابط المكتشفة:[/bold green]")
        for link in all_links:
            console.print(f"[green]{link}[/green]")

        with open("sensitive_links_results.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(all_links))
        console.print("[cyan]📄 تم حفظ النتائج في [bold]sensitive_links_results.txt[/bold][/cyan]")
    else:
        console.print("[red]❌ لم يتم العثور على أي روابط حساسة.[/red]")
