import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
if __name__ == "__main__":
    mq = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 40,
        border = 10,
        )
    data_content = 'hello there'
    mq.add_data(data_content)
    mq.make(fit=True)
    img = mq.make_image(fill_color="black", back_color="white",image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
    #make_image(embeded_image_path='image.png')
    type(img)
    img.save('qrcode_image.png')
    
