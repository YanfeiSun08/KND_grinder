O9225 (外圆量仪往复粗磨) ;
(判断程序调用方法) ;
IF [ ! ISNULL[#16] ] GOTO 10 ( G65调用 ) ;
PARAMS[ r1,r2,r3,r4,r8,r9,r18,r20,r21,r23] (与主程序CALL配对使用) ;
N10 (判断程序调用结束) ;
(子程序局部变量赋值与程序使用变量) ;
#201 = #1  (工件外圆毛胚尺寸) ;
#202 = #2  (工件外圆图纸尺寸) ;
#203 = #3  (端面对刀点Z ) ;
#204 = #4  (粗磨进给量) ;
#208 = #8  (粗磨进给速度) ;
#209 = #9  (粗磨Z轴移动速度)
#218 = #18 (Z轴磨削区间) ;
#220 = #20 (到位停顿时间) ;
(变量赋值结束) ;
#285 = #203 (Z轴起点) ;
#286 = #203 + #218 (Z轴终点) ;
#270 = 1 (粗磨次数初始化) ;
N100 ;
#280 = #201 - #204 * #270 (每次粗磨进刀位置) ;
#281 = #202 (粗磨进刀终点位置) ;
G31 X#280 F#509 P1 (X轴量仪进刀) ;
G31 X#280 F#510 P2 (X轴量仪进刀) ;
G31 X#280 F#511 P3 (X轴量仪进刀) ;
M54 (量仪进) ;
G01 Z#286 F#209 (Z轴移动到终点位置) ;
G04 P#202 ;
G01 Z#285 F#209 (Z轴移动到起点位置) ;
#270= #270 + 1 (粗磨次数加一) ;
IF [ #1002 == 0 ] GOTO 100 (进刀位置大与终点位置，到N100 ) ;
M99 ;