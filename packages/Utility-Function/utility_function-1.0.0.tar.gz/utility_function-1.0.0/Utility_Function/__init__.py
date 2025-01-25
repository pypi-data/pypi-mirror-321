import base64
import hashlib
import platform
import random
import shutil
import datetime
import string
import pyfiglet
import random
import time
import os
import PIL
import cv2
import numpy
import re   
import requests
import json
import bs4
import urllib
import pandas
import numpy
import matplotlib
import packaging
import cv2
import numpy
import pyzbar.pyzbar
import keyboard
import math
import datetime
import pandas
import numpy
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pygame
import pyautogui
import qrcode
import sympy

class CAPTCHA:
    class String:
        @staticmethod
        def random_string(length):
            """
            生成随机字符串。
            """
            random_str = ''.join(random.sample(string.ascii_letters + string.digits, length))
            return random_str

        @staticmethod
        def random_number(length):
            """
            生成随机数字。
            """
            random_num = ''.join(random.sample(string.digits, length))
            return random_num

        @staticmethod
        def random_lower_string(length):
            """
            生成随机小写字母字符串。
            """
            random_lower_str = ''.join(random.sample(string.ascii_lowercase, length))
            return random_lower_str

        @staticmethod
        def random_upper_string(length):
            """
            生成随机大写字母字符串。
            """
            random_upper_str = ''.join(random.sample(string.ascii_uppercase, length))
            return random_upper_str

        @staticmethod
        def random_mix_string(length):
            """
            生成随机混合字母字符串。
            """
            random_mix_str = ''.join(random.sample(string.ascii_letters, length))
            return random_mix_str

    class Number:  

        # 生成数字验证码
        @staticmethod
        def createCode(who='有人',number=4,isreturn=True):
            res = ""
            for i in range(number):
                num = random.randint(0,9)
                res += str(num)
            if isreturn:
                return res
            else:
                print("%s向你发送验证码，验证码5分钟内有效，你的验证码为%s" % (who, res))

        # 验证码校验
        @staticmethod
        def checkingCode(inputCode,realCode):
            res = False
            if inputCode == realCode:
                res = True
            return res
        # 生成字母加数字的验证码
        @staticmethod
        def generate_verification_code(length=6,isreturn=True):
            verification_code_chars = string.ascii_letters + string.digits
            verification_code = ''.join(random.choice(verification_code_chars) for _ in range(length))
            if isreturn:
                return verification_code
            else:
                print(verification_code)

