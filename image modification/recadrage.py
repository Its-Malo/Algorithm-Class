from PIL import Image

image = Image.open("quantique.jpg")
pixels = image.load()

largeur,hauteur = image.size

recadrage = 20

new_image = Image.new(image.mode,(largeur-recadrage*2,hauteur-recadrage*2))
new_pixels = new_image.load()

for x in range(largeur - recadrage*2):
    for y in range(hauteur - recadrage*2):
        pixel = pixels[x,y]

        if(x > recadrage and y > recadrage):
            new_pixels[x,y] = pixel

#new_pixels[0,0] = pixels[1,1]
#new_pixels[x,y] = pixel[x + recadrage,y + recadrage]

new_image.save("new.jpg")