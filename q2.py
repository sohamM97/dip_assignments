import numpy as np 
import cv2

def point_process(point,gamma):
	
	L=256
	c=(L-1)**(1-gamma)
	return int(c*(point**gamma))


def gamma_transform(img,gamma):

	N,M=img.shape
	
	for row in range(N):
		for col in range(M):
			img[row][col]=point_process(img[row][col],gamma)


if __name__=='__main__':

	img=cv2.imread('q1_input.jpg')
	img_blue,img_green,img_red=cv2.split(img)

	gamma_transform(img_blue,5)
	gamma_transform(img_green,5)
	gamma_transform(img_red,5)

	final1=cv2.merge((img_blue,img_green,img_red))
	cv2.imwrite('q2_output_1.jpg',final1)
	#cv2.imshow('image',final1)
	#cv2.waitKey(0)

	img_blue,img_green,img_red=cv2.split(img)
	gamma_transform(img_blue,0.2)
	gamma_transform(img_green,0.2)
	gamma_transform(img_red,0.2)

	final2=cv2.merge((img_blue,img_green,img_red))
	cv2.imwrite('q2_output_2.jpg',final2)
	#cv2.imshow('image',final2)
	#cv2.waitKey(0)

	#cv2.destroyAllWindows()