class color:
    white = (0, 0, 1)
    smoke = (0, 0, 0.96)
    light_gray = (0, 0, 0.75)
    gray = (0, 0, 0.5)
    dark_gray = (0, 0, 0.25)
    black = (0, 0, 0)
    red = (0, 1, 1)
    orange = (30, 1, 1)
    yellow = (60, 1, 1)
    lime = (90, 1, 1)
    green = (120, 1, 1)
    turquoise = (150, 1, 1)
    cyan = (180, 1, 1)
    azure = (210, 1, 1)
    blue = (240, 1, 1)
    violet = (270, 1, 1)
    magenta = (300, 1, 1)
    pink = (330, 1, 1)
    brown = (165, 42, 42)
    olive = (128, 128, 0)
    peach = (255, 218, 185)
    gold = (255, 215, 0)
    silver = (192, 192, 192)
    beige = (245, 245, 220)
    tan = (210, 180, 140)
    brown_sugar = (193, 154, 107)
    chocolate = (210, 105, 30)
    coffee = (111, 78, 55)
    coral = (255, 127, 80)
    cream = (255, 253, 208)
    peach_puff = (255, 218, 185)
    pink_salmon = (255, 140, 145)
    light_pink = (255, 182, 193)
    rose = (255, 0, 127)
    mauve = (224, 176, 255)
    plum = (221, 160, 221)
    lavender = (230, 230, 250)
    wheat = (245, 222, 179)
    sandy_brown = (244, 164, 96)
    khaki = (240, 230, 140)
    cornsilk = (255, 248, 220)
    golden_rod = (218, 165, 32)
    dark_golden_rod = (184, 134, 11)
    orange_red = (255, 69, 0)
    dark_orange = (255, 140, 0)
    dark_red = (139, 0, 0)
    dark_magenta = (139, 0, 139)
    dark_violet = (148, 0, 211)
    purple = (128, 0, 128)
    indigo = (75, 0, 130)
    dark_slate_blue = (72, 61, 139)
    slate_blue = (106, 90, 205)
    medium_slate_blue = (123, 104, 238)
    medium_blue = (0, 0, 205)
    navy = (0, 0, 128)
    blue_violet = (138, 43, 226)
    dark_blue = (0, 0, 139)
    midnight_blue = (25, 25, 112)
    cornflower_blue = (100, 149, 237)
    royal_blue = (65, 105, 225)
    light_steel_blue = (176, 196, 222)
    light_sky_blue = (135, 206, 250)
    sky_blue = (135, 206, 235)
    deep_sky_blue = (0, 191, 255)
    dodger_blue = (30, 144, 255)
    cadet_blue = (95, 158, 160)
    steel_blue = (70, 130, 180)
    light_blue = (173, 216, 230)
    powder_blue = (176, 224, 230)
    pale_turquoise = (175, 238, 238)
    aquamarine = (127, 255, 212)
    dark_turquoise = (0, 206, 209)
    medium_turquoise = (72, 209, 204)
    turquoise_blue = (0, 199, 140)
    dark_cyan = (0, 139, 139)
    teal = (0, 128, 128)
    light_green = (144, 238, 144)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    sea_green = (46, 139, 87)
    olive_drab = (107, 142, 35)
    dark_olive_green = (85, 107, 47)
    medium_aquamarine = (102, 205, 170)
    dark_sea_green = (143, 188, 143)    
    light_sea_green = (32, 178, 170)
    dark_slate_gray = (47, 79, 79)
    dark_slate_grey = (47, 79, 79)
    dim_gray = (105, 105, 105)
    dim_grey = (105, 105, 105)
    slate_gray = (112, 128, 144)                
    slate_grey = (112, 128, 144)
    light_slate_gray = (119, 136, 153)
    light_slate_grey = (119, 136, 153)
    medium_spring_green = (0, 250, 154)
    spring_green = (0, 255, 127)
    medium_sea_green = (60, 179, 113)
    sea_green = (46, 139, 87)
    lime_green = (50, 205, 50)
    dark_sea_green = (143, 188, 143)
    medium_aquamarine = (102, 205, 170)
    yellow_green = (154, 205, 50)
    lime = (0, 255, 0)
    chartreuse = (127, 255, 0)
    lawn_green = (124, 252, 0)
    green_yellow = (173, 255, 47)
    olive_green = (128, 128, 0)
    dark_khaki = (189, 183, 107)
    pale_green = (152, 251, 152)
    light_green = (144, 238, 144)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    sea_green = (46, 139, 87)
    olive_drab = (107, 142, 35)
    dark_olive_green = (85, 107, 47)
    medium_aquamarine = (102, 205, 170)
    dark_sea_green = (143, 188, 143)
    light_sea_green = (32, 178, 170)
    dark_slate_gray = (47, 79, 79)
    dark_slate_grey = (47, 79, 79)
    dim_gray = (105, 105, 105)
    dim_grey = (105, 105, 105)
    slate_gray = (112, 128, 144)                
    slate_grey = (112, 128, 144)
    light_slate_gray = (119, 136, 153)
    light_slate_grey = (119, 136, 153)
    medium_spring_green = (0, 250, 154)
    spring_green = (0, 255, 127)
    medium_sea_green = (60, 179, 113)
    sea_green = (46, 139, 87)
    lime_green = (50, 205, 50)
    dark_sea_green = (143, 188, 143)
    medium_aquamarine = (102, 205, 170)
    yellow_green = (154, 205, 50)
    lime = (0, 255, 0)
    chartreuse = (127, 255, 0)
    lawn_green = (124, 252, 0)
    green_yellow = (173, 255, 47)
    olive_green = (128, 128, 0)
    dark_khaki = (189, 183, 107)
    pale_green = (152, 251, 152)
    light_green = (144, 238, 144)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    sea_green = (46, 139, 87)
    olive_drab = (107, 142, 35)
    dark_olive_green = (85, 107, 47)
    medium_aquamarine = (102, 205, 170)
    dark_sea_green = (143, 188, 143)
    light_sea_green = (32, 178, 170)
    dark_slate_gray = (47, 79, 79)
    dark_slate_grey = (47, 79, 79)                
    dim_gray = (105, 105, 105)                                                                
    slate_gray = (112, 128, 144)                
    slate_grey = (112, 128, 144)
    light_slate_gray = (119, 136, 153)
    light_slate_grey = (119, 136, 153)
    medium_spring_green = (0, 250, 154)
    spring_green = (0, 255, 127)
    medium_sea_green = (60, 179, 113)
    sea_green = (46, 139, 87)
    lime_green = (50, 205, 50)
    dark_sea_green = (143, 188, 143)                                                                
    medium_aquamarine = (102, 205, 170)
    yellow_green = (154, 205, 50)
    lime = (0, 255, 0)
    chartreuse = (127, 255, 0)
    lawn_green = (124, 252, 0)
    green_yellow = (173, 255, 47)
    olive_green = (128, 128, 0)
    dark_khaki = (189, 183, 107)
    pale_green = (152, 251, 152)
    light_green = (144, 238, 144)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    sea_green = (46, 139, 87)
    olive_drab = (107, 142, 35)
    dark_olive_green = (85, 107, 47)
    medium_aquamarine = (102, 205, 170)
    dark_sea_green = (143, 188, 143)
    light_sea_green = (32, 178, 170)
    dark_slate_gray = (47, 79, 79)
    dark_slate_grey = (47, 79, 79)
    dim_gray = (105, 105, 105)
    dim_grey = (105, 105, 105)
    slate_gray = (112, 128, 144)                
    slate_grey = (112, 128, 144)
    light_slate_gray = (119, 136, 153)
    light_slate_grey = (119, 136, 153)
    medium_spring_green = (0, 250, 154)
    spring_green = (0, 255, 127)
    medium_sea_green = (60, 179, 113)
    sea_green = (46, 139, 87)
    lime_green = (50, 205, 50)
    dark_sea_green = (143, 188, 143)
    medium_aquamarine = (102, 205, 170)
    yellow_green = (154, 205, 50)
    lime = (0, 255, 0)
    chartreuse = (127, 255, 0)
    lawn_green = (124, 252, 0)
    green_yellow = (173, 255, 47)
    olive_green = (128, 128, 0)
    dark_khaki = (189, 183, 107)                                                                
    pale_green = (152, 251, 152)
    light_green = (144, 238, 144)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    salmon = (250, 128, 114)
    clear = (0, 0, 0, 0)
    white10 = (1,1,1, 0.10)
    white33 = (1,1,1, 0.33)
    white50 = (1,1,1, 0.50)
    white66 = (1,1,1, 0.66)
    black10 = (0,0,0, 0.10)
    black33 = (0,0,0, 0.33)
    black50 = (0,0,0, 0.50)
    black66 = (0,0,0, 0.66)
    black90 = (0,0,0, 0.90)
    black95 = (0,0,0, 0.95)
    black99 = (0,0,0, 0.99)
    red10 = (1,0,0, 0.10)
    red33 = (1,0,0, 0.33)
    red50 = (1,0,0, 0.50)
    red66 = (1,0,0, 0.66)
    red90 = (1,0,0, 0.90)
    red95 = (1,0,0, 0.95)
    red99 = (1,0,0, 0.99)
    green10 = (0,1,0, 0.10)
    green33 = (0,1,0, 0.33)    
    green50 = (0,1,0, 0.50)
    green66 = (0,1,0, 0.66)
    green90 = (0,1,0, 0.90)
    green95 = (0,1,0, 0.95)
    green99 = (0,1,0, 0.99)
    blue10 = (0,0,1, 0.10)
    blue33 = (0,0,1, 0.33)
    blue50 = (0,0,1, 0.50)
    blue66 = (0,0,1, 0.66)
    blue90 = (0,0,1, 0.90)
    blue95 = (0,0,1, 0.95)
    blue99 = (0,0,1, 0.99)
    yellow10 = (1,1,0, 0.10)
    yellow33 = (1,1,0, 0.33)
    yellow50 = (1,1,0, 0.50)
    yellow66 = (1,1,0, 0.66)
    yellow90 = (1,1,0, 0.90)
    yellow95 = (1,1,0, 0.95)
    yellow99 = (1,1,0, 0.99)
    cyan10 = (0,1,1, 0.10)
    cyan33 = (0,1,1, 0.33)
    cyan50 = (0,1,1, 0.50)
    cyan66 = (0,1,1, 0.66)
    cyan90 = (0,1,1, 0.90)
    cyan95 = (0,1,1, 0.95)
    cyan99 = (0,1,1, 0.99)
    magenta10 = (1,0,1, 0.10)
    magenta33 = (1,0,1, 0.33)
    magenta50 = (1,0,1, 0.50)
    magenta66 = (1,0,1, 0.66)
    magenta90 = (1,0,1, 0.90)
    magenta95 = (1,0,1, 0.95)
    magenta99 = (1,0,1, 0.99)
    gray10 = (0.1,0.1,0.1, 0.10)
    gray33 = (0.1,0.1,0.1, 0.33)
    gray50 = (0.1,0.1,0.1, 0.50)
    gray66 = (0.1,0.1,0.1, 0.66)
    gray90 = (0.1,0.1,0.1, 0.90)
    gray95 = (0.1,0.1,0.1, 0.95)
    gray99 = (0.1,0.1,0.1, 0.99)
    dark_gray10 = (0.2,0.2,0.2, 0.10)
    dark_gray33 = (0.2,0.2,0.2, 0.33)
    dark_gray50 = (0.2,0.2,0.2, 0.50)
    dark_gray66 = (0.2,0.2,0.2, 0.66)        
    dark_gray90 = (0.2,0.2,0.2, 0.90)
    dark_gray95 = (0.2,0.2,0.2, 0.95)
    dark_gray99 = (0.2,0.2,0.2, 0.99)
    light_gray10 = (0.3,0.3,0.3, 0.10)
    light_gray33 = (0.3,0.3,0.3, 0.33)
    light_gray50 = (0.3,0.3,0.3, 0.50)  
    light_gray66 = (0.3,0.3,0.3, 0.66)
    light_gray90 = (0.3,0.3,0.3, 0.90)
    light_gray95 = (0.3,0.3,0.3, 0.95)
    light_gray99 = (0.3,0.3,0.3, 0.99)
    white = (1,1,1)
    black = (0,0,0)
    red = (1,0,0)
    green = (0,1,0)
    blue = (0,0,1)
    yellow = (1,1,0)
    cyan = (0,1,1)
    magenta = (1,0,1)
    gray = (0.5,0.5,0.5)

