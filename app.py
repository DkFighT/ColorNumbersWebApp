from flask import Flask, render_template, url_for, request, jsonify
import colorgram
import requests
import random
from PIL import Image, ImageFilter
import base64
from io import BytesIO

app = Flask(__name__)

images = ['https://i.pinimg.com/736x/91/f5/ec/91f5ec83f65e3840aa4384ac0121fa33.jpg',
          'https://i.pinimg.com/736x/3e/50/6e/3e506e21bea2e4e85cc629649fb883ac.jpg',
          'https://i.pinimg.com/564x/44/a9/99/44a999c2b1c654598124ab8fd32210c3.jpg',
          'https://i.pinimg.com/736x/c7/39/58/c73958f37af03a71953a505d2da1d2ea.jpg',
          'https://i.pinimg.com/564x/8b/49/ac/8b49ac500b0004d861e66de4b24ed266.jpg',
          'https://i.pinimg.com/564x/14/d7/5d/14d75d35bf236f4e32c053d750d81107.jpg',
          'https://i.pinimg.com/564x/aa/3d/9a/aa3d9a46a8f92f80c3827414a44d6b75.jpg',
          'https://i.pinimg.com/564x/d0/9f/d1/d09fd1987db554e3fce3ad521e8adf82.jpg',
          'https://i.pinimg.com/736x/30/15/c4/3015c49a1965aef16901d846778bcf4a.jpg',
          'https://i.pinimg.com/564x/78/df/fe/78dffe086f2d53f0780706d35d09a0a4.jpg',
          'https://i.pinimg.com/564x/b2/c4/8d/b2c48dbdb81331b463e5e74aed9ae46e.jpg',
          'https://i.pinimg.com/564x/85/ee/7f/85ee7f3de995d21eb34fdb4796161048.jpg',
          'https://i.pinimg.com/736x/55/e4/a8/55e4a8b50726188b2e2f3a7058802db9.jpg',
          'https://i.pinimg.com/564x/cd/ee/2d/cdee2d4f6bb8dc541519eb5fee29b85f.jpg',
          'https://i.pinimg.com/564x/44/a9/99/44a999c2b1c654598124ab8fd32210c3.jpg',
          'https://i.pinimg.com/736x/df/78/20/df7820197c19d46284f00c5e83eadbac.jpg',
          'https://i.pinimg.com/736x/af/0b/1b/af0b1b90c29e0b4002b3b526461baf17.jpg',
          'https://i.pinimg.com/736x/34/dd/46/34dd46945af60100928bcfc028d2aa9a.jpg',
          'https://i.pinimg.com/564x/0a/e4/04/0ae404abeac8c4d8107fa2e367996ee4.jpg',
          'https://i.pinimg.com/564x/8c/7e/a6/8c7ea6bd64b10b02c406e69284c16458.jpg',
          'https://i.pinimg.com/736x/f4/bb/6d/f4bb6d50853d1959ca94b8e314b6f437.jpg',
          'https://i.pinimg.com/564x/5e/81/1a/5e811ad25422ba9e5812e587485b6120.jpg',
          'https://i.pinimg.com/564x/80/4a/ac/804aacb812af3f489cef89b850b48f55.jpg',
          'https://i.pinimg.com/736x/2b/97/80/2b97807a1f2c8e2f530ee4c7cbb871cd.jpg',
          'https://i.pinimg.com/564x/bb/3e/40/bb3e40c194d57596502440532276d69a.jpg',
          'https://i.pinimg.com/564x/c2/6a/03/c26a03716d9cf6f451f581e913d73743.jpg',
          'https://i.pinimg.com/564x/49/d6/09/49d609d55ea1dea4ce47eddb582d86e4.jpg',
          'https://i.pinimg.com/564x/56/e0/f6/56e0f646b58349c9bdeb5f82b6b4c67d.jpg',
          'https://i.pinimg.com/564x/af/70/c0/af70c09f1669b259e42963d9bea77720.jpg',
          'https://i.pinimg.com/564x/a7/ac/d7/a7acd7ab0c758903d433f2b5f786580d.jpg']


def image_base64(im):
    with BytesIO() as buffer:
        buffer.truncate(0)
        im.save(buffer, 'jpeg')
        return base64.b64encode(buffer.getvalue()).decode()

def check(color, orig_col):
    count = 0
    for i in range(3):
        if int(color[i]) - 30 <= orig_col[i] <= int(color[i]) + 30:
            count += 1
    if count == 3:
        return True
    else:
        return False

def convert_image(threshold, mask):
    th_im = mask.point(lambda x: 255 if x > threshold else 0)
    filter = th_im.filter(ImageFilter.CONTOUR)
    return filter

def create_images():
    global img, colors, arr, im
    arr = []
    im = Image.open(requests.get(img, stream=True).raw)
    scale_factor = 0.5
    im = im.resize((int(im.size[0] * scale_factor), int(im.size[1] * scale_factor)))
    colors = colorgram.extract(im, 9)
    t_im = im.convert("L")
    l_im = im.convert("L")
    thresholds = [10, 70, 140, 200]
    l_im = (l_im.point(lambda x: 255 if x > thresholds[0] else 0)).filter(ImageFilter.CONTOUR)
    for i in thresholds:
        edit_img = convert_image(i, t_im)
        l_im.paste(edit_img, (0, 0), edit_img.point(lambda x: 0 if x == 255 else 255))
    l_im = l_im.convert('RGB')
    arr.append(image_base64(l_im))
    # width, height = l_im.size
    # arr.append(image_base64(l_im))
    # mask = Image.new("L", (width, height), 0)
    # for c in range(len(colors)):
    #     col = (colors[c].rgb.r, colors[c].rgb.g, colors[c].rgb.b)
    #     for x in range(width):
    #         for y in range(height):
    #             if check(col, im.getpixel((x, y))):
    #                 mask.putpixel((x, y), 255)

    #     l_im.paste(im, (0, 0), mask)
    #     arr.append(image_base64(l_im))
    # arr = arr[:-1]
    # arr.append(image_base64(im))


def create_next_image(color, img, orig_img):
    img = img.convert('RGB')
    width, height = img.size
    # arr.append(image_base64(l_im))
    mask = Image.new("L", (width, height), 0)
    for x in range(width):
        for y in range(height):
            if check(color, orig_img.getpixel((x, y))):
                mask.putpixel((x, y), 255)

    img.paste(orig_img, (0, 0), mask)
    return img

@app.route('/getimg', methods=['GET', 'POST'])
def get_img():
    global im
    data = request.get_json()
    image = data['image'].split('"')[1].split(',')[1]
    msg = base64.b64decode(image)
    buf = BytesIO(msg)
    img = Image.open(buf)
    color = tuple(data['color'].split('(')[1][:-1].split(','))
    new_img = image_base64(create_next_image(color, img, im))
    res = jsonify({'image': f'{new_img}'})
    return res

@app.route('/getlast', methods=['GET'])
def get_last():
    global im
    new_img = image_base64(im)
    res = jsonify({'image': new_img})
    return res

@app.route('/', methods=['POST', 'GET'])
def index():
    global img, colors, arr
    img = random.choice(images)
    create_images()
    col = []
    t_col = []
    for i in range(len(colors)):
        col.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
        t_col.append((255 - colors[i].rgb.r, 255 - colors[i].rgb.g, 255 - colors[i].rgb.b))
    
    return render_template('index.html', image=arr, col=col, t_col=t_col, href_img = img)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
