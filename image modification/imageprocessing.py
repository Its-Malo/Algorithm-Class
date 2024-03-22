from PIL import Image

image = Image.open("quantique.jpg")
pixels = image.load()

print("module de l'image : " + image.mode)
print("bande de l'image : " + str(image.getbands()))

largeur,hauteur = image.size
print(largeur,hauteur)

new_image = Image.new(image.mode,(largeur,hauteur))
new_pixels = new_image.load()

for x in range(largeur):
    for y in range(hauteur):
        pixel = pixels[x,y]
        new_pixels[x,y] = (255-pixel[0], 255-pixel[1], 255-pixel[2])

new_image.save("new.jpg")