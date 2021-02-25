# coding: utf-8
from knd_ui import *

# 是否显示标题栏
set_size(800, 600, title=True)

# 此处为自定义界面中的控件设定一些默认设置，良好的默认设置可以简化后面的控件定义
# 在定义页面之前设置所有控件默认字体颜色，字体大小，对齐方式
default_attr(白色, f24x16, 左对齐)
# 设置所有页面中的静态字符控件默认字体颜色，字体大小，对齐方式
default_text_attr(红色, f24x16, 居中)
# 设置所有页面中的数据控件默认字体颜色，字体大小
default_data_attr(黄色, f20x10)

# 设置系统型号
sys_version("V5.2.00c_24724")

# 此自定义界面在数控系统的"位置"页面下
kui_id(位置)
# 此自定义界面根目录菜单名称为"demo"
menu("外圆磨")

# 此页的id为"main"，共有10行，5列。
with page(510, 792, id="main" , text=(Color.red, Align.left, f28x14) , data=(Color.green, f28x14)):
 #磨床主界面标题
    text("外圆磨床", (30, 1, 60, 792), Color.green, Align.center)

    # 左侧第一列text标题
    text("当前砂轮形状", (100, 15, 40, 180))
    data("#522",        (100, 200, 40, 160),Color.green, f24x16, Mode.ro, LineShow.show, choices={1: "直角砂轮"})  

    text("正在加工第",   (100, 380, 45, 160))
    text("台阶",        (100, 720, 40, 60))
    text("工件计数",    (145, 380, 45, 160))
    text("修砂轮时机",  (190, 380, 45, 160))

    data("#901",        (100, 600, 40, 110), LineShow.hide, enable ="#500 == 4" ,id="A", prev="D", next="B")
    data("#900",        (145, 600, 40, 110), Mode.ro, LineShow.hide) 
    data("#524",        (190, 600, 40, 110), Color.green,Mode.ro,LineShow.hide)

    text("外径量仪", (190, 5, 40, 400) , Color.green, Align.center)
    text("P1",      (235, 5, 40, 200) , Color.green, Align.center)
    text("P2",      (280, 5, 40, 200) , Color.green, Align.center)
    text("P3",      (325, 5, 40, 200) , Color.green, Align.center)
    text("P4",      (370, 5, 40, 200) , Color.green, Align.center)

    led("X0.0", (235, 200, 40, 100), Align.center) 
    led("X0.1", (280, 200, 40, 100), Align.center)
    led("X0.2", (325, 200, 40, 100), Align.center)
    led("X0.3", (370, 200, 40, 100), Align.center)

    text("端面量仪", (280,405, 40, 385) , Color.green, Align.center)
    text("P5",      (325, 405, 40, 200) , Color.green, Align.center)
    text("P6",      (370, 405, 40, 200) , Color.green, Align.center)
    
    led("X0.4",  (325,605, 40, 100), Align.center)
    led("X0.5",  (370,605, 40, 100), Align.center)

    text("开启端面测量误差检查", (415,15,40,280))
    data("#505", (415, 305, 40, 120), f24x16, enable ="#503 == 1",id ="B", choices={0: "不启用", 1: "启用"} ,prev= "A" ,right = "C", next = "D")

    text("误差范围设定", (415,450, 40, 180))
    data("#506", (415, 630, 40, 155), f24x16, id ="C", left = "B", right="B" ,prev= "B", next = "D")

    text("模式选择", (460,15, 40, 140) ,Align.left)
    #data("#500", (460,155, 40, 160), id ="D", choices={ 1: "工件磨削",2: "砂轮修整",3: "端面测量"}, prev= "B", next= "A", right= "C",left= "C")
    #text("1.工件磨削 2.砂轮修整 3.端面量仪",(470,340, 40, 400), Color.blue, Align.left, Font.s20x10)
    data("#500", (460,155, 40, 160), id ="D", choices={ 1: "工件磨削",2: "砂轮修整"}, prev= "B", next= "A", right= "C",left= "C")
    text("1.工件磨削 2.砂轮修整 ",(470,340, 40, 400), Color.blue, Align.left, Font.s20x10)

    menu("基本参数", "共同参数")
    menu("磨削参数", "磨削参数")
    menu("休整参数", "休整参数")
    menu("外径量仪", "外径量仪", "#510 == 1")
    menu("端面量仪", "端面量仪", "#503 == 1")


