'''
此之程式原作者：呂可弘哥哥

來源：http://lyukehong.blogspot.tw/

有興趣可以上去看看唷！

改編者：Jimmy

以下為我的程式日誌：

我是Jimmy，幫他稍微註解幾個重點和改編幾個內容，讓使用者知道如何使用

執行程式前:

1. 在執行此程式前，建議先安裝Anaconda(不建議直接安裝Python)
2. 在Anaconda的程式集中，有一個Anaconda Prompt，請點選右鍵，利用"系統管理用的身分執行"
3. 在裏頭輸入"pip install easygui"，顯示"成功"後，可執行本程式。

我修改的內容:

1. 將哥哥第一行程式刪除(# -*- coding: cp950 -*-)，因為跑起來有bug

2. 將ax+by=c,dx+ey=f 複製到所有程式，讓使用者更清楚瞭解到自己應該輸入什麼

3. 在每行程式後面新增註解，給未來有興趣了解卻不知道什麼意思的朋友們增加研究效率:)

4. 為了讓程式更簡潔，增加"def"之元素

5. 可弘哥哥解二元一次方程式的方法有bug，我用加減消去法自己改寫了一遍

此為他的解法：【有興趣可以挑戰看看debug】
dt=a*e-b*d
dtx=b*f-e*c
dty=a*f-d*c

'''

import easygui                                              #將"easygui"的視窗功能開啟
a=float(easygui.enterbox("ax+by=c,dx+ey=f   give me a"))    #從33~38行，皆為得到使用者輸入的答案
b=float(easygui.enterbox("ax+by=c,dx+ey=f   give me b"))
c=float(easygui.enterbox("ax+by=c,dx+ey=f   give me c"))
d=float(easygui.enterbox("ax+by=c,dx+ey=f   give me d"))
e=float(easygui.enterbox("ax+by=c,dx+ey=f   give me e"))
f=float(easygui.enterbox("ax+by=c,dx+ey=f   give me f"))

def 解二元一次方程式(a,b,c,d,e,f):
    if (a==d) and (b==e) and (c==f):
        easygui.msgbox(u'無限解')
    elif (a==d) and (b==e) and (c!=f):
        easygui.msgbox(u'無解')
    else:
        ad公倍數=float(a*d)                                         #加減消去法，未來有興趣可以去看我帶入消去法原理解說的程式唷！程式步入思考階段
        a式除幾=float(ad公倍數/a)
        d式除幾=float(ad公倍數/d)
        a=a*a式除幾
        b=b*a式除幾
        c=c*a式除幾
        d=d*d式除幾
        e=e*d式除幾
        f=f*d式除幾
        y係數=b-e
        y係數答案=c-f
        y=y係數答案/y係數
        bty=float(b*y)
        #ety=float(e*y)
        atx=float(c-bty)
        #dtx=f-ety
        x=float(atx/a)
        easygui.msgbox(u"x={}\ty={}".format(x,y))
    return
def main():
    解二元一次方程式(a,b,c,d,e,f)
    return 'Done!'
if __name__ == '__main__':
    main()