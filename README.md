






<img width="1920" height="1080" alt="output_detected_image2" src="https://github.com/user-attachments/assets/8694ba0c-c366-420c-8d48-a3bf8621cf01" />




YOLOv4 Zararlı Bitki Tespit Sistemi
Bu proje, YOLOv4 derin öğrenme modeli kullanarak tarımsal alanlarda zararlı bitkilerin tespit edilmesini sağlar. Görseller, proje sahibi tarafından hazırlanmış ve etiketlenmiş veri setiyle eğitildi ve Python kodu ile test edildi.
-------------------------------------------------------------------------------------------------

Temel Özellikler

1.YOLOv4 Nesne Tespiti: Zararlı bitkileri yüksek doğrulukla tespit eder.

2.Kendi Veri Seti ile Eğitim: Proje sahibi tarafından hazırlanmış ve etiketlenmiş veri seti kullanılmıştır.

3.Python ile Test: Eğitim sonrası model, Python kodu ile doğrulanmıştır.

4.Gerçek Zamanlı veya Görüntü Tabanlı Algılama: Kamera veya önceden çekilmiş görüntüler üzerinde çalışabilir.

5.Görselleştirilmiş Sonuçlar: Tespit edilen bitkiler bounding box ve sınıf etiketi ile gösterilir.

Not:
-yolov4.cfg, obj.data ve obj.names dosyaları 6 sınıf için özelleştirilmiştir: "pink","black","orange","purple","white" ve "blue".

-Kendi özel nesneleriniz için bu dosyalar düzenlenebilir.

-zararlı_zararsız.py (kamera üzerinden) veya test_image.py (görsel üzerinden) ile zararlı ve zararsız sınıflar kişiselleştirilebilir. Etiketler ve tespit renkleri koda bağımlı olarak ayarlanmıştır.

-------------------------------------------------------------------------------------------------

Eğitim ve Ağırlıklar

Eğitim sonrası en verimli alınan ağırlıklar:
Google Drive Linki: https://drive.google.com/drive/folders/1fYnUDAAh40QuQE9-uHE-y2_eLYR1EVLo?usp=sharing

Test için, ağırlıkları indirip test_image.py veya zararlı_zararsız.py ile kullanabilirsiniz.

Not:
-Proje prototip amaçlıdır ve sınırlı veri ile test edilmiştir.

-Daha yüksek doğruluk ve kapsamlı kullanım için modelin daha büyük veri seti ile yeniden eğitilmesi önerilir.

-Model yalnızca eğitimde kullanılan bitki türlerini tespit edebilir; yeni türler için yeniden etiketleme ve eğitim gerekir.