class about_Text:
    def default(font="larry3d"):
        f = PIL.Figlet(font=font, width=200)
        print(f.renderText())
    def renderText(text="Happy Children's Day"):
        f = PIL.Figlet(font="larry3d", width=200)
        print(f.renderText(text))
    
class GraytoChar:
    def __GraytoChar__(gray,zifu):
        allChar = zifu
        rate = gray/256
        char = allChar[int(len(allChar)*rate)]
        return char
    def UseCraytoChar(lujing,zifu):
        img = PIL.Image.open(lujing)
        img = img.resize((60, 60))
        img = img.convert('L')
        text = ""
        for i in range(60):
            for j in range(60):
                text += GraytoChar.__GraytoChar(img.getpixel((i,j)),zifu)
            text += "\n"

        print(text)

        result = open("output.txt", "w")
        result.write(text)
        result.close()
        os.system("notepad output.txt")

class Email:
    def __init__(self,email,subject,sendto,password,zhenwen,SMTP服务器地址,端口):
        self.SMTP服务器地址 = SMTP服务器地址
        self.email = email
        self.subject = subject
        self.sendto = sendto
        self.password = password
        self.zhenwen = zhenwen
        self.端口 = 端口
    
    def send_email(self):
        # 发件人邮箱地址和密码
        sender_email = self.email
        sender_password = self.password

        # 收件61
        receiver_email = self.sendto

        # 创建邮件对象
        message = MIMEMultipart()
        message["From"] = sender_email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = self.subject

        body = self.zhenwen
        message.attach(MIMEText(body, "plain"))

        # 连接到SMTP服务器
        try:
            server = smtplib.SMTP(self.SMTP服务器地址, self.端口)  # Gmail的SMTP服务器地址和端口
            server.starttls()  # 启动安全传输模式
            server.login(sender_email, sender_password)  # 登录到邮箱

            # 发送邮件
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {e}")
        finally:
            server.quit()  # 关闭连接

