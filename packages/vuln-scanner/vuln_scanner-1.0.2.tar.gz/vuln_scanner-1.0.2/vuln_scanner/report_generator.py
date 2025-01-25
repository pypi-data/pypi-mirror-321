from fpdf import FPDF
from rich.console import Console
from datetime import datetime

console = Console()

class ReportGenerator:
    def __init__(self, report_name="vulnerability_report"):
        self.report_name = report_name
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_title(self, title):
        """إضافة عنوان التقرير"""
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=16, style="B")
        self.pdf.cell(200, 10, txt=title, ln=True, align="C")
        self.pdf.ln(10)

    def add_subtitle(self, subtitle):
        """إضافة عنوان فرعي"""
        self.pdf.set_font("Arial", size=14, style="B")
        self.pdf.cell(200, 10, txt=subtitle, ln=True, align="L")
        self.pdf.ln(8)

    def add_paragraph(self, text):
        """إضافة فقرة نصية"""
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, txt=text)
        self.pdf.ln(5)

    def add_table(self, headers, data):
        """إضافة جدول إلى التقرير"""
        self.pdf.set_font("Arial", size=12, style="B")
        self.pdf.set_fill_color(200, 220, 255)
        for header in headers:
            self.pdf.cell(40, 10, header, 1, 0, "C", fill=True)
        self.pdf.ln()

        self.pdf.set_font("Arial", size=12)
        for row in data:
            for item in row:
                self.pdf.cell(40, 10, str(item), 1)
            self.pdf.ln()

    def save_pdf(self):
        """حفظ التقرير كملف PDF"""
        filename = f"{self.report_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        self.pdf.output(filename)
        console.print(f"[green]✅ تم حفظ التقرير بنجاح: {filename}[/green]")

# استخدام مولد التقارير
def generate_vulnerability_report(results):
    """
    📝 إنشاء تقرير احترافي بالنتائج.

    Args:
        results (dict): قاموس يحتوي على نتائج الفحص.

    Example:
        results = {
            "عنوان التقرير": "تقرير فحص الثغرات",
            "النتائج": [
                {"الثغرة": "XSS", "الوصف": "ثغرة XSS مكتشفة", "الحالة": "غير آمنة"},
                {"الثغرة": "SQLi", "الوصف": "ثغرة SQL Injection غير مكتشفة", "الحالة": "آمنة"},
            ]
        }
        generate_vulnerability_report(results)
    """
    report = ReportGenerator(report_name="vulnerability_report")
    report.add_title(results.get("عنوان التقرير", "تقرير فحص الثغرات"))

    # إضافة تفاصيل الفحص
    if "النتائج" in results:
        report.add_subtitle("نتائج الفحص:")
        headers = ["الثغرة", "الوصف", "الحالة"]
        data = [[r["الثغرة"], r["الوصف"], r["الحالة"]] for r in results["النتائج"]]
        report.add_table(headers, data)

    report.save_pdf()
