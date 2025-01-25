import requests
from urllib.parse import urljoin
from rich.console import Console

console = Console()

def scan_file_upload(upload_url, base_url=None, file_types=None):
    """
    🔍 فحص نقاط رفع الملفات لاكتشاف الثغرات.

    Args:
        upload_url (str): رابط صفحة رفع الملفات.
        base_url (str): الرابط الأساسي للموقع لمحاولة الوصول للملف المرفوع.
        file_types (dict): قاموس بأنواع الملفات المراد تجربتها مع محتواها.

    Example:
        scan_file_upload("https://example.com/upload", "https://example.com/uploads/")
    """
    # أنواع الملفات الافتراضية إذا لم يتم تحديدها
    if file_types is None:
        file_types = {
            "php": "<?php echo 'Vulnerable'; ?>",
            "asp": "<% Response.Write(\"Vulnerable\") %>",
            "jsp": "<% out.println(\"Vulnerable\"); %>",
            "html": "<h1>Test Upload</h1>",
            "exe": "MZP",
        }

    console.print(f"[cyan]🔍 بدء فحص رفع الملفات في: {upload_url}[/cyan]")

    for extension, content in file_types.items():
        filename = f"vuln_test.{extension}"
        files = {'file': (filename, content)}

        try:
            response = requests.post(upload_url, files=files, timeout=10)

            # التحقق من استجابة رفع الملف
            if response.status_code in [200, 201]:
                console.print(f"[yellow]⚠️ قد يكون الموقع عرضة لرفع ملفات {extension}: {upload_url}[/yellow]")

                # محاولة الوصول إلى الملف المرفوع إذا تم توفير base_url
                if base_url:
                    file_url = urljoin(base_url, filename)
                    verify_upload(file_url, extension)
            elif response.status_code == 403:
                console.print(f"[green]✅ رفع ملفات {extension} مرفوض: {upload_url}[/green]")
            else:
                console.print(f"[green]✅ الموقع يبدو آمناً ضد رفع ملفات {extension}[/green]")

        except requests.RequestException:
            console.print(f"[red]❌ تعذر الوصول إلى: {upload_url}[/red]")


def verify_upload(file_url, extension):
    """
    🔎 التحقق من الوصول إلى الملف المرفوع.

    Args:
        file_url (str): الرابط المحتمل للملف المرفوع.
        extension (str): امتداد الملف المرفوع.
    """
    try:
        response = requests.get(file_url, timeout=5)
        if response.status_code == 200:
            console.print(f"[red]❌ الملف المرفوع متاح للوصول: {file_url}[/red]")
        else:
            console.print(f"[green]✅ الملف {extension} غير متاح للوصول: {file_url}[/green]")
    except requests.RequestException:
        console.print(f"[yellow]⚠️ تعذر الوصول إلى الملف المرفوع: {file_url}[/yellow]")