class qita:
    π: float
    π = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674676788952521385225499546667278239864565961163548862305774564980355936345681743241125150760694794510965960940252288797108931456691368672287489405601015033086179286809208747609178249385890097149096759852613655497818931297848216829989487226588048575640142704775551323796414515237462343645428584447952658678210511413547357395231134271661021359695362314429524849371871101457654035902799344037420073105785390621983874478084784896833214457138687519435064302184531910484810053706146806749192781911979399520614196634287544406437451237181921799983910159195618146751426912397489409071864942319615679452080951465502252316038819301420937621378559566389377870830390697920773467221825625996615014215030680384477345492026054146659252014974428507325186660021324340881907104863317346496514539057962685610055081066587969981635747363840525714591028970641401109712062804390397595156771577004203378699360072305587631763594218731251471205329281918261861258673215791984148488291644706095752706957220917567116722910981690915280173506712748583222871835209353965725121083579151369882091444210067510334671103141267111369908658516398315019701651511685171437657618351556508849099898599823873455283316355076479185358932261854896321329330898570642046752590709154814165498594616371802709819943099244889575712828905923233260972997120844335732654893823911932597463667305836041428138830320382490375898524374417029132765618093773444030707469211201913020330380197621101100449293215160842444859637669838952286847831235526582131449576857262433441893039686426243410773226978028073189154411010446823252716201052652272111660396665573092547110557853763466820653109896526918620564769312570586356620185581007293606598764861179104533488503461136576867532494416680396265797877185560845529654126654085306143444318586769751456614068007002378776591344017127494704205622305389945613140711270004078547332699390814546646458807972708266830634328587856983052358089330657574067954571637752542021149557615814002501262285941302164715509792592309907965473761255176567513575178296664547791745011299614890304639947132962107340437518957359614589019389713111790429782856475032031986915140287080859904801094121472213179476477726224142548545403321571853061422881375850430633217518297986622371721591607716692547487389866549494501146540628433663937900397692656721463853067360965712091807638327166416274888800786925602902284721040317211860820419000422966171196377921337575114959501566049631862947265473642523081770367515906735023507283540567040386743513622224771589150495309844489333096340878076932599397805419341447377441842631298608099888687413260472156951623965864573021631598193195167353812974167729478672422924654366800980676928238280689964004824354037014163149658979409243237896907069779422857562498336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674676788952521385225499546667278239864565961163548862305774564980355936345681743241125150760694794510965960940252288797108931456691368672287489405601015033086179286809208747609178249385890097149096759852613655497818931297848216829989487226588048575640142704775551323796414515237462343645428584447952658678210511413547357395231134271661021359695362314429524849371871101457654035902799344037420073105785390621983874478084784896833214457138687519435064302184531910484810053706146806749192781911979399520614196634287544406437451237181921799983910159195618146751426912397489409071864942319615679452080951465502252316038819301420937621378559566389377870830390697920773467221825625996615014215030680384477345492026054146659252014974428507325186660021324340881907104863317346496514539057962685610055081066587969981635747363840525714591028970641401109712062804390397595156771577004203378699360072305587631763594218731251471205329281918261861258673215791984148488291644706095752706957220917567116722910981690915280173506712748583222871835209353965725121083579151369882091444210067510334671103

