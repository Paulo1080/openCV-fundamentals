import cv2 as cv

img = cv.imread('park.jpg')
cv.imshow('Imagem', img)

#converter para tons de cinza (grayscale)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', gray)


#resized (redimensionamento)
resized = cv.resize(gray, (700,700), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping (Recorte de imagem, obviamente menor que entrada)
cropped = img[50:200, 200:400]
cv.imshow('imagemcroppada', cropped)

#dilatar imagens
dilated = cv.dilate(img, (9,9), iterations=3)
cv.imshow('Dilatar',dilated)

#filtro gaussiano
blur1 = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur1', blur1)

blur2 = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur2', blur2)

#filtro de bordas baseado em gauss: canny edge
canny1 = cv.Canny(blur1, 125, 175)
cv.imshow('Canny Edges 1', canny1)

canny2 = cv.Canny(blur2, 125, 175)
cv.imshow('Canny Edges 2', canny2)



cv.waitKey(0)