from io import BytesIO
import threading
import time
import av
import customtkinter as ctk
from PIL import Image

# Material You (MD3) Dark Renk Paleti
MD3_PALETTE = {
    "bg": "#141218",
    "surface_variant": "#2B2930",
    "primary": "#D0BCFF",
    "on_primary": "#381E72",
    "secondary_container": "#4A4458",
    "text_main": "#E6E0E9",
    "text_sub": "#CAC4D0",
    "danger": "#F2B8B5",
    "on_danger": "#601410",
}

ctk.set_appearance_mode("Dark")


class PurePythonTV(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Material You - Canlı TV")
    self.geometry("1000x650")
    self.configure(fg_color=MD3_PALETTE["bg"])

    self.is_playing = False
    self.play_thread = None

    # Canlı TV Kanalları Listesi
    self.channels = [
        {
            "name": "TRT 1",
            "category": "Genel",
            "url": "https://tv-trt1.medya.trt.com.tr/master.m3u8",
        },
        {
            "name": "TRT Haber",
            "category": "Haber",
            "url": "https://tv-trthaber.medya.trt.com.tr/master.m3u8",
        },
        {
            "name": "TRT Spor",
            "category": "Spor",
            "url": "https://tv-trtspor1.medya.trt.com.tr/master.m3u8",
        },
        {
            "name": "TRT Belgesel",
            "category": "Belgesel",
            "url": "https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8",
        },
        {
            "name": "NTV",
            "category": "Haber",
            "url": "https://ntv.daioncdn.net/ntv/ntv.m3u8",
        },
        {
            "name": "Star TV",
            "category": "Genel",
            "url": "https://startv.daioncdn.net/startv/startv.m3u8",
        },
    ]

    self.setup_ui()

  def setup_ui(self):
    # Sol Panel (Kanal Listesi)
    self.sidebar = ctk.CTkFrame(
        self,
        width=280,
        fg_color=MD3_PALETTE["surface_variant"],
        corner_radius=24,
    )
    self.sidebar.pack(side="left", fill="y", padx=15, pady=15)
    self.sidebar.pack_propagate(False)

    sidebar_title = ctk.CTkLabel(
        self.sidebar,
        text="Canlı Kanallar",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=MD3_PALETTE["text_main"],
    )
    sidebar_title.pack(padx=20, pady=(20, 15), anchor="w")

    self.channel_scroll = ctk.CTkScrollableFrame(
        self.sidebar, fg_color="transparent"
    )
    self.channel_scroll.pack(fill="both", expand=True, padx=5, pady=5)

    for ch in self.channels:
      btn = ctk.CTkButton(
          self.channel_scroll,
          text=f"  {ch['name']}  ({ch['category']})",
          font=ctk.CTkFont(size=14),
          anchor="w",
          fg_color="transparent",
          text_color=MD3_PALETTE["text_main"],
          hover_color=MD3_PALETTE["secondary_container"],
          corner_radius=16,
          height=42,
          command=lambda channel=ch: self.play_channel(channel),
      )
      btn.pack(fill="x", pady=4)

    # Sağ Panel (Video Display Area)
    self.main_content = ctk.CTkFrame(self, fg_color="transparent")
    self.main_content.pack(
        side="right", fill="both", expand=True, padx=(0, 15), pady=15
    )

    self.player_card = ctk.CTkFrame(
        self.main_content,
        fg_color=MD3_PALETTE["surface_variant"],
        corner_radius=28,
    )
    self.player_card.pack(fill="both", expand=True)

    # Üst Bar
    self.top_bar = ctk.CTkFrame(self.player_card, fg_color="transparent")
    self.top_bar.pack(fill="x", padx=20, pady=15)

    self.channel_title = ctk.CTkLabel(
        self.top_bar,
        text="Bir Kanal Seçin",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=MD3_PALETTE["text_main"],
    )
    self.channel_title.pack(side="left")

    self.stop_btn = ctk.CTkButton(
        self.top_bar,
        text="Durdur",
        font=ctk.CTkFont(size=13, weight="bold"),
        fg_color=MD3_PALETTE["danger"],
        text_color=MD3_PALETTE["on_danger"],
        hover_color="#F28B82",
        corner_radius=16,
        width=80,
        height=32,
        command=self.stop_channel,
    )
    self.stop_btn.pack(side="right")

    # Video Ekran Alanı
    self.video_container = ctk.CTkFrame(
        self.player_card, fg_color="#000000", corner_radius=16
    )
    self.video_container.pack(
        fill="both", expand=True, padx=20, pady=(0, 20)
    )

    # Video Karelerinin Basılacağı Etiket
    self.video_display = ctk.CTkLabel(
        self.video_container, text="", fg_color="#000000"
    )
    self.video_display.pack(fill="both", expand=True)

    # Yükleniyor Mesajı
    self.loading_label = ctk.CTkLabel(
        self.video_container,
        text="Bir kanal seçin",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=MD3_PALETTE["primary"],
    )
    self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

  def play_channel(self, channel):
    self.stop_channel()
    time.sleep(0.1)

    self.is_playing = True
    self.channel_title.configure(
        text=f"{channel['name']} ({channel['category']})"
    )

    self.loading_label.configure(text="İstasyona Bağlanılıyor...")
    self.loading_label.lift()

    # Arka planda yayını çözen thread
    self.play_thread = threading.Thread(
        target=self._stream_worker, args=(channel["url"],), daemon=True
    )
    self.play_thread.start()

  def _stream_worker(self, url):
    try:
      # PyAV ile M3U8 Akışını Açma (Ağ önbelleği ayarlı)
      container = av.open(
          url,
          options={
              "buffer_size": "1024000",
              "rtsp_transport": "tcp",
              "stimeout": "5000000",
          },
      )
      video_stream = container.streams.video[0]

      first_frame = True

      for frame in container.decode(video_stream):
        if not self.is_playing:
          break

        # Kareyi PIL Image nesnesine dönüştür
        img = frame.to_image()

        # Ekran boyutuna göre görüntüyü ölçekle
        target_w = max(self.video_container.winfo_width(), 640)
        target_h = max(self.video_container.winfo_height(), 360)
        img = img.resize((target_w, target_h), Image.Resampling.BILINEAR)

        ctk_img = ctk.CTkImage(
            light_image=img, dark_image=img, size=(target_w, target_h)
        )

        # İlk kare geldiğinde "İstasyona Bağlanılıyor" yazısını kaldır
        if first_frame:
          self.loading_label.lower()
          first_frame = False

        # Ana thread üzerinde UI güncellemesi yap
        self.after(0, self._update_video_frame, ctk_img)

    except Exception as e:
      self.after(
          0,
          lambda: self.loading_label.configure(
              text="Bağlantı Hatası veya Yayın Kapalı"
          ),
      )

  def _update_video_frame(self, ctk_img):
    if self.is_playing:
      self.video_display.configure(image=ctk_img)

  def stop_channel(self):
    self.is_playing = False
    self.video_display.configure(image="")
    self.loading_label.configure(text="Yayın Durduruldu")
    self.loading_label.lift()
    self.channel_title.configure(text="Bir Kanal Seçin")


if __name__ == "__main__":
  app = PurePythonTV()
  app.mainloop()