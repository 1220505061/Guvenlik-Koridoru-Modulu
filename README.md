# Otonom Araç Navigasyon Sistemi: Güvenlik Koridoru Modülü 🚗🛡️

Bu proje, otonom araçların navigasyon süreçlerinde karşılaştığı engelleri sadece aşmasını değil, bu engellerden **maksimum güvenlik mesafesinde (maximum margin)** geçmesini sağlayan matematiksel bir modelleme çalışmasıdır.

**Geliştirici:** Fatih Çiçek
**Kurum:** Kırklareli Üniversitesi, Yazılım Mühendisliği

## 🎯 Projenin Amacı
İki boyutlu bir düzlemde tespit edilen iki farklı engel sınıfı (A ve B) arasından geçecek en güvenli rotayı bulmak. Klasik bir ayırıcı çizgi yerine, **Support Vector Machines (SVM)** algoritması kullanılarak engellere en uzak olan "Optimum Güvenlik Koridoru" hesaplanmıştır.

## ⚙️ Teknik Mimari ve Özellikler
Proje tamamen **Nesne Yönelimli Programlama (OOP)** prensiplerine uygun olarak 3 ana sınıfta tasarlanmıştır:
1. `ObstacleGenerator`: Doğrusal ayrılabilen rastgele engel koordinatları (test verisi) üretir.
2. `SafetyCorridorModel`: `scikit-learn` (Linear SVM) kullanarak karar sınırını ve maksimum marjini hesaplar.
3. `Visualizer`: Engelleri, destek vektörlerini ve güvenlik koridorunu `matplotlib` ile çizer.

## 📊 Görsel Çıktı ve Destek Vektörleri
*(Buraya o meşhur yeşil çizgili grafiği ekleyeceğiz)*
**[GRAFİK BURAYA GELECEK]**

* **Kalın Yeşil Çizgi:** Aracın izlemesi gereken optimum (en güvenli) rota.
* **Kesikli Çizgiler:** Güvenlik koridorunun sınırları (Margin).
* **Siyah Halkalı Noktalar:** Destek Vektörleri. Rotanın sınırlarını belirleyen en kritik engeller.

## ⏱️ Zaman Karmaşıklığı (Big-O)
* **Model Eğitimi (Hesaplama):** ~ $O(n^2)$ (LibSVM optimizasyonu)
* **Anlık Rota Tahmini:** $O(k)$ (Özellik sayısına bağlı hızlı tepki)

## 🚀 Nasıl Çalıştırılır?
Gerekli kütüphaneleri kurmak için:
```bash
pip install numpy matplotlib scikit-learn
