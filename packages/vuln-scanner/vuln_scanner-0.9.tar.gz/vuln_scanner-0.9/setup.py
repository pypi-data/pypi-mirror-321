from setuptools import setup, find_packages

setup(
    name='vuln_scanner',
    version='0.9',
    author='ALMHEB',
    author_email='appasqw107@gmail.com',
    description='مكتبة Python لفحص واكتشاف الثغرات الأمنية مثل XSS، SQL Injection، LFI، RFI، والفحص المتقدم للملفات الحساسة والنطاقات الفرعية.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AL-MHIB/vuln_scanner',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'rich'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
