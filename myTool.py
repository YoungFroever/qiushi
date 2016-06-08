# -*- coding:utf-8 -*-
import re;
import sys;
reload(sys);
sys.setdefaultencoding('utf-8');
class myZhengze:
    removeQiuBai = re.compile('<div class="content">');
    removeDiv = re.compile('<div>|</div>')
    removeBr = re.compile('<br/>');
    #removeDiv = re.compile('<P>|<span class="copyright">|<P>')
    def __init__(self):
        return None;
    
    def myReplace(self,x):
        x = re.sub(self.removeQiuBai,"",x);
        x = re.sub(self.removeDiv,"",x);
        x = re.sub(self.removeBr,'',x);
        return x.strip();
    def writeToFile(self,filename,txt):
    	  # 'w'是覆盖模式 'a'是追加格式
        f = open(filename,'a');
        f.write(txt);
        f.write('\n')
        f.close();
     
        
