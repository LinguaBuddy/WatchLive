<div align="center">

<!-- Material 3 Expressive Header Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6750A4,50:7D5260,100:D0BCFF&height=220&section=header&text=WatchLive&fontSize=52&fontColor=FFFFFF&animation=twinkling" width="100%" alt="WatchLive M3 Banner" />
</p>

<!-- Animasyonlu Dynamic Typing -->
<img src="https://readme-typing-svg.herokuapp.com?font=Google+Sans&weight=600&size=28&pause=1000&color=D0BCFF&center=true&vCenter=true&width=600&height=70&lines=📺+WatchLive;Pure+Python+Live+TV;Material+3+Expressive+Design;No+VLC+|+No+Web+Server;Google+M3+Dynamic+Theming" alt="Typing SVG" />

<p align="center">
  <b>Harici oynatıcı ve sunucu bağımlılığı olmayan, saf Python ile geliştirilmiş Material 3 Expressive canlı TV deneyimi.</b>
</p>

<!-- Rozetler (Badges) -->
<p align="center">
  <img src="https://img.shields.io/badge/Version-v1.0.0-6750A4?style=for-the-badge&logo=github&logoColor=white" alt="Version" />
  <img src="https://img.shields.io/badge/Author-LinguaBuddy-7D5260?style=for-the-badge&logo=github&logoColor=white" alt="Author" />
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/UI-Material_3_Expressive-D0BCFF?style=for-the-badge&logo=materialdesign&logoColor=381E72" alt="UI" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Platform" />
</p>

<p align="center">
  <a href="#-hızlı-başlangıç">Hızlı Başlangıç</a> •
  <a href="#-özellikler">Özellikler</a> •
  <a href="#-dahili-kanallar">Kanallar</a> •
  <a href="#-geliştirici-kurulumu">Kaynak Kod</a>
</p>

</div>

---

<!-- 🎁 HIDDEN MATERIAL 3 EXPRESSIVE EASTER EGG -->
<details>
  <summary>🎨 <b>[EASTER EGG] Google Material 3 Expressive Dynamic Palette</b></summary>
  <br />
  <div align="center">
    <p><b>✨ Dynamic Color Tokens (MD3 System)</b></p>
    <pre>
 Primary     : #6750A4  [Primary Container : #EADDFF]
 Secondary   : #625B71  [Secondary Container : #E8DEF8]
 Tertiary    : #7D5260  [Tertiary Container  : #FFD8E4]
 Surface     : #1C1B1F  [On Surface         : #E6E1E5]
    </pre>
    <p><i>"Design is not just what it looks like and feels like. Design is how it works."</i> — Steve Jobs</p>
  </div>
</details>

<br />

## ⚡ Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| 🎨 **Material 3 Expressive** | Google'ın en yeni M3 Expressive tasarım dilini temel alan, dinamik renk tonlarına ve akıcı animasyon odaklı koyu temaya sahip CustomTkinter arayüzü. |
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
git clone [https://github.com/LinguaBuddy/WatchLive.git](https://github.com/LinguaBuddy/WatchLive.git)
cd WatchLive

# Gerekli kütüphaneleri yükleyin
pip install customtkinter av pillow requests

# Uygulamayı başlatın
python app.py
