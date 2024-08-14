from flask import Flask, render_template, url_for, request, redirect
import colorgram
import requests
import random

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

@app.route('/', methods=['POST', 'GET'])
def index():
    img = random.choice(images)
    print(img)
    colors = colorgram.extract(requests.get(img, stream=True).raw, 7)
    col = []
    t_col = []
    for i in range(len(colors)):
        col.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
        t_col.append((255 - colors[i].rgb.r, 255 - colors[i].rgb.g, 255 - colors[i].rgb.b))
    return render_template('index.html', image=img, col=col, t_col=t_col)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()