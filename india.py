import csv
import lxml.html

url1='http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition=6;orderby=start;'
url2 ='page='
url3 ='size=100;team=30;template=results;type=team;view=results'
url5 = ['http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition=6;orderby=start;size=100;team=30;template=results;type=team;view=results']

#2=australia
#4=west indies
#7=pakistan
#3=south africa
#9=zimbabwe
#29=ireland
#27=UAE
#1=england
#8=sri lanka
#25=bangladesh
#5=newzealand
#40=afghanistan
#30=scotland


for i in range(1,3):   #Mention the upper and lower limits
    url4 = url1 + url2 + str(i) + ';' + url3
    url5.append(url4)
data = open('ODI_ind_vs_scotland.csv','wb',)
out = csv.writer(data)
out.writerow(('Team', 'Result','Margin', 'Toss', 'Bat','Opposition','Ground','Date'))
for page in url5:
    teamsss = []
    resultsss = []
    marginsss = []
    tosssss = []
    batsss = []
    oppsss = []
    groundsss = []
    datesss = []

    content = lxml.html.parse(page)
    
    team = content.xpath('//tr[@class="data1"]/td[1]/a')
    result = content.xpath('//tr[@class="data1"]/td[2]')
    margin = content.xpath('//tr[@class="data1"]/td[3]')
    toss = content.xpath('//tr[@class="data1"]/td[5]')
    bat = content.xpath('//tr[@class="data1"]/td[6]')
    opp = content.xpath('//tr[@class="data1"]/td[8]/a')
    ground = content.xpath('//tr[@class="data1"]/td[9]/a')
    date = content.xpath('//tr[@class="data1"]/td[10]/b')
    #strike = content.xpath('//tr[@class="data1"]/td[7]')
    #inns = content.xpath('//tr[@class="data1"]/td[8]')
    #oppos = content.xpath('//tr[@class="data1"]/td[10]/a')

    team1 = [t.text for t in team]
    results = [r.text for r in result]
    margins = [m.text for m in margin]
    tosss = [tosses.text for tosses in toss]
    bats = [first.text for first in bat]
    opposition = [oppose.text for oppose in opp]
    gr = [g.text for g in ground]
    dates = [d.text for d in date]
    #str_rat = [srt.text for srt in strike]
    #inngs = [inn.text for inn in inns]
    #oppos = [opp.text for opp in oppos]

    teamsss.extend(team1)
    resultsss.extend(results)
    marginsss.extend(margins)
    tosssss.extend(tosss)
    batsss.extend(bats)
    oppsss.extend(opposition)
    groundsss.extend(gr)
    datesss.extend(dates)
    #strike_rate.extend(str_rat)
    #innings.extend(inngs)
    #opposition.extend(oppos)

    zipped = zip(teamsss,resultsss,marginsss,tosssss,batsss,oppsss,groundsss,datesss)
    for row in zipped:
        out.writerow(row)
        zipped = None
data.close()