class QrCode:
    def QRCodeGenerator(data,lujing):
        # 创建一个二维码对象
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # 添加要编码的数据到二维码
        date = date
        qr.add_data(data)

        # 生成二维码                        
        qr.make(fit=True)

        # 从二维码生成图像                        
        img = qr.make_image(fill_color="black", back_color="white")

        # 保存二维码为图像文件
        filename = lujing
        img.save(filename + ".png") 

    def QRcodescanner(lujing):
        # 询问用户输入二维码图像的路径
        image_path = lujing

        # 读取图像
        frame = cv2.imread(image_path)

        if frame is None:
            print("无法加载图像，请检查路径是否正确。")
        else:
            decoded_objects = pyzbar.pyzbar.decode(frame)  # 解码二维码
            results = []

            for obj in decoded_objects:
                data = obj.data.decode('utf-8')  # 获取解码的数据
                results.append(data)  # 将结果添加到列表中
                print("Data:", data)

            if results:
                print("扫描结果如下：")
                for item in results:
                    print(item)
            else:
                print("未检测到二维码。")

class NetworkUtility:
    class IPv4:
        def IPv4_to_decimal(self, ip_address):
            """
            将一个IPv4地址转换为十进制格式。
            """
            octets = ip_address.split('.')
            decimal_value = 0
            for index, octet in enumerate(octets):
                decimal_value += int(octet) * (256 ** (3 - index))
            return decimal_value
        
        def decimal_to_IPv4(self, decimal_value):
            """
            将一个十进制值转换为IPv4地址。
            """
            octets = []
            for _ in range(4):
                octet = decimal_value % 256
                octets.insert(0, str(octet))  # 使用 insert(0, octet) 将八位字节插入到列表的开头
                decimal_value //= 256
            return '.'.join(octets)
    
    class IPv6:
        def IPv6_to_decimal(self, ip_address):
            """
            将一个IPv6地址转换为十进制格式。
            """
            hextets = ip_address.split(':')
            decimal_value = 0
            for index, hextet in enumerate(hextets):
                decimal_value += int(self.hex_to_decimal(hextet)) * (2 ** (16 * (7 - index)))
            return decimal_value
        
        def decimal_to_IPv6(self, decimal_value):
            """
            将一个十进制值转换为IPv6地址。
            """
            hextets = []
            for _ in range(8):
                hextet = decimal_value % 65536
                hextets.insert(0, self.decimal_to_hex(hextet))  # 使用 insert(0, hextet) 将十六进制块插入到列表的开头
                decimal_value //= 65536
            return ':'.join(hextets)
        
        def hex_to_decimal(self, hextet):
            """
            将一个十六进制块转换为十进制值。
            """
            return int(hextet, 16)
        
        def decimal_to_hex(self, decimal_value):
            """
            将一个十进制值转换为十六进制块。
            """
            return format(decimal_value, 'x')

