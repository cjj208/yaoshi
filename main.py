import pyautogui
import time
import cv2 as cv
import numpy as np
import os
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import webbrowser

#os.chdir(r"D:\Python_projects\trade_projects\opencv_projects\药师公需项目")

def retxy(screen=(0, 0, 1920, 1080), templateimg="B.png", ):
    screenshot = ImageGrab.grab(bbox=screen)
    screenshot = np.array(screenshot)

    img_rgb = screenshot
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(templateimg, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    postion = []
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        p = (pt[0]+w*0.5,pt[1]+h*0.5,)
        postion.append(p)
        #print(pt)


    return postion

def clicking(px=1213,py=18):
    time.sleep(0.5)
    pyautogui.moveTo(x=px, y=py, )
    time.sleep(0.3)
    pyautogui.click()

    time.sleep(0.5)
def postion():
    try:
        while True:
            x, y = pyautogui.position()
            print("x=%s  y=%s"%(x, y))
    except KeyboardInterrupt:
        print('\nExit.')
def openurl():


    url = "https://stu.chinahrt.com/index.html#/pharmacist/index"
    chromepath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    webbrowser.get('chrome').open(url)
def backhome():
    clicking(px=1919, py=300)  # 鼠标移至右侧滑条
    pyautogui.scroll(1000)  # 移至最上层
    down = 0  # 执行15次向下键
    while down < 15:
        time.sleep(0.1)
        pyautogui.press('down')
        down += 1


def doit():

    topl = 544
    botr = 365
    qudati = retxy((0, 0, 1920, 1080),templateimg="qudati.png",)

    duoxuan = retxy((topl, botr, 1303, 631),templateimg="duoxuan.png",)
    duoxuan2 = retxy((topl, botr, 1303, 631), templateimg="duoxuan2.png", )

    gohome = retxy((0, 0, 1920, 1080), templateimg="homepage.png", )
    dangxuan = retxy((0, 0, 1920, 1080), templateimg="danxuan.png", )
    panduan = retxy((0, 0, 1920, 1080), templateimg="panduan.png", )
    if len(qudati)>0:
        print ("进入判断题%s"%qudati)
        x = qudati[0][0]
        y = qudati[0][1]
        clicking(px=x, py=y)

    if len(panduan)>0:
        #选对]: a664 533
        duil = 620
        duib = 518
        dui = retxy((duil, duib, 870, 700), templateimg="dui.png", )
        
        duipostion = (dui[0][0] + duil,dui[0][1] + duib)


        if len(dui)>0:#选对 提交
            clicking(px=duipostion[0], py=duipostion[1])

            time.sleep(1)
            # 提交
            tijiaol = 550
            tijiaob = 550
            tijiao = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
            tijiaox = tijiao[0][0] + tijiaol
            tijiaoy = tijiao[0][1] + tijiaob

            time.sleep(1)
            clicking(px=tijiaox, py=tijiaoy)
            time.sleep(1)

        #如果作对了，就点返回首页

            panduancuowu = retxy((duil, duib, 1363, 801), templateimg="panduancuowu.png", )
            if len(panduancuowu)>0:
                time.sleep(1)
                cuo = retxy((duil, duib, 870, 700), templateimg="cuo.png", )
                cuopostion = (cuo[0][0] + duil, cuo[0][1] + duib)

                clicking(px=cuopostion[0], py=cuopostion[1])
                time.sleep(1)
                #提交
                tijiaol = 550
                tijiaob = 550
                tijiao = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
                tijiaox = tijiao[0][0] + tijiaol
                tijiaoy = tijiao[0][1] + tijiaob

                time.sleep(1)
                clicking(px=tijiaox, py=tijiaoy)
                time.sleep(1)

        pb = retxy((topl, botr, 1363, 801), templateimg="huanhui.png", )
        pbx = pb[0][0] + topl
        pby = pb[0][1] + botr
        print("xy", pbx, pby)
        clicking(px=pbx, py=pby)
        time.sleep(1)




    if len(dangxuan)>0  :

        #选A
        pa = retxy((topl, botr, 1363, 801),templateimg="A.png",)
        pax = pa[0][0]+topl
        pay = pa[0][1]+botr
        # print ("xy",pax,pay)
        clicking(px=pax, py=pay)
        #提交

        tijiaol = 550
        tijiaob = 550
        tijiao = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
        tijiaox = tijiao[0][0] + tijiaol
        tijiaoy = tijiao[0][1] + tijiaob
        # print(tijiaox, tijiaoy)  # 953.0 699.5
        clicking(px=tijiaox, py=tijiaoy)

        # 如果通过则返回首页
        tongguo = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
        time.sleep(0.5)
        if len(tongguo)>0:

            pb = retxy((topl, botr, 1363, 801), templateimg="huanhui.png", )
            pbx = pb[0][0] + topl
            pby = pb[0][1] + botr
            # print("xy", pbx, pby)
            clicking(px=pbx, py=pby)


        if len(retxy((topl, botr, 1363, 801),templateimg="cuowu.png",))>0:
            # 选B
            pb = retxy((topl, botr, 1363, 801), templateimg="B.png", )
            pbx = pb[0][0] + topl
            pby = pb[0][1] + botr
            # print("xy", pbx, pby)
            clicking(px=pbx, py=pby)
            #提交

            # 提交
            tijiaol = 550
            tijiaob = 550
            tijiao = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
            tijiaox = tijiao[0][0] + tijiaol
            tijiaoy = tijiao[0][1] + tijiaob
            # print(tijiaox, tijiaoy)  # 953.0 699.5
            clicking(px=tijiaox, py=tijiaoy)
            # 返回首页

            pb = retxy((topl, botr, 1363, 801), templateimg="huanhui.png", )
            pbx = pb[0][0] + topl
            pby = pb[0][1] + botr
            # print("xy", pbx, pby)
            clicking(px=pbx, py=pby)
    if len(duoxuan) > 0 or len(duoxuan2) > 0 :

        # 选A
        pa = retxy((topl, botr, 1363, 801), templateimg="A.png", )
        pax = pa[0][0] + topl
        pay = pa[0][1] + botr
        print("xy", pax, pay)
        clicking(px=pax, py=pay)

        # 选B
        pb = retxy((topl, botr, 1363, 801), templateimg="B.png", )
        pbx = pb[0][0] + topl
        pby = pb[0][1] + botr
        print("xy", pbx, pby)
        clicking(px=pbx, py=pby)
        # 选C
        cb = retxy((topl, botr, 1363, 801), templateimg="C.png", )


        if len(cb) > 0:

            cx = cb[0][0] + topl
            cy = cb[0][1] + botr
            print("xy", cx, cx)
            clicking(px=cx, py=cy)
        # 选C
        xuanD = retxy((topl, botr, 1363, 801), templateimg="D.png", )
        if len(xuanD)>0:
            xuanDx = xuanD[0][0] + topl
            xuanDy = xuanD[0][1] + botr
            clicking(px=xuanDx, py=xuanDy)


        # 提交
        tijiaol = 550
        tijiaob = 550
        tijiao = retxy((tijiaol, tijiaob, 1363, 801), templateimg="tijiao.png", )
        tijiaox = tijiao[0][0] + tijiaol
        tijiaoy = tijiao[0][1] + tijiaob
        print(tijiaox, tijiaoy)  # 953.0 699.5
        clicking(px=tijiaox, py=tijiaoy)


        # 返回首页

        pb = retxy((topl, botr, 1363, 801), templateimg="huanhui.png", )
        pbx = pb[0][0] + topl
        pby = pb[0][1] + botr
        print("xy", pbx, pby)
        clicking(px=pbx, py=pby)
        time.sleep(1)


if __name__ == "__main__":
    openurl()#打开网站
    login = False
    strinput = input("是否已完成登陆,请输入y或n!")
    if strinput == "y" or strinput == "Y":
        print ("程序继续")
        login = True
    else:
        login = False

        print ("程序退出")
    if login == True:

        backhome()
        time.sleep(1)
        #截图并指定预计时长的位置并找到
        clickxy = retxy((0, 0, 1920, 1080),templateimg="yujishichan.png",)

        list(range(len(clickxy)))
        print("今天总共有%s个任务"%len(clickxy))
        if len(clickxy)>0:
            for i in clickxy:
                backhome()
                #print (i)
                x = i[0]
                y = i[1]
                clicking(px=x, py=y)
                time.sleep(1)
                '''
                做题的规则写在这里！这里做点修改！
                ！！
                '''

                wancheng = retxy((0, 0, 1920, 1080), templateimg="wancheng.png", )

                if len(wancheng)==0:

                    while True:
                        print ('等待完成...')
                        time.sleep(1)

                        startdo = len(retxy((0, 0, 1920, 1080), templateimg="startdo.png", )) > 0
                        videodoover = len(retxy((0, 0, 1920, 1080), templateimg="videodoover.png", )) > 0
                        shiping = retxy((0, 0, 1920, 1080), templateimg="shiping.png", )
                        wenzhang = retxy((0, 0, 1920, 1080), templateimg="wenzhang.png", )
                        budati = retxy((0, 0, 1920, 1080), templateimg="budati.png", )
                        qudati2 = retxy((0, 0, 1920, 1080), templateimg="qudati2.png", )
                        time.sleep(1)
                        if startdo>0:#当跳出答题卡，进行以下操作
                            if len(wenzhang)>0:#如果是文章列表
                                if len(budati) > 0:
                                    print(budati)
                                    x = budati[0][0]
                                    y = budati[0][1]
                                    clicking(px=x, py=y)
                                    time.sleep(2)

                                if len(qudati2) > 0:

                                    x = qudati2[0][0]
                                    y = qudati2[0][1]
                                    clicking(px=x, py=y)

                                doit()####
                                break
                            if len(shiping)>0:#如果是视频

                                clicking(px=1919, py=300)  # 鼠标移至右侧滑条
                                pyautogui.press('down')
                                time.sleep(0.1)
                                pyautogui.press('down')
                                qudati = retxy((0, 0, 1920, 1080), templateimg="qudati.png", )

                                qudati3 = retxy((0, 0, 1920, 1080), templateimg="qudati3.png", )
                                if len(qudati) > 0:

                                    x = qudati[0][0]
                                    y = qudati[0][1]
                                    clicking(px=x, py=y)
                                    time.sleep(2)
                                    doit()
                                    break
                        if videodoover>0:#如果这道题已经作完
                            gohome = retxy((0, 0, 1920, 1080), templateimg="homepage.png", )
                            clicking(px=1919, py=300)  # 鼠标移至右侧滑条
                            pyautogui.press('up')
                            time.sleep(0.1)
                            pyautogui.press('up')
                            time.sleep(0.1)
                            clicking(px=gohome[0][0], py=gohome[0][1])

                            break

                else:
                    print ("当前篇已完成进入下一篇")
                clicking(px=1235, py=123)





            # 查看学习任务
            lengwu = retxy((0, 0, 1920, 1080), templateimg="lengwu.png", )
            if len(lengwu) > 0:
                pbx = lengwu[0][0]
                pby = lengwu[0][1]
                clicking(px=pbx, py=pby)
                time.sleep(1)
                over = retxy((0, 0, 1920, 1080), templateimg="over.png", )
                if len(over)>0:
                    print ("#"*20)
                    print("恭喜你！今天的任务已完成！")
                    print("#" * 20)
                else:
                    print ("请检查是否有题没有答对！！")
        else:
            print("未获利坐标")
