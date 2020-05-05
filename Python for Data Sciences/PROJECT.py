import xlsxwriter
import urllib.request
import requests
from bs4 import BeautifulSoup
req = urllib.request.Request( "http://www.team4adventure.com/tours", data=None, 
             headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } 
                                      ) 
f = urllib.request.urlopen(req)
s = f.read()
soup = BeautifulSoup(s)
a = soup.find(class_ = 'row')
link = a.find_all('a')

#print(a)

print(link)
for l in link:
	names = l.contents[0]
	links = l.get('href')
	print(links)
	print(names)

workbook = xlsxwriter.Workbook('module.xlsx')
worksheet = workbook.add_worksheet('SEO')
row = 0
col = 0

worksheet.write(row,0,'Links')
worksheet.write(row,1,'Names')

worksheet.write(row, 2, "Keyword1(Kayaking)")
worksheet.write(row, 3, "Keyword2(Expedition)")
worksheet.write(row, 4, "Keyword3(Treks)")
worksheet.write(row, 5, "Density(keyword1)")
worksheet.write(row, 6, "Density(keyword2)")
worksheet.write(row, 7, "Density(keyword3)")

row = 1
for l in link:
    names = l.contents[0]
    links = l.get('href')
    print(links)
    print(names)
    worksheet.write(row, col, links)
    worksheet.write(row, col+1, names)

    req1 = requests.get(links)
    data = req1.text
    s1 = BeautifulSoup(data, "lxml")
    text = s1.get_text()
    t1 = text.split()
    #print(t1)
    a = len(text)
    print(a)

    k1 = 'kayaking'
    k2 = 'expedition'
    k3 = 'treks'

    calkeyword1 = text.count(k1)
    calkeyword2 = text.count(k2)
    calkeyword3 = text.count(k3)
    worksheet.write(row, col+2, calkeyword1)
    worksheet.write(row, col+3, calkeyword2)
    worksheet.write(row, col+4, calkeyword3)

    print(calkeyword1)
    print(calkeyword2)
    print(calkeyword3)

    density1 = calkeyword1/a
    worksheet.write(row, col+5, density1)
    print(density1)
    density2 = calkeyword2/a
    worksheet.write(row, col+6, density2)
    print(density2)
    density3 = calkeyword3/a
    worksheet.write(row, col+7, density3)
    print(density3)
    row = row+1

chart1 = workbook.add_chart({'type':'column'})
chart1.set_x_axis({'name':'Density of SEO Keywords'})
chart1.set_title({'name':'SEARCH ENGINE OPTIMIZATION'})
heading = workbook.add_format({'bold':True, 'font_color':'red'})
chart1.add_series({'values':'=SEO!$C2:$C20'})
chart1.add_series({'values':'=SEO!$D2:$D20'})
chart1.add_series({'values':'=SEO!$E2:$E20'})
worksheet.insert_chart('L20',chart1)

workbook.close()

    




    





