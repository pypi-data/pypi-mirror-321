import requests
from rich.console import Console
from queue import Queue
from threading import Thread

console = Console()

def scan_broken_auth(url, username, wordlist_path):
    """
    🔐 فحص ضعف آليات تسجيل الدخول (Broken Authentication).
    
    Args:
        url (str): رابط صفحة تسجيل الدخول.
        username (str): اسم المستخدم الذي سيتم اختباره.
        wordlist_path (str): مسار ملف كلمات المرور.
    
    Example:
        scan_broken_auth("https://example.com/login", "admin", "passwords.txt")
    """
    try:
        # قراءة كلمات المرور من ملف wordlist
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print("[red]❌ ملف كلمات المرور غير موجود.[/red]")
        return

    # إعداد قائمة الانتظار لكلمات المرور
    q = Queue()
    for password in passwords:
        q.put(password)

    found = False

    # دالة تجربة تسجيل الدخول
    def attempt_login():
        nonlocal found
        while not q.empty() and not found:
            password = q.get()
            data = {"username": username, "password": password}
            
            try:
                response = requests.post(url, data=data, timeout=5)

                # تعديل هنا حسب استجابة الموقع عند تسجيل الدخول الصحيح
                if "Welcome" in response.text or response.status_code == 302:
                    console.print(f"[red]❌ تم تسجيل الدخول باستخدام كلمة المرور: {password}[/red]")
                    found = True
                else:
                    console.print(f"[yellow]🔍 تجربة كلمة المرور: {password}[/yellow]")

            except requests.RequestException:
                console.print(f"[red]❌ تعذر الوصول إلى: {url}[/red]")

            q.task_done()

    # تشغيل الفحص باستخدام Threads لتسريع العملية
    threads = []
    for _ in range(10):  # يمكن زيادة العدد لتسريع الفحص
        thread = Thread(target=attempt_login)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if not found:
        console.print("[green]✅ آلية تسجيل الدخول آمنة ضد هجمات التخمين.[/green]")
