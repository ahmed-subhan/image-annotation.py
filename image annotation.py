import cv2
import matplotlib.pyplot as plt

image_path = 'example.jpg'
image = cv2.imread(image_path)


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


hight, width, _ = image_rgb.shape



rect1_width, rect1_hight = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_hight)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)


rect2_width, rect2_hight = 200, 150
top_left2 = (width - rect2_width - 20, hight - rect2_hight - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_hight)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)


center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_hight // 2
center2_x = top_left2[0] + rect2_width //2
center2_y = top_left2[1] + rect2_hight // 2