from PIL import Image, ImageDraw, ImageFont

im1 = Image.open("image1.jpeg")
im2 = Image.open("image2.png")

im_crop = im2.crop((39, 39, 371, 371))

# resizing
resized_im = im_crop.resize(
    (round(im_crop.size[0] * 1.334), round(im_crop.size[1] * 1.334))
)

# writing the id
draw = ImageDraw.Draw(im1)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Aaargh.ttf", 80)
qrCodeId = 1
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((21, 1180), str(qrCodeId), "black", font=font)

im1.paste(resized_im, (45, 575))
# im1.save("paste.jpg", quality=95)

# convert to pdf
# image_1 = Image.open("paste.jpg")
im_1 = im1.convert("RGB")
im_1.save("QrCode.pdf")
