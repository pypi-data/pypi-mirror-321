from distutils.core import setup

packages = ['txdpy']
setup(name='txdpy',
    version='10.9.14',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'},
    install_requires=[
        "lxml","loguru","tqdm","colorama","openpyxl","pymysql","xlsxwriter","xlrd","sshtunnel","file_ls","requests","fuzzywuzzy","PyMuPDF","pdfplumber","bs4"
    ])