import os
import os.path

try:
    from urllib.parse import quote
except:
    from urllib import quote

cdir = r'C:\Users\Sabrina\Documents\StayGoldSpa\code' # Directory of files txt .

#os.listdir('.')
#os.listdir(cdir)

arch_in  = cdir + '\\' + 'kwords.txt'
arch_out = cdir + '\\' + 'kwords-urls.txt'

url_a = 'https://www.google.com.ar/search?num=100&q='
url_b = '&uule=w+CAIQICIjQnVlbm9zIEFpcmVzLEJ1ZW5vcyBBaXJlcyxBcmdlbnRpbmE&lr=lang_es&ie=UTF-8'

with open(arch_in, 'r',encoding='UTF-8') as rf:
    with open(arch_out, 'w',encoding='UTF-8') as wf:
        for line in rf:
            lin = line.strip()
            lin = quote(lin)
            lin = lin.replace('%20','+')
            lin = url_a + lin + url_b + '\n'
            wf.write(lin)

rf.close()
wf.close()


#url = "http://earth.google.com/gallery/kmz/women_for_women.kmz?a=large"
# Python 2
#urllib.quote_plus(url)
# Python 3
#urllib.quote_plus(url)