class BaseConversion:
    class HexDecimal:
        def hex_to_decimal(self, hex_value):
            """
            将一个十六进制值转换为十进制格式。
            """
            decimal_value = 0
            for digit in hex_value:
                decimal_value = decimal_value * 16 + int(digit, 16)
            return decimal_value
            
        def decimal_to_hex(self, decimal_value):
            """
            将一个十进制值转换为十六进制格式。
            """
            hex_value = ''
            while decimal_value > 0:
                hex_digit = decimal_value % 16
                if hex_digit < 10:
                    hex_value = chr(hex_digit + 48) + hex_value
                else:
                    hex_value = chr(hex_digit + 55) + hex_value
                decimal_value //= 16
            return hex_value
        
    class BinaryDecimal:
        @staticmethod
        def decimal_to_binary(b: int) -> str:
            """
            将一个十进制值转换为二进制格式。
            """
            if b == 0:
                return "0"
            zh: str = ""
            while b > 0:
                yy = b % 2
                b = b // 2
                zh = str(yy) + zh
            return zh

        @staticmethod
        def binary_to_decimal(s: str) -> int:
            """
            将一个二进制值转换为十进制格式。
            """
            s = str(s)
            decimal_value = 0
            for index, digit in enumerate(reversed(s)):
                decimal_value += int(digit) * (2 ** index)
            return decimal_value

class Time:
    @staticmethod
    def get_now_date():
        """
        获取当前日期，格式为 yyyy-mm-dd。
        """
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d')

    @staticmethod
    def get_now_time():
        """
        获取当前时间，格式为 hh:mm:ss。
        """
        now = datetime.datetime.now()
        return now.strftime('%H:%M:%S')

    @staticmethod
    def get_now_datetime():
        """
        获取当前日期和时间，格式为 yyyy-mm-dd hh:mm:ss。
        """
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

