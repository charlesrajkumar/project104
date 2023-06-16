import cv2


img = cv2.imread('solar-system.jpg')

cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "mercury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "venus",
            (180,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "earth",
            (280,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "mars",
            (380,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "jupiter",
            (580,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "saturn",
            (780,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "uranus",
            (950,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )




cv2.imshow('output',img)
cv2.waitKey(0)
