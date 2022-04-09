import cv2

#Leitura da imagem desejada (deixe ela no mesmo diretório deste arquivo)
image = cv2.imread("seu arquivo.jpeg")

#Tornar a foto cinza
foto_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Tornar a foto em preto e branco, mude os parâmetros do threshold para seus desejados
thresh, foto_final = cv2.threshold(foto_cinza, 160, 400, cv2.THRESH_BINARY)

#Resultado final da imagem
cv2.imshow("seu arquivo.jpeg", foto_final)

cv2.waitKey(0)
