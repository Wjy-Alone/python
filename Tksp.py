import tkinter as tk
from lxml import etree
import requests
from urllib import parse

first_url = 'https://baike.baidu.com/item/'
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
def find():
    n = 0
    c = 0
    all_url = first_url+parse.quote(inp.get())
    html = requests.get(all_url,headers=headers)
    selector = etree.HTML(html.text)
    rezult_list = selector.xpath('//html/body/div[3]/div[2]/div/div[1]/div[4]/*/text()|//html/body/div[3]/div[2]/div/div[1]/div[4]/*/*/text()')
    rezult = ""
    for i in rezult_list:
        if ('[' in i) or ('\n' in i):
            #rezult_list.pop(i)
            pass
        else:
            rezult = rezult+i
    #print(rezult)
    rezult_list = list(rezult)
    #print(rezult_list)
    rezult = ''
    for i in rezult_list:
        n+=1
        rezult = rezult + i
        if n >= 20:
            rezult = rezult + '\n'
            n=0
            c+=1
        if c >= 10:
            window.geometry('600x500')
        else:
            window.geometry('500x400')
    if rezult == '':
        text.configure(text='Search Failed')
    else:
        text.configure(text=rezult)
window = tk.Tk()
window.geometry('500x400')
window.title("Search")
inp = tk.Entry(window,width=30)
inp.pack()
button = tk.Button(window,text='search',fg='green',command=find)
button.pack()
text = tk.Label(window,text='rezult',font=('microsoft yahei',15))
text.pack()
text2 = tk.Label(window,text='(source:百度百科,url:https://baike.baidu.com/)')
text2.pack()
tk.mainloop()
