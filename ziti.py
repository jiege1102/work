# # '''字体设置1.py'''
# # #导入库
# # from docx import Document
# # from docx.oxml.ns import qn
# # from docx.enum.style import WD_STYLE_TYPE
# #
# # document = Document() # 新建docx文档
# #
# # # 设置宋体字样式
# # style_font = document.styles.add_style('宋体', WD_STYLE_TYPE.CHARACTER)
# # style_font.font.name = '宋体'
# # document.styles['宋体']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
# #
# # # 设置楷体字样式
# # style_font = document.styles.add_style('楷体', WD_STYLE_TYPE.CHARACTER)
# # style_font.font.name = '楷体'
# # document.styles['楷体']._element.rPr.rFonts.set(qn('w:eastAsia'), u'楷体')
# #
# # # 设置华文中宋字样式
# # style_font = document.styles.add_style('华文中宋', WD_STYLE_TYPE.CHARACTER)
# # style_font.font.name = '华文中宋'
# # document.styles['华文中宋']._element.rPr.rFonts.set(qn('w:eastAsia'), u'华文中宋')
# #
# # paragraph1 = document.add_paragraph() # 添加段落
# # run = paragraph1.add_run(u'aBCDefg这是中文', style='宋体') # 设置宋体样式
# #
# # font = run.font #设置字体
# # font.name = 'Cambira' # 设置西文字体
# # paragraph1.add_run(u'aBCDefg这是中文', style='楷体').font.name = 'Cambira'
# # paragraph1.add_run(u'aBCDefg这是中文', style='华文中宋').font.name = 'Cambira'
# #
# # document.save('output/字体设置1.docx')
#
# # r = float(input('请输入圆的半径(cm): '))
# # zc = 2 * r * 3.1415
# # mj = r * r * 3.1415
# # print(f'圆的周长 = {zc:.2f}cm')
# # print(f'圆的面积 = {mj:.2f}cm')
#
# # year = int(input('请输入年份: '))
# # # 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
# # is_leap = year % 4 == 0 and year % 100 != 0 or \
# #           year % 400 == 0
# # if is_leap == True:
# #     print("是闰年")
# # else:
# #     print("不是闰年")
# """
# 分段函数求值
#
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
#
# Version: 0.1
# Author: 骆昊
# """
# # x = float(input("输入x的值："))
# # if x > 1:
# #     y = 3 * x + 5
# # elif -1 <= x <= 1:
# #     y = x + 2
# # else:
# #     y = 5 * x + 3
# # print(f'f({x:.2f}) = {y:.2f}')
# # print('f(%.2f) = %.2f' % (x, y))
# """
# 如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
# """
# """
# 百分制成绩转换为等级制成绩
#
# Version: 0.1
# Author: 骆昊
# """
# # score = float(input('请输入成绩: '))
# # if score >= 90:
# #     grade = 'A'
# # elif score >= 80:
# #     grade = 'B'
# # elif score >= 70:
# #     grade = 'C'
# # elif score >= 60:
# #     grade = 'D'
# # else:
# #     grade = 'E'
# # print('对应的等级是:', grade)
#
# """
# 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
# """
# # a = float(input("a = "))
# # b = float(input("b = "))
# # c = float(input("c = "))
# # if a+b>c and a+c>b and b+c>a:
# #     print('周长=%.2f' % (a+b+c)+'cm')
# #     p = (a + b + c) / 2
# #     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# #     print('面积=%.2f' % (area)+'cm')
# # else:
# #     print('不能构成三角形')
#
# def calculate_triangle_properties(a, b, c):
#     def is_triangle(a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     if is_triangle(a, b, c):
#         perimeter = a + b + c
#         s = perimeter / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         return f'周长 = {perimeter:.2f}cm', f'面积 = {area:.2f}cm'
#     else:
#         return '不能构成三角形'
#
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# result = calculate_triangle_properties(a, b, c)
# for item in result:
#     print(item)
#
#
#
"""
猜数字游戏

Version: 0.1
Author: 骆昊
"""
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')
for i in range(1, 10):
    for j in range(1, i + 1):

        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
