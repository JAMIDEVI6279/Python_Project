import qrcode as qr     #importing the libraries
img = qr.make("https://www.youtube.com/@wscubetech/playlists")    #converting the link into the qrcode
img.save("wscube_youtube.png")         #Saving the qrcode in to the png format




"""
We import the qrcode library.
We use the qr.make() function to generate a QR code with a specific URL.
We save the generated QR code image to a file named "wscube_youtube.png"."""