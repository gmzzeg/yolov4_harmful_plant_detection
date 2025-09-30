import cv2 as cv

# Tespit eşiği değerleri
Conf_threshold = 0.70
NMS_threshold = 0.30

# Sınıf isimleri ve özellikleri
class_name = ["pink", "black", "orange", "white", "blue", "purple"]
class_properties = {
    "pink": "zararlı",
    "black": "zararlı",
    "orange": "zararlı",
    "white": "zararsız",
    "blue": "zararlı",
    "purple": "zararlı",
}

# Model yükleme
net = cv.dnn.readNet("yolov4.cfg", "yolov4.weights")
model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

# Test edilecek resim
image_path = "plant.jpg"  
frame = cv.imread(image_path)

# Renkler
COLORS = [(255,180,220),(0,0,0),(0,165,255),(255,255,255),(255,0,0),(128,0,128)]

# Nesne tespiti
classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)

# Sonuçları çiz
for (classid, score, box) in zip(classes, scores, boxes):
    color = COLORS[int(classid) % len(COLORS)]
    label = "%s : %.2f" % (class_name[classid], score)
    cv.rectangle(frame, box, color, 2)
    cv.putText(frame, label, (box[0], box[1]-10),
               cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

    detected_class = class_name[classid]
    property = class_properties.get(detected_class, "Unknown property")
    print(f"BITKI: {detected_class}, TURU: {property}")

# Sonucu göster
cv.imshow("plant.jpg", frame)
cv.waitKey(0)
cv.destroyAllWindows()
