# -*- coding:utf-8 -*-
import urllib;
import urllib2;
import re;
import myTool;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)';
headers = {'User-Agent':user_agent};

class Spider:

    def __init__(self):
    	  #默认网址
        self.url = "";
        self.tool = myTool.myZhengze();
        
    def getHtml(self,url):
        request = urllib2.Request(url,headers=headers);
        response = urllib2.urlopen(request);
        #此处更改网站编码方式
        return response.read().decode('utf-8');
    def getInfo(self,html):
    	  #初步取出
        iden = '<div class="content">.*?</div>';
        
        temp = re.compile(iden,re.S);
        result = re.findall(temp,html);
        for item in result:
            middle = self.tool.myReplace(item);
            hahah = self.tool.writeToFile('端午节快乐.txt',middle);
            print middle;
        
        return result;
        
    def getPic(self,html):
        idenPic = '<img src=.*?.jpg';
        tempPic = re.compile(idenPic,re.S);
        result = re.findall(tempPic,html);
        x = 0;
        for item in result:
            removeSome = re.compile('<img src="|"');
            middle = re.sub(removeSome,'',item);
            middle.strip();
            getjpgName = re.compile('http://.*?com|\/.*?\/')
            urllib.urlretrieve(middle,'%s.jpg' % x);
            x+=1;
            print middle;
        return result;
          
spider = Spider();
a = spider.getHtml('http://www.qiushibaike.com/hot/1');
#print a;
b = spider.getInfo(a);
c = spider.getPic(a);
#print b;