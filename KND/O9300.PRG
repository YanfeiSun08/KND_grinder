O9030 (修砂轮主程序) ;
(判断程序调用方法) ;
IF [ ! ISNULL[#16] ] GOTO 10 ( G65调用 ) ;
PARAMS[r1,r2,r3,r7]  (与主程序CALL配对使用) ;
N10 (判断程序调用结束) ;
(子程序局部变量赋值与程序使用变量) ;
#201 = #1 (砂轮形状) ;
#202 = #2 (修砂轮时机设定) ;
#203 = #3 (修砂轮时机计数变量号) ;
#207 = #7 (模式选择1磨削，2休整，3端面量仪) ;
(变量赋值结束) ;
IF [#207 == 1 ] GOTO 10 ;
IF [#207 == 2 ] GOTO 100 ;
IF [#207 == 3 ] GOTO 700 ;
GOTO 700 ;
N10 ;
IF [ ISNULL [#[[INT]#203]]] THEN #[[INT]#203] = 0 ;
IF [ #202 == 0 ] GOTO 700 ;
IF [ #202 > #[[INT]#203]] GOTO 700 ;
N100 ;
IF [ #201 == 1 ] GOTO 200 ;
IF [ #201 == 2 ] GOTO 300 ;
IF [ #201 == 3 ] GOTO 400 ;
N200 ;
(直角) ;
CALL[ 9031 ,800,801,#802,0,#803,0,#804,#805] ;
GOTO 500 ;
N300 ;
(圆角) ;
GOTO 500 ;
() ;
N400 ;
(自定义) ;
GOTO 500 ;
N500 ;
(计数清零) ;
#[[INT]#3] = 0 ;
(退刀) ;
N700 ;
G54 ;
G01 Z0 ;
G01 X#501 F1000 ;
M99 ;
