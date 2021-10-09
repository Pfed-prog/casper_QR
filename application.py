import base64
from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from io import BytesIO

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SquareGradiantColorMask


application = Flask(__name__)
app = application


def return_image(image):
    data = BytesIO()
    image.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data

def generate_image(address:str='', amount=0, message:str='', transaction:str='', network:str='casper'):

    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, version=1,
    )

    # taking url or text
    if network =='casper':
        url = f"{network}:{address}?amount={amount}&message={message}&transfer_id={transaction}"
    else:
        url = f"{network}?recipient={address}&amount={amount}&transfer_id={transaction}"
    # addingg URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make(fit=True)

    # get the logo and resize it
    Logo_link = './static/casper.png'
    # taking base width
    basewidth = 100
    logo = Image.open(Logo_link)
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    # adding color to QR code
    QRimg = QRcode.make_image(
        back_color="white",\
        image_factory=StyledPilImage,\
        module_drawer=RoundedModuleDrawer(),\
        color_mask=SquareGradiantColorMask()\
    ).convert('RGB')

    # position the logo
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo,pos)# put QRimg.paste(logo,pos,log) to make the logo fully transparent

    # set size of QR code
    return QRimg.resize((400, 400), Image.ANTIALIAS)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        data = [x for x in request.form.values()]
        image = generate_image(data[0], data[1], data[2], data[3], data[4])

    else: 
        image = generate_image()

    image.save('./static/output.png')
    img_data = return_image(image)
    return render_template("home.html", img_data = img_data.decode('utf-8'), address=data[0])

@app.route("/img", methods=["GET"])
def send():
    return send_from_directory(directory='./static/',path='output.png',as_attachment=True)

if __name__ == "__main__":
    app.run()