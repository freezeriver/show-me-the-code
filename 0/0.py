# encoding = utf-8

from PIL import Image,ImageDraw,ImageFont,ImageColor

def add_num(img):
    draw_img = ImageDraw.Draw(img)        # 创建一个画布
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)   # 创建一个字体对象
    fillcolor = ImageColor.colormap.get('red')                                # 设置字体填充颜色
    width,height = img.size
    draw_img.text((width-30,0),'1',font=myfont,fill=fillcolor)              # 将数字写入图片
    img.save('result.jpg','jpeg')
    return 0


if __name__ == '__main__':
    image = Image.open('test.jpg')
    add_num(image)

