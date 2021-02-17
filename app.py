import tkinter as tk
import tkinter.ttk as ttk
import urllib.request

id = 'https://www.investing.com/currencies/chf-huf'

i = urllib.request.urlopen(id)
page_content = str(i.read())
forint_index = page_content.find(
    '<span class="arial_26 inlineblock pid-90-last" id="last_last" dir="ltr">')
iban_rate = page_content[forint_index + 1:forint_index+6]

print(iban_rate)
