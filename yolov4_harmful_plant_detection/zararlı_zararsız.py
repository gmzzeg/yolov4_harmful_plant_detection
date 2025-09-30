# OpenCV kütüphanesi içe aktarılıyor.
import cv2 as cv

# Tespitlerin doğruluk eşiği ve Non-Maximum Suppression (NMS) eşiği tanımlanıyor.
Conf_threshold = 0.70 # Tespit için minimum doğruluk eşiği 
NMS_threshold = 0.30  # NMS için eşik değeri (çakışan kutuların filtrelenmesi)

# Çizim için farklı renkler tanımlanıyor (BGR formatında).

# Tespit edilecek sınıfların isimleri ve özellikleri tanımlanıyor.
class_name = ["pink", "black", "orange", "white", "blue","purple"]
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
# Kameradan video akışı başlatılıyor.
cap = cv.VideoCapture(0)  # 0, varsayılan kamera kaynağını temsil eder.
# Sonsuz döngüde video akışı işleniyor.
while True:
    # Kamera çerçevesi okunuyor.
    ret, frame = cap.read()  # ret: Çerçeve okuma başarılı mı? frame: Okunan çerçeve.
    
    # Kamera akışı sona ererse döngü kırılıyor.
    if not ret:
        break
    # YOLO modeli ile tespit yapılıyor.
    classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
    # classes: Tespit edilen sınıfların indeksleri.
    # scores: Sınıfların doğruluk puanları.
    # boxes: Her tespit için dikdörtgen kutu koordinatları.

    COLORS=[(255, 180, 220),(0,0,0),(0,165,255),(255,255,255),(255,0,0),(128,0,128)]
    # Tespit edilen nesneler üzerinde döngü.
    for (classid, score, box) in zip(classes, scores, boxes):
        # Sınıf id'sine göre renk seçiliyor.
        color = COLORS[int(classid) % len(COLORS)]
        # Tespit etiketi oluşturuluyor.
        label = "%s : %f" % (class_name[classid], score)
        # Çerçeve üzerine tespit kutusu çiziliyor.
        cv.rectangle(frame, box, color, 2)  # Dikdörtgen çerçeve çizimi.
        # Tespit etiketi kutunun üzerine yazılıyor.
        cv.putText(frame, label, (box[0], box[1] -10), cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

        # Sınıf ismine göre özellik bulunuyor ve konsola yazdırılıyor.
        detected_class = class_name[classid]
        property = class_properties.get(detected_class, "Unknown property")
        print(f"BITKI: {detected_class}, TURU: {property}")
    # İşlenmiş çerçeve ekranda gösteriliyor.
    cv.imshow('frame', frame)  # 'frame' adlı pencere açılıyor ve işlenmiş görüntü gösteriliyor.
    key = cv.waitKey(1)  # 1 ms bekleniyor; bir tuşa basılırsa döngü kontrol ediliyor.
    if key == ord('q'):  # Eğer 'q' tuşuna basılırsa döngü sonlandırılıyor.
        break
# Kamera ve pencereler temizleniyor.
cap.release()  # Kamera kaynağı serbest bırakılıyor.
cv.destroyAllWindows()  # Tüm OpenCV pencereleri kapatılıyor.