class File:
    class file:
        @staticmethod
        def read_file(file_path):
            """
            读取文件内容。
            """
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content

        @staticmethod
        def write_file(file_path, content):
            """
            写入文件内容。
            """
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                return True

        @staticmethod
        def append_file(file_path, content):
            """
            追加文件内容。
            """
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(content)
                return True

        @staticmethod
        def delete_file(file_path):
            """
            删除文件。
            """
            os.remove(file_path)
            return True

        @staticmethod
        def rename_file(file_path, new_name):
            """
            重命名文件。
            """
            os.rename(file_path, new_name)
            return True

        @staticmethod
        def copy_file(src_file_path, dst_file_path):
            """
            复制文件。
            """
            shutil.copyfile(src_file_path, dst_file_path)
            return True

        @staticmethod
        def move_file(src_file_path, dst_file_path):
            """
            移动文件。
            """
            shutil.move(src_file_path, dst_file_path)
            return True

        @staticmethod
        def get_file_size(file_path):
            """
            获取文件大小。
            """
            file_size = os.path.getsize(file_path)
            return file_size

        @staticmethod
        def get_file_list(dir_path):
            """
            获取目录下的文件列表。
            """
            file_list = os.listdir(dir_path)
            return file_list

    class dir:
        @staticmethod
        def create_dir(dir_path):
            """
            创建目录。
            """
            os.makedirs(dir_path)
            return True

        @staticmethod
        def delete_dir(dir_path):
            """
            删除目录。
            """
            shutil.rmtree(dir_path)
            return True

        @staticmethod
        def rename_dir(dir_path, new_name):
            """
            重命名目录。
            """
            os.rename(dir_path, new_name)
            return True

        @staticmethod
        def copy_dir(src_dir_path, dst_dir_path):
            """
            复制目录。
            """
            shutil.copytree(src_dir_path, dst_dir_path)
            return True

        @staticmethod
        def move_dir(src_dir_path, dst_dir_path):
            """
            移动目录。
            """
            shutil.move(src_dir_path, dst_dir_path)
            return True

class Image:
    @staticmethod
    def show_image(window_name, image):
        """
        显示图像。
        """
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return True

    @staticmethod
    def save_image(file_path, image):
        """
        保存图像。
        """
        cv2.imwrite(file_path, image)
        return True

    @staticmethod
    def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
        """
        调整图像大小。
        """
        dim = None
        (h, w) = image.shape[:2]
        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))
        resized = cv2.resize(image, dim, interpolation=inter)
        return resized

    @staticmethod
    def rotate_image(image, angle, center=None, scale=1.0):
        """
        旋转图像。
        """
        (h, w) = image.shape[:2]
        if center is None:
            center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (w, h))
        return rotated

    @staticmethod
    def flip_image(image, flip_code):
        """
        翻转图像。
        """
        flipped = cv2.flip(image, flip_code)
        return flipped

    @staticmethod
    def crop_image(image, x, y, w, h):
        """
        裁剪图像。
        """
        cropped = image[y:y+h, x:x+w]
        return cropped

