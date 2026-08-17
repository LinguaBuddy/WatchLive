import av
import customtkinter as ctk
from PIL import Image

class StreamWorker:
    def __init__(self, app_instance):
        self.app = app_instance

    def decode_stream(self, url):
        try:
            # PyAV ile M3U8 Akışını Açma
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
                if not self.app.is_playing:
                    break

                # Kareyi PIL Image nesnesine dönüştür
                img = frame.to_image()

                # Ekran boyutuna göre görüntüyü ölçekle
                target_w = max(self.app.video_container.winfo_width(), 640)
                target_h = max(self.app.video_container.winfo_height(), 360)
                img = img.resize((target_w, target_h), Image.Resampling.BILINEAR)

                ctk_img = ctk.CTkImage(
                    light_image=img, dark_image=img, size=(target_w, target_h)
                )

                if first_frame:
                    self.app.after(0, self.app.loading_label.lower)
                    first_frame = False

                # Ana thread üzerinde UI güncellemesi yap
                self.app.after(0, self.app._update_video_frame, ctk_img)

        except Exception as e:
            self.app.after(
                0,
                lambda: self.app.loading_label.configure(
                    text="Bağlantı Hatası veya Yayın Kapalı"
                ),
            )
