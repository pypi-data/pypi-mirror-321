import cv2

def draw_centers(image, centers):
    for center in centers:
        c = (int(center.px[0]), int(center.px[1]))
        cv2.drawMarker(image, c, (0, 0, 255), cv2.MARKER_CROSS, 30, 8)
    return image