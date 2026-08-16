<div align="center">

<!-- Animasyonlu Banner / Başlık -->
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=32&pause=1000&color=38BDF8&center=true&vCenter=true&width=500&height=70&lines=📺+WatchLive;Pure+Python+Live+TV;Material+You+(MD3)+UI;No+VLC+|+No+Web+Server" alt="Typing SVG" />

<p align="center">
  <b>Harici oynatıcı ve sunucu bağımlılığı olmayan, saf Python ile geliştirilmiş modern canlı TV deneyimi.</b>
</p>

<!-- Rozetler (Badges) -->
<p align="center">
  <img src="https://img.shields.io/badge/Version-v1.0.0-38BDF8?style=for-the-badge&logo=github" alt="Version" />
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/UI-CustomTkinter-FF6F61?style=for-the-badge" alt="UI" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows" alt="Platform" />
</p>

<p align="center">
  <a href="#-hızlı-başlangıç">Hızlı Başlangıç</a> •
  <a href="#-özellikler">Özellikler</a> •
  <a href="#-dahili-kanallar">Kanallar</a> •
  <a href="#-geliştirici-kurulumu">Kaynak Kod</a>
</p>

---

</div>

## ⚡ Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| 🎨 **Material You (MD3)** | Modern, koyu tema odaklı ve dinamik CustomTkinter arayüzü. |
| 🚀 **Saf Python Motoru** | `PyAV` (FFmpeg) altyapısı sayesinde M3U8 akışlarını doğrudan arayüzde işler. |
| 🔒 **Sıfır Sunucu Bağımlılığı** | Arka planda HTTP/Web sunucusu çalıştırmaz, tamamen yerel çalışır. |
| 🛰️ **Akıllı Yükleme Katmanı** | Kanal geçişlerindeki donma ve siyah ekranı önleyen akıcı arayüz geri bildirimi. |
| 📦 **Taşınabilir (.exe)** | VLC Player veya Python kurulumu gerektirmeyen tek parça çalıştırılabilir dosya. |

---

## 📺 Dahili Kanallar

<div align="center">

`TRT 1` • `TRT Haber` • `TRT Spor` • `TRT Belgesel` • `NTV` • `Star TV`

</div>

---

## 🚀 Hızlı Başlangıç

1. GitHub ekranının sağ tarafındaki **[Releases](../../releases)** bölümüne gidin.
2. `WatchLive.exe` dosyasını indirin.
3. Çift tıklayarak doğrudan çalıştırın!

---

## 🛠️ Geliştirici Kurulumu

<details>
<summary><b>Projeyi bilgisayarınızda çalıştırmak için tıklayın</b></summary>

<br />

```bash
# Depoyu klonlayın
git clone [https://github.com/KullaniciAdin/WatchLive.git](https://github.com/KullaniciAdin/WatchLive.git)
cd WatchLive

# Gerekli kütüphaneleri yükleyin
pip install customtkinter av pillow requests

# Uygulamayı başlatın
python app.py