#共同参数
with page(510, 792, id="共同参数", text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):

    row_start = 10
    col_start = 1
    row_length = 35 
    col_length = 198

    text("共同参数", (5, 1,100,386), Color.red, Align.center ,f28x14)

    picture("外圆磨床.png"   , (100, 1, 270, 396))

    text("X轴安全位置"      , (row_start + 0*row_length, 2*col_length , row_length, col_length))
    text("台阶数"           , (row_start + 1*row_length, 2*col_length, row_length, col_length), Color.yellow)
    text("是否使用端面量仪"  , (row_start + 2*row_length, 2*col_length, row_length, col_length) )
    text("量仪与砂轮间距"      , (row_start + 3*row_length, 2*col_length, row_length, col_length) )
    text("是否使用外径量仪"  , (row_start + 4*row_length, 2*col_length, row_length, col_length))
    text("砂轮转速"         , (row_start + 5*row_length, 2*col_length, row_length, col_length))
    text("头架转速"         , (row_start + 6*row_length, 2*col_length, row_length, col_length))
    text("砂轮形状选择"     , (row_start + 7*row_length, 2*col_length, row_length, col_length))  
    text("修砂轮转速"       , (row_start + 8*row_length, 2*col_length, row_length, col_length))
    text("修砂轮时机"       , (row_start + 9*row_length, 2*col_length, row_length, col_length))
    text("Z轴重叠切入参数"   , (row_start + 10*row_length, 2*col_length, row_length, 2*col_length), Color.red,Align.center)
    text("直切Z轴移动量"     , (row_start + 11*row_length, 2*col_length, row_length, col_length))
    text("直切X轴抬刀量"    , (row_start + 12*row_length, 2*col_length, row_length, col_length))
    text("光磨速度"        , (row_start + 13*row_length, 2*col_length, row_length, col_length))

    teach("#501","#5011 - #5541", (row_start + 0*row_length, 3*col_length , row_length, col_length), Font.s24x12)
    data("#502", (row_start + 1*row_length, 3*col_length , row_length, col_length), min=1, max=8 ,data_type='uint')
    data("#503", (row_start + 2*row_length, 3*col_length , row_length, col_length), choices={0: "不启用",1: "启用"})
    data("#504", (row_start + 3*row_length, 3*col_length , row_length, col_length))
    data("#510", (row_start + 4*row_length, 3*col_length , row_length, col_length), choices={0: "不启用",1: "启用"} , \
    action = 运行脚本("IF #510 == 0 THEN #551 = 0 #581= 0 #611 = 0 #641= 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"))

    data("#520", (row_start + 5*row_length, 3*col_length , row_length, col_length))
    data("#521", (row_start + 6*row_length, 3*col_length , row_length, col_length))
    data("#522", (row_start + 7*row_length, 3*col_length , row_length, col_length), choices={1: "直角砂轮"})
    data("#523", (row_start + 8*row_length, 3*col_length , row_length, col_length))
    data("#524", (row_start + 9*row_length, 3*col_length , row_length, col_length))
