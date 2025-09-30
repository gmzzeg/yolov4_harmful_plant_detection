# import cv2
# vidcap=cv2.VideoCapture("video2.mp4")
# succes,image=vidcap.read()
# count=0
# while succes:
#     cv2.imwrite("white.%d.jpg" % count, image)
#     succes,image=vidcap.read()
#     print('read a new frame:' , succes)
#     count+= 1


# OpenCV ve zaman kütüphanesi içe aktarılıyor.
import cv2 as cv

# Tespitlerin doğruluk eşiği ve Non-Maximum Suppression (NMS) eşiği tanımlanıyor.
Conf_threshold = 0.70  # Tespit için minimum doğruluk eşiği
NMS_threshold = 0.30   # NMS için eşik değeri (çakışan kutuların filtrelenmesi)

# Tespit edilecek sınıfların isimleri ve özellikleri tanımlanıyor.
class_name = ["pink", "black", "orange", "white", "blue", "purple"]

# Her sınıfın özellikleri bir sözlükte saklanıyor.
class_properties = {
    "pink": "zararlı",
    "black": "zararlı",
    "orange": "zararlı",
    "white": "zararsız",
    "blue": "zararlı",
    "purple": "zararlı",
}

# YOLO modelinin ağı ve ağırlıkları yükleniyor.
net = cv.dnn.readNet("yolov4.cfg", "yolov4.weights")

# Tespit modeli oluşturuluyor ve giriş parametreleri ayarlanıyor.
model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)  # Giriş boyutu, normalleştirme ölçeği ve renk dönüşümü.

# Resim dosyası okunuyor.
image_path = "bitki.14.jpg"  # Resim dosyasının yolu.
frame = cv.imread(image_path)  # Resmi yükle.

# YOLO modeli ile tespit yapılıyor.
classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)

# Çizim için farklı renkler tanımlanıyor (BGR formatında).
COLORS = [(255, 180, 220), (0, 0, 0), (0, 165, 255), (255, 255, 255), (255, 0, 0), (128, 0, 128)]

# Tespit edilen nesneler üzerinde döngü.
for (classid, score, box) in zip(classes, scores, boxes):
    # Sınıf id'sine göre renk seçiliyor.
    color = COLORS[int(classid) % len(COLORS)]
    # Tespit etiketi oluşturuluyor.
    label = "%s : %f" % (class_name[classid], score)
    # Çerçeve üzerine tespit kutusu çiziliyor.
    cv.rectangle(frame, box, color, 2)  # Dikdörtgen çerçeve çizimi.
    # Tespit etiketi kutunun üzerine yazılıyor.
    cv.putText(frame, label, (box[0], box[1] - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

    # Sınıf ismine göre özellik bulunuyor ve konsola yazdırılıyor.
    detected_class = class_name[classid]
    property = class_properties.get(detected_class, "Unknown property")
    print(f"BITKI: {detected_class}, TURU: {property}")

# İşlenmiş çerçeve gösteriliyor.
cv.imshow('Detected Image', frame)  # 'Detected Image' adlı pencere açılıyor ve işlenmiş görüntü gösteriliyor.
cv.waitKey(0)  # Kullanıcı bir tuşa basana kadar bekleniyor.
cv.destroyAllWindows()  # Tüm OpenCV pencereleri kapatılıyor.

# Sonuçları bir dosyaya kaydetmek için aşağıdaki satırı da ekleyebilirsiniz:
cv.imwrite("output_detected_image.jpg", frame)

