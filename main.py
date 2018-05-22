import urllib
import urllib.request
import re
def download(url, path, id):
    pagedata = urllib.request.urlopen(url + str(id)).read()
    file=open( path+ str(id) + ".html","wb") #写入二进制
    file.write(pagedata)
    file.close()

url = "https://www.luogu.org/problemnew/show/P"
for i in range(1000, 4624):
    print("正在下载第" + str(i) + "题...")
    download(url, r"C:\Users\LJY\Desktop\dd\\", i)
