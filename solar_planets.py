import cv2
img=cv2.imread("images/images/solar-system.jpg")
cv2.putText(img, 
"Sun",
(20, 300),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Mercury",
(105, 250),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Venus",
(190, 250),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Earth",
(290, 260),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Mars",
(390, 240),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Jupitar",
(490, 60),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Saturn",
(750, 100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Uranus",
(950, 100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.putText(img, 
"Neptune",
(1100, 100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255, 255, 255)
)
cv2.imshow("display image",img)
cv2.waitKey(0)