#    data("#502", (row_start + 10*row_length, 3*col_length , row_length, col_length), Type.u8, LineShow.hide)
    data("#525", (row_start + 11*row_length, 3*col_length , row_length, col_length))
    data("#526", (row_start + 12*row_length, 3*col_length , row_length, col_length))
    data("#527", (row_start + 13*row_length, 3*col_length , row_length, col_length))

    text("[绝对坐标]", (375, 5,45,200),f24x12)
    text("X", (420, 5, 45, 15))
    coor("X", (420, 10, 45, 168),Color.white, f24x12, Align.right, Coor.abs)
    text("Z", (465, 5, 45, 15)) 
    coor("Z", (465, 10, 45, 168), Color.white, f24x12, Align.right, Coor.abs)
    text("[机床坐标]", (375, 200, 45, 200),f24x12)
    text("X", (420, 198, 45, 15))
    coor("X", (420, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)
    text("Z", (465, 198, 45, 15)) 
    coor("Z", (465, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)


    menu("基本参数", "共同参数")
    menu("磨削参数", "磨削参数")
    menu("休整参数", "休整参数")
    menu("外径量仪", "外径量仪", enable= "#510 == 1")
    #menu("端面量仪", "端面量仪", enable= "#503 == 1")
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("示教", 示教表达式) 
    menu("主界面", "main")

#共同参数
with page(510, 792, id= "磨削参数", text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
    menu("外圆一", "外圆一" )
    menu("外圆二", "外圆二" , enable= "#502 >= 2")
    menu("外圆三", "外圆三" , enable= "#502 >= 3")
    menu("外圆四", "外圆四" , enable= "#502 >= 4")
    menu("外圆五", "外圆五" , enable= "#502 >= 5")
    menu("外圆六", "外圆六" , enable= "#502 >= 6")
    menu("外圆七", "外圆七" , enable= "#502 >= 7")
    menu("主界面", "main")
    menu("外圆八", "外圆八" , enable= "#502 >= 8")


#共同参数
with page(510, 792, id= "外圆一",text=(Color.green, Align.left, f24x12), data=(Color.cyan, Align.right,f24x12, LineShow.show)):
#加工参数
    text("外圆1 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
#
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#540", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_1", right="CA_1")
    teach("#541", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_1", right="CB_1")
    data("#542", (195, 160, 45, 120) ,id ="LC_1", right="CC_1")
    data("#543", (240, 160, 45, 120) ,id ="LD_1", right="CD_1")
    data("#544", (285, 160, 45, 120) ,id ="LE_1", right="CE_1")
    data("#545", (330, 160, 45, 120) ,id ="LF_1", right="CF_1")
    data("#546", (375, 160, 45, 120) ,id ="LG_1", right="CG_1")
    data("#547", (420, 160, 45, 120) ,id ="LH_1", right="CL_1")
    data("#548", (465, 160, 45, 120) ,id ="LI_1", right="CI_1")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#549", (105, 450, 45, 120) , f24x12, id ="CA_1", choices={0: "直切磨削",1: "往复磨削"}, left="LA_1")
    data("#550", (150, 450, 45, 120) , f24x12,  id ="CB_1", choices={0: "单边进刀",1: "双边进刀"}, left="LB_1", right="RB_1")
    data("#551", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_1", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #551 == 1 THEN #581= 0 #611 = 0 #641= 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_1", right="RC_1")
    teach("#552", "#552 = #5012 - #5542", (240, 450, 45, 120) , id ="CD_1", left="LD_1")
    teach("#553", "#553 = #5012 - #5542 - #552 " ,(285, 450, 45, 120) , id ="CE_1", left="LE_1")
    data("#554", (330, 450, 45, 120) , id ="CF_1", left="LF_1")
    data("#555", (375, 450, 45, 120) , id ="CG_1", left="LG_1")
    data("#556", (420, 450, 45, 120) , id ="CH_1", left="LH_1")
    data("#557", (465, 450, 45, 120) , id ="CI_1", left="LI_1")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m ", (145, 612, 45, 180),LineShow.hide, id ="RB_1",  left="CB_1")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_1",  left="CC_1")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")


#共同参数
with page(510, 792, id= "外圆二",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆2 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
#
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#570", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_2", right="CA_2")
    teach("#571", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_2", right="CB_2")
    data("#572", (195, 160, 45, 120) ,id ="LC_2", right="CC_2")
    data("#573", (240, 160, 45, 120) ,id ="LD_2", right="CD_2")
    data("#574", (285, 160, 45, 120) ,id ="LE_2", right="CE_2")
    data("#575", (330, 160, 45, 120) ,id ="LF_2", right="CF_2")
    data("#576", (375, 160, 45, 120) ,id ="LG_2", right="CG_2")
    data("#577", (420, 160, 45, 120) ,id ="LH_2", right="CL_2")
    data("#578", (465, 160, 45, 120) ,id ="LI_2", right="CI_2")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#579", (105, 450, 45, 120) , f24x12, id ="CA_2", choices={0: "直切磨削",1: "往复磨削"}, left="LA_2")
    data("#580", (150, 450, 45, 120) , f24x12,  id ="CB_2", choices={0: "单边进刀",1: "双边进刀"}, left="LB_2", right="RB_2")
    data("#581", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_2", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #581 == 1 THEN #551= 0 #611 = 0 #641= 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_2", right="RC_2")
    teach("#582", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_2", left="LD_2")
    teach("#583", "#5012 - #5542  - #582" ,(285, 450, 45, 120) , id ="CE_2", left="LE_2")
    data("#584", (330, 450, 45, 120) , id ="CF_2", left="LF_2")
    data("#585", (375, 450, 45, 120) , id ="CG_2", left="LG_2")
    data("#586", (420, 450, 45, 120) , id ="CH_2", left="LH_2")
    data("#587", (465, 450, 45, 120) , id ="CI_2", left="LI_2")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_2",  left="CB_2")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_2",  left="CC_2")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")


#共同参数
with page(510, 792, id= "外圆三",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆3 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#600", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_3", right="CA_3")
    teach("#601", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_3", right="CB_3")
    data("#602", (195, 160, 45, 120) ,id ="LC_3", right="CC_3")
    data("#603", (240, 160, 45, 120) ,id ="LD_3", right="CD_3")
    data("#604", (285, 160, 45, 120) ,id ="LE_3", right="CE_3")
    data("#605", (330, 160, 45, 120) ,id ="LF_3", right="CF_3")
    data("#606", (375, 160, 45, 120) ,id ="LG_3", right="CG_3")
    data("#607", (420, 160, 45, 120) ,id ="LH_3", right="CL_3")
    data("#608", (465, 160, 45, 120) ,id ="LI_3", right="CI_3")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#609", (105, 450, 45, 120) , f24x12, id ="CA_3", choices={0: "直切磨削",1: "往复磨削"}, left="LA_3")
    data("#610", (150, 450, 45, 120) , f24x12,  id ="CB_3", choices={0: "单边进刀",1: "双边进刀"}, left="LB_3", right="RB_3")
    data("#611", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_3", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #611 == 1 THEN #551= 0 #581 = 0 #641= 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_3", right="RC_3")
    teach("#612", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_3", left="LD_3")
    teach("#613", "#5012 - #5542 - #612" ,(285, 450, 45, 120) , id ="CE_3", left="LE_3")
    data("#614", (330, 450, 45, 120) , id ="CF_3", left="LF_3")
    data("#615", (375, 450, 45, 120) , id ="CG_3", left="LG_3")
    data("#616", (420, 450, 45, 120) , id ="CH_3", left="LH_3")
    data("#617", (465, 450, 45, 120) , id ="CI_3", left="LI_3")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_3",  left="CB_3")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_3",  left="CC_3")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")


#共同参数
with page(510, 792, id= "外圆四",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆4 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#630", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_4", right="CA_4")
    teach("#631", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_4", right="CB_4")
    data("#632", (195, 160, 45, 120) ,id ="LC_4", right="CC_4")
    data("#633", (240, 160, 45, 120) ,id ="LD_4", right="CD_4")
    data("#634", (285, 160, 45, 120) ,id ="LE_4", right="CE_4")
    data("#635", (330, 160, 45, 120) ,id ="LF_4", right="CF_4")
    data("#636", (375, 160, 45, 120) ,id ="LG_4", right="CG_4")
    data("#637", (420, 160, 45, 120) ,id ="LH_4", right="CL_4")
    data("#638", (465, 160, 45, 120) ,id ="LI_4", right="CI_4")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#639", (105, 450, 45, 120) , f24x12, id ="CA_4", choices={0: "直切磨削",1: "往复磨削"}, left="LA_4")
    data("#640", (150, 450, 45, 120) , f24x12,  id ="CB_4", choices={0: "单边进刀",1: "双边进刀"}, left="LB_4", right="RB_4")
    data("#641", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_4", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #641 == 1 THEN #551= 0 #581 = 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_4", right="RC_4")
    teach("#642", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_4", left="LD_4")
    teach("#643", "#5012 - #5542 - #642" ,(285, 450, 45, 120) , id ="CE_4", left="LE_4")
    data("#644", (330, 450, 45, 120) , id ="CF_4", left="LF_4")
    data("#645", (375, 450, 45, 120) , id ="CG_4", left="LG_4")
    data("#646", (420, 450, 45, 120) , id ="CH_4", left="LH_4")
    data("#647", (465, 450, 45, 120) , id ="CI_4", left="LI_4")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_4",  left="CB_4")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_4",  left="CC_4")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))

    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")

#外圆五
with page(510, 792, id= "外圆五",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆5 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#660", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_5", right="CA_5")
    teach("#661", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_5", right="CB_5")
    data("#662", (195, 160, 45, 120) ,id ="LC_5", right="CC_5")
    data("#663", (240, 160, 45, 120) ,id ="LD_5", right="CD_5")
    data("#664", (285, 160, 45, 120) ,id ="LE_5", right="CE_5")
    data("#665", (330, 160, 45, 120) ,id ="LF_5", right="CF_5")
    data("#666", (375, 160, 45, 120) ,id ="LG_5", right="CG_5")
    data("#667", (420, 160, 45, 120) ,id ="LH_5", right="CL_5")
    data("#668", (465, 160, 45, 120) ,id ="LI_5", right="CI_5")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#669", (105, 450, 45, 120) , f24x12, id ="CA_5", choices={0: "直切磨削",1: "往复磨削"}, left="LA_5")
    data("#670", (150, 450, 45, 120) , f24x12,  id ="CB_5", choices={0: "单边进刀",1: "双边进刀"}, left="LB_5", right="RB_5")
    data("#671", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_5", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #671 == 1 THEN #551= 0 #581 = 0 #671 = 0 #701 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_5", right="RC_5")
    teach("#672", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_5", left="LD_5")
    teach("#673", "#5012 - #5542 - #672" ,(285, 450, 45, 120) , id ="CE_5", left="LE_5")
    data("#674", (330, 450, 45, 120) , id ="CF_5", left="LF_5")
    data("#675", (375, 450, 45, 120) , id ="CG_5", left="LG_5")
    data("#676", (420, 450, 45, 120) , id ="CH_5", left="LH_5")
    data("#677", (465, 450, 45, 120) , id ="CI_5", left="LI_5")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_5",  left="CB_5")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_5",  left="CC_5")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))

    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")


#外圆六
with page(510, 792, id= "外圆六",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆6 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#690", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_6", right="CA_6")
    teach("#691", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_6", right="CB_6")
    data("#692", (195, 160, 45, 120) ,id ="LC_6", right="CC_6")
    data("#693", (240, 160, 45, 120) ,id ="LD_6", right="CD_6")
    data("#694", (285, 160, 45, 120) ,id ="LE_6", right="CE_6")
    data("#695", (330, 160, 45, 120) ,id ="LF_6", right="CF_6")
    data("#696", (375, 160, 45, 120) ,id ="LG_6", right="CG_6")
    data("#697", (420, 160, 45, 120) ,id ="LH_6", right="CL_6")
    data("#698", (465, 160, 45, 120) ,id ="LI_6", right="CI_6")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#699", (105, 450, 45, 120) , f24x12, id ="CA_6", choices={0: "直切磨削",1: "往复磨削"}, left="LA_6")
    data("#700", (150, 450, 45, 120) , f24x12, id ="CB_6", choices={0: "单边进刀",1: "双边进刀"}, left="LB_6", right="RB_6")
    data("#701", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_6", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #701 == 1 THEN #551= 0 #581 = 0 #641= 0 #671 = 0 #731 =0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_6", right="RC_6")
    teach("#702", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_6", left="LD_6")
    teach("#703", "#5012 - #5542 - #702" ,(285, 450, 45, 120) , id ="CE_6", left="LE_6")
    data("#704", (330, 450, 45, 120) , id ="CF_6", left="LF_6")
    data("#705", (375, 450, 45, 120) , id ="CG_6", left="LG_6")
    data("#706", (420, 450, 45, 120) , id ="CH_6", left="LH_6")
    data("#707", (465, 450, 45, 120) , id ="CI_6", left="LI_6")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_6",  left="CB_6")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_6",  left="CC_6")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")

#外圆七
with page(510, 792, id= "外圆七",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#加工参数
    text("外圆7 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#720", "#5011 - #5541",(105, 160, 45, 120) ,id ="LA_7", right="CA_7")
    teach("#721", "#5011 - #5541" ,(150, 160, 45, 120) ,id ="LB_7", right="CB_7")
    data("#722", (195, 160, 45, 120) ,id ="LC_7", right="CC_7")
    data("#723", (240, 160, 45, 120) ,id ="LD_7", right="CD_7")
    data("#724", (285, 160, 45, 120) ,id ="LE_7", right="CE_7")
    data("#725", (330, 160, 45, 120) ,id ="LF_7", right="CF_7")
    data("#726", (375, 160, 45, 120) ,id ="LG_7", right="CG_7")
    data("#727", (420, 160, 45, 120) ,id ="LH_7", right="CL_7")
    data("#728", (465, 160, 45, 120) ,id ="LI_7", right="CI_7")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#729", (105, 450, 45, 120) , f24x12, id ="CA_7", choices={0: "直切磨削",1: "往复磨削"}, left="LA_7")
    data("#730", (150, 450, 45, 120) , f24x12,  id ="CB_7", choices={0: "单边进刀",1: "双边进刀"}, left="LB_7", right="RB_7")
    data("#731", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_7", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #731 == 1 THEN #551= 0 #581 = 0 #641= 0 #671 = 0 #701 = 0 #761 = 0 #791 = 0 #821 = 0 ENDIF"), left="LC_7", right="RC_7")
    teach("#732", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_7", left="LD_7")
    teach("#733", "#5012 - #5542 - #732" ,(285, 450, 45, 120) , id ="CE_7", left="LE_7")
    data("#734", (330, 450, 45, 120) , id ="CF_7", left="LF_7")
    data("#735", (375, 450, 45, 120) , id ="CG_7", left="LG_7")
    data("#736", (420, 450, 45, 120) , id ="CH_7", left="LH_7")
    data("#737", (465, 450, 45, 120) , id ="CI_7", left="LI_7")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_7",  left="CB_7")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_7",  left="CC_7")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))

    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")

#外圆八
with page(510, 792, id= "外圆八",text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):
#    text("外圆8 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14,)
    text("外圆8 加工设定", (30, 1, 50, 792), Color.red,Align.center, f28x14)
    text("外圆毛胚尺寸"  , (105, 6, 45, 150))
    text("外圆图纸尺寸"  , (150, 6, 45, 150))
    text("粗磨进给量"    , (195, 6, 45, 150))
    text("精磨进给量"    , (240, 6, 45, 150))  
    text("精磨次数"      , (285, 6, 45, 150))
    text("光磨次数"      , (330, 6, 45, 150))
    text("到位停顿时间"  , (375, 6, 45, 150))
    text("粗磨进给速度"  , (420, 6, 45, 150))
    text("精磨进给速度"  , (465, 6, 45, 150))
#
    teach("#750", "#5011 - #5541", (105, 160, 45, 120) ,id ="LA_8", right="CA_8")
    teach("#751", "#5011 - #5541", (150, 160, 45, 120) ,id ="LB_8", right="CB_8")
    data("#752", (195, 160, 45, 120) ,id ="LC_8", right="CC_8")
    data("#753", (240, 160, 45, 120) ,id ="LD_8", right="CD_8")
    data("#754", (285, 160, 45, 120) ,id ="LE_8", right="CE_8")
    data("#755", (330, 160, 45, 120) ,id ="LF_8", right="CF_8")
    data("#756", (375, 160, 45, 120) ,id ="LG_8", right="CG_8")
    data("#757", (420, 160, 45, 120) ,id ="LH_8", right="CL_8")
    data("#758", (465, 160, 45, 120) ,id ="LI_8", right="CI_8")
#
    text("外圆加工模式"  , (105, 300, 45, 150), Color.yellow)
    text("往复进刀方式"  , (150, 300, 45, 150), Color.yellow)
    text("外径量仪功能"  , (195, 300, 45, 150), Color.yellow)
    text("端面对刀点Z"   , (240, 300, 45, 150))  
    text("Z轴磨削区间"   , (285, 300, 45, 150))
    text("粗磨Z轴速度"   , (330, 300, 45, 150))
    text("精磨Z轴速度"   , (375, 300, 45, 150))
    text("Z轴退刀量"     , (420, 300, 45, 150))
    text("X轴退刀量"     , (465, 300, 45, 150))
#
    data("#759", (105, 450, 45, 120) , f24x12, id ="CA_8", choices={0: "直切磨削",1: "往复磨削"}, left="LA_8")
    data("#760", (150, 450, 45, 120) , f24x12,  id ="CB_8", choices={0: "单边进刀",1: "双边进刀"}, left="LB_8", right="RB_8")
    data("#761", (195, 450, 45, 120) , f24x12, enable= "#510 == 1",id ="CC_8", choices={0: "不用量仪",1: "使用量仪"},\
    action = 运行脚本("IF #761 == 1 THEN #551= 0 #581 = 0 #641= 0 #671 = 0 #701 = 0 #731 =0 #791 = 0 #821 = 0 ENDIF"), left="LC_8", right="RC_8")
    teach("#762", "#5012 - #5542", (240, 450, 45, 120) , id ="CD_8", left="LD_8")
    teach("#763", "#5012 - #5542 - #762" ,(285, 450, 45, 120) , id ="CE_8", left="LE_8")
    data("#764", (330, 450, 45, 120) , id ="CF_8", left="LF_8")
    data("#765", (375, 450, 45, 120) , id ="CG_8", left="LG_8")
    data("#766", (420, 450, 45, 120) , id ="CH_8", left="LH_8")
    data("#767", (465, 450, 45, 120) , id ="CI_8", left="LI_8")

#
    text("[工件零点G54]" , (100, 592,45,200))
    text("X",           (145, 592, 45, 15)) 
    teach("#5541", "#5011 + $m "   , (145, 612, 45, 180),LineShow.hide, id ="RB_8",  left="CB_8")
    text("Z",           (190, 592, 45, 15))
    teach("#5542", "#5542 = #5012" , (190, 612, 45, 180),LineShow.hide, id ="RC_8",  left="CC_8")

    text("[绝对坐标]", (235, 592,45,200), f24x12)
    text("X",         (280, 592, 45, 15))
    coor("X",         (280, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 592, 45, 15)) 
    coor("Z",         (325, 592, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 592, 45, 200), f24x12)
    text("X",         (415, 592, 45, 15))
    coor("X",         (415, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 592, 45, 15)) 
    coor("Z",         (460, 592, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("工件零点", 工件坐标("G54"))
    menu("+输入", 部分表达式("#5541-#5011 + ($v)"))
    menu("测量", 测量)
    menu("示教", 示教表达式) 
    menu("上一页", "磨削参数")
    menu("主界面", "main")

with page(510, 792, id="休整参数" ,text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):

    text("直角休整", (5, 1,100,792), Color.red, Align.center, f28x14)

    picture("砂轮.png"   , (100, 1, 270, 396))

    text("底面对刀位置X"    , (105, 396, 45, 198))
    text("侧面对刀位置Z"         , (150, 396, 45, 198))
    text("底面每次修整量"     , (195, 396, 45, 198))
    text("修整次数"       , (240, 396, 45, 198))  
    text("修整进给速度"     , (285, 396, 45, 198))
    text("砂轮底面宽度" , (330, 396, 45, 198))


    teach("#890", "#5011", (105 , 604, 45, 178))
    teach("#891", "#5012", (150, 604, 45, 178))
    data("#892", (195, 604, 45, 178))
    data("#893", (240, 604, 45, 178))
    data("#894", (285, 604, 45, 178))
    data("#895", (330, 604, 45, 178))


    text("[绝对坐标]", (375, 5,45,200),f24x12)
    text("X", (420, 5, 45, 15))
    coor("X", (420, 10, 45, 168),Color.white, f24x12, Align.right, Coor.abs)
    text("Z", (465, 5, 45, 15)) 
    coor("Z", (465, 10, 45, 168), Color.white, f24x12, Align.right, Coor.abs)
    text("[机床坐标]", (375, 200, 45, 200),f24x12)
    text("X", (420, 198, 45, 15))
    coor("X", (420, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)
    text("Z", (465, 198, 45, 15)) 
    coor("Z", (465, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)


    menu("基本参数", "共同参数")
    menu("磨削参数", "磨削参数")
    menu("休整参数", "休整参数")
    menu("外径量仪", "外径量仪", "#510 == 1")
    #menu("端面量仪", "端面量仪", "#503 == 1")
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("示教", 示教表达式) 
    menu("主界面", "main")


with page(510, 792, id="外径量仪" ,text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):

    text("外径量仪", (5, 1,100,792), Color.red, Align.center, f28x14)

    picture("砂轮.png"   , (100, 1, 270, 396))

    text("是否使用外径量仪"   , (150, 396, 45, 198))
    text("第一段进给速度"      , (195, 396, 45, 198))
    text("第二段进给速度"     , (240, 396, 45, 198))
    text("第三段进给速度"     , (285, 396, 45, 198))  
    text("第四段进给速度"     , (330, 396, 45, 198))
 

    #data("#510", (105 , 604, 45, 178), Font.s24x12,LineShow.hide)
    data("#510", (150, 604, 45, 178), choices={0: "不用量仪",1: "使用量仪"})
    data("#511", (195, 604, 45, 178), enable= "#510 == 1")
    data("#512", (240, 604, 45, 178), enable= "#510 == 1")
    data("#513", (285, 604, 45, 178), enable= "#510 == 1")
    data("#514", (330, 604, 45, 178), enable= "#510 == 1")

    text("[绝对坐标]", (375, 5,45,200),f24x12)
    text("X", (420, 5, 45, 15))
    coor("X", (420, 10, 45, 168),Color.white, f24x12, Align.right, Coor.abs)
    text("Z", (465, 5, 45, 15)) 
    coor("Z", (465, 10, 45, 168), Color.white, f24x12, Align.right, Coor.abs)
    text("[机床坐标]", (375, 200, 45, 200),f24x12)
    text("X", (420, 198, 45, 15))
    coor("X", (420, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)
    text("Z", (465, 198, 45, 15)) 
    coor("Z", (465, 210, 45, 168), Color.white, f24x12, Align.right, Coor.mt)

    menu("基本参数", "共同参数")
    menu("磨削参数", "磨削参数")
    menu("休整参数", "休整参数")
    menu("外径量仪", "外径量仪", "#510 == 1")
    #menu("端面量仪", "端面量仪", "#503 == 1")
    menu("", 信号翻转("F5200.0"))
    menu("", 信号翻转("F5200.0"))
    menu("示教", 示教表达式) 
    menu("主界面", "main")


#端面量仪
with page(510, 792, id="端面量仪", text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):

    text("自动量仪间距测量", (5, 1,100,792), Color.red, Align.center, f28x14)

    picture("端面量仪.JPG"   , (100, 460, 180, 300))

    text("端面量仪坐标系G59" , (100, 220,45,220))
    text("X",           (145, 220, 45, 15))
    teach("#5591", "#5011", (145, 240, 45, 180),LineShow.hide )
    text("Z",           (190, 220, 45, 15))
    teach("#5592", "#5012" , (190, 240, 45, 180),LineShow.hide)

    text("量仪与砂轮间距测量值"   , (285, 430, 45, 240) )
    data("#504",  (285, 670, 45, 120), Color.red, LineShow.hide)

    text("步骤一"   , (300, 220, 30, 150) , f20x10)  
    text("手动把量仪移动到工件表面位置"   , (330, 220, 30, 350) , f20x10)
    text("步骤二"   , (360, 220, 30, 150) , f20x10)
    text("按F1启动自动测量"   , (390, 220, 30, 200) , f20x10)
    text("步骤三"     , (420, 220, 30, 150) , f20x10)
    text("手动把砂轮移动到工件表面,再按F2," , (450, 220, 30, 350) , f20x10)
    text("进行量仪间距设定" , (480, 220, 30, 300) , f20x10)


    text("[端面量仪G59]" , (100, 5,45,200))
    text("X",           (145, 5, 45, 15)) 
    data("#5591",  (145, 25, 45, 180), Color.white, Mode.ro,LineShow.hide )
    text("Z",           (190, 5, 45, 15))
    data("#5592",   (190, 25, 45, 180), Color.white, Mode.ro,LineShow.hide)

    text("[绝对坐标]", (235, 5,45,200), f24x12)
    data("#4005",     (235, 165, 45, 45) , f24x12, Mode.ro, LineShow.hide, choices={45: "G45",55: "G55" ,56: "G56" ,57: "G57",58: "G58",59: "G59"} )
    text("X",         (280, 5, 45, 15))
    coor("X",         (280, 5, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 5, 45, 15)) 
    coor("Z",         (325, 5, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 5, 45, 200), f24x12)
    text("X",         (415, 5, 45, 15))
    coor("X",         (415, 5, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 5, 45, 15)) 
    coor("Z",         (460, 5, 45, 200), Color.white, f24x12, Align.right, Coor.mt)

    #menu("端面量仪", "端面量仪")
    menu("自动测量", action=运行脚本('''IF RESULT_YES==MSGBOX["是否执行端面自动测量\\n是,执行端面测量\\n否,不执行端面测量", MB_YESNOCANCEL, "端面自动测量"]
    THEN #990 = 1 #100 = 0 ENDIF'''), enable="F3500.0 == 0")
    menu("间距设定", action=运行脚本('''IF RESULT_YES==MSGBOX["是否自动设定量仪与砂轮间距\\n自动设定量仪与砂轮间距前,请执行自动测量\\n是,设定量仪与砂轮间距\\n否,不设定量仪与砂轮间距", MB_YESNOCANCEL, "量仪与砂轮间距"]
    THEN #504 = #5012 - #100 ENDIF'''), enable="F3500.0 == 0")

    #menu("自动测量", 工件坐标("G59"))
    #menu("间距设定", 工件坐标("G59"))
    
    menu("", 信号翻转("F5200.0"))
    menu("量仪参数", "量仪参数" ,"k80.0 == 0")
    menu("", 信号翻转("F5200.0"))
    menu("量仪零点", 工件坐标("G59"))
    menu("示教", 示教表达式, enable="F3500.0 == 0") 


    menu("主界面", "main")

with page(510, 792, id="量仪参数", text=(Color.green, Align.left, f24x12), data=(Color.cyan, f24x12, LineShow.show)):

    text("自动量仪间距测量", (5, 1,100,792), Color.red, Align.center, f28x14)

    picture("端面量仪.JPG"   , (100, 460, 180, 300))

    text("端面量仪坐标系G59" , (100, 220,45,220))
    text("X",           (145, 220, 45, 15)) 
    teach("#5591", "#5591 = #5011", (145, 240, 45, 180),LineShow.hide )
    text("Z",           (190, 220, 45, 15))
    teach("#5592", "#5592 = #5012" , (190, 240, 45, 180),LineShow.hide)

    text("量仪与砂轮间距测量值"   , (285, 430, 45, 240) )
    data("#504",  (285, 670, 45, 120), Color.red, LineShow.hide)

    text("步骤一"   , (300, 220, 30, 150) , f20x10)  
    text("手动把量仪移动到工件表面位置"   , (330, 220, 30, 350) , f20x10)
    text("步骤二"   , (360, 220, 30, 150) , f20x10)
    text("按F1启动自动测量"   , (390, 220, 30, 200) , f20x10)
    text("步骤三"     , (420, 220, 30, 150) , f20x10)
    text("手动把砂轮移动到工件表面,再按F2," , (450, 220, 30, 350) , f20x10)
    text("进行量仪间距设定" , (480, 220, 30, 300) , f20x10)



    text("[端面量仪G59]" , (100, 5,45,200))
    text("X",           (145, 5, 45, 15)) 
    data("#5591",  (145, 25, 45, 180), Color.white, Mode.ro,LineShow.hide )
    text("Z",           (190, 5, 45, 15))
    data("#5592",   (190, 25, 45, 180), Color.white, Mode.ro,LineShow.hide)

    text("[绝对坐标]", (235, 5,45,200), f24x12)
    text("X",         (280, 5, 45, 15))
    coor("X",         (280, 5, 45, 200), Color.white, f24x12, Align.right, Coor.abs)
    text("Z",         (325, 5, 45, 15)) 
    coor("Z",         (325, 5, 45, 200), Color.white, f24x12, Align.right, Coor.abs)

    text("[机床坐标]", (370, 5, 45, 200), f24x12)
    text("X",         (415, 5, 45, 15))
    coor("X",         (415, 5, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
    text("Z",         (460, 5, 45, 15)) 
    coor("Z",         (460, 5, 45, 200), Color.white, f24x12, Align.right, Coor.mt)
#   menu("量仪参数", "外径量仪" ,"k40.0 == 0")
    menu("上一页", "端面量仪")


download(__file__,"192.168.1.101")


#generate(__file__)
#preview(__file__)