class Video:
    @staticmethod
    def read_video(file_path):
        """
        读取视频。
        """
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():    
            ret, frame = cap.read()
            if ret:
                yield frame
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        return True

    @staticmethod
    def save_video(file_path, frame_list):
        """
        保存视频。
        """
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))
        for frame in frame_list:
            out.write(frame)
        out.release()
        return True
    @staticmethod
    def show_video(window_name, file_path):
        """
        显示视频。
        """
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow(window_name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        return True

class Web:
    @staticmethod
    def get_html(url):
        """
        获取网页HTML内容。
        """
        response = requests.get(url)
        return response.text

    @staticmethod
    def get_json(url):
        """
        获取网页JSON内容。
        """
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_image(url):
        """
        获取网页图片。
        """
        response = requests.get(url)
        return response.content

    @staticmethod
    def post_data(url, data):
        """
        向网页提交数据。
        """
        response = requests.post(url, data=data)
        return response.text
    @staticmethod
    def download_file(url, file_path):
        """
        下载文件。
        """
        response = requests.get(url, stream=True)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return True
    @staticmethod
    def upload_file(url, file_path):
        """
        上传文件。
        """
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        return response.text

class System:
    @staticmethod
    def get_platform():
        """
        获取当前平台。
        """
        return platform.system()

    @staticmethod
    def get_platform_version():
        """
        获取当前平台版本。
        """
        return platform.version()

    @staticmethod
    def get_platform_release():
        """
        获取当前平台发行版本。
        """
        return platform.release()

    @staticmethod
    def get_platform_machine():
        """
        获取当前平台架构。
        """
        return platform.machine()

    @staticmethod
    def get_platform_processor():
        """
        获取当前平台处理器。
        """
        return platform.processor()

    @staticmethod
    def get_python_version():
        """
        获取当前Python版本。
        """
        return platform.python_version()

    @staticmethod
    def get_python_build():
        """
        获取当前Python编译版本。
        """
        return platform.python_build()

    @staticmethod
    def get_python_compiler():
        """
        获取当前Python编译器。
        """
        return platform.python_compiler()

    @staticmethod
    def get_python_branch():
        """
        获取当前Python分支。
        """
        return platform.python_branch()

    @staticmethod
    def get_python_implementation():
        """
        获取当前Python实现。
        """
        return platform.python_implementation()

    @staticmethod
    def get_python_revision():
        """
        获取当前Python修订版本。
        """
        return platform.python_revision()

    @staticmethod
    def get_system_version():
        """
        获取当前系统版本。
        """
        return platform.system_alias(platform.system(), platform.release(), platform.version())

    @staticmethod
    def get_system_name():
        """
        获取当前系统名称。
        """
        return platform.system()

    @staticmethod
    def get_system_release():
        """
        获取当前系统发行版本。
        """
        return platform.release()

    @staticmethod
    def get_system_version():
        """
        获取当前系统版本。
        """
        return platform.version()

    @staticmethod
    def get_system_machine():
        """
        获取当前系统架构。
        """
        return platform.machine()

    @staticmethod
    def get_system_processor():
        """
        获取当前系统处理器。
        """
        return platform.processor()

    @staticmethod
    def get_system_architecture():
        """
        获取当前系统架构。
        """
        return platform.architecture()

    @staticmethod
    def get_system_uname():
        """
        获取当前系统uname信息。
        """
        return platform.uname()

    @staticmethod
    def get_system_libc_version():
        """
        获取当前系统libc版本。
        """
        return platform.libc_ver()

    @staticmethod
    def get_system_mac_ver():
        """
        获取当前系统mac版本。
        """
        return platform.mac_ver()

    @staticmethod
    def get_system_win32_ver():
        """
        获取当前系统win32版本。
        """
        return platform.win32_ver()

    @staticmethod
    def get_system_win32_edition():
        """
        获取当前系统win32版本。
        """
        return platform.win32_edition()

    @staticmethod
    def get_system_win32_is_iot():
        """
        获取当前系统是否为IOT。
        """
        return platform.win32_is_iot()

    @staticmethod
    def get_system_win32_ver_major():
        """
        获取当前系统win32版本主版本号。
        """
        return platform.win32_ver()[0]

    @staticmethod
    def get_system_win32_ver_minor():
        """
        获取当前系统win32版本次版本号。
        """
        return platform.win32_ver()[1]

    @staticmethod
    def get_system_win32_ver_build():
        """
        获取当前系统win32版本构建号。
        """
        return platform.win32_ver()[2]

    @staticmethod
    def get_system_win32_ver_platform():
        """
        获取当前系统win32版本平台。
        """
        return platform.win32_ver()[3]

    @staticmethod
    def get_system_win32_ver_service_pack():
        """
        获取当前系统win32版本服务包。
        """
        return platform.win32_ver()[4]

    @staticmethod
    def get_system_win32_ver_product_type():
        """
        获取当前系统win32版本产品类型。
        """
        return platform.win32_ver()[5]

class HashValueString:
    @staticmethod
    def md5(string):
        """
        计算字符串的MD5值。
        """
        md5_obj = hashlib.md5()
        md5_obj.update(string.encode('utf-8'))
        return md5_obj.hexdigest()

    @staticmethod
    def sha1(string):
        """
        计算字符串的SHA1值。
        """
        sha1_obj = hashlib.sha1()
        sha1_obj.update(string.encode('utf-8'))
        return sha1_obj.hexdigest()

    @staticmethod
    def sha256(string):
        """                                                                    
        计算字符串的SHA256值。
        """
        sha256_obj = hashlib.sha256()
        sha256_obj.update(string.encode('utf-8'))
        return sha256_obj.hexdigest()
    @staticmethod
    def sha512(string):
        """
        计算字符串的SHA512值。
        """
        sha512_obj = hashlib.sha512()
        sha512_obj.update(string.encode('utf-8'))
        return sha512_obj.hexdigest()

class CodeString:
    @staticmethod
    def base64_encode(string):
        """
        编码字符串为Base64。
        """
        base64_obj = base64.b64encode(string.encode('utf-8'))
        return base64_obj.decode('utf-8')

    @staticmethod
    def base64_decode(string):
        """
        解码Base64字符串。
        """
        base64_obj = base64.b64decode(string.encode('utf-8'))
        return base64_obj.decode('utf-8')

print("欢迎使用Utility_Function辅助工具")
print("Welcome to the Utility_Function helper")