from PIL import Image

image = Image.open("images.jpg")
pixels = image.load()

largeur,hauteur = image.size

imageR = Image.new(image.mode,(largeur,hauteur))
new_pixels = imageR.load()

for x in range(largeur):
    for y in range(hauteur):
        new_pixels[x, hauteur - y -1] = pixels[x,y]
    


imageR.save("new.jpg")
