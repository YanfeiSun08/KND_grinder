# 外圆磨床程序

本项目是专用于KND数控系统的一套外圆磨削解决方案。主要功能有

* 外圆磨削
  * 外圆直切磨削
  * 外圆往复磨削
  * 外圆量仪直切磨削
  * 外圆量仪往复磨削
* 砂轮休整
* 端面量仪
  * 工件端面位置测量
  * 量仪与砂轮间距测量
  * 工件端面误差检查
* 外径量仪
* 自定义UI界面



## 程序结构

* 主程序 O0001 
* 端面测量  ---O9100
  * 
* 工件磨削  ---O9200
  * 
* 砂轮休整  ---OP9300
  * 



## 主程序



### 参数

| 序号 | 参数名称       | 地址 | 局部变量 | 程序变量 | 说明           |
| ---- | -------------- | ---- | -------- | -------- | -------------- |
| 1    | 起点台阶       | A    | #1       | #201     | 起点台阶       |
| 2    | 终点台阶       | B    | #2       | #202     | 终点台阶       |
| 3    | 台阶计数变量号 | C    | #3       | #203     | 台阶计数变量号 |
| 4    | 加工计数变量号 | D    | #7       | #207     | 加工计数变量号 |
| 5    | 模式选择       | H    | #11      | #211     | 模式选择       |







```
O0001 (主程序) ;
G54 (工件坐标系) ;
G00 X#501 (X轴安全位置) ;
G65 P9100 A B C E H (端面测量) ;
G65 P9200 A B C E H (工件磨削) ;
G65 P9300 A B C E (砂轮休整) ;
M30 ;
```
