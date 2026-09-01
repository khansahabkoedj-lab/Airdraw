import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pydub import AudioSegment
import os
import threading

class SoundBoosterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sound Booster for Windows")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.filepath = None

        # UI Elements
        self.lbl_title = tk.Label(root, text="Audio File Volume Booster", font=("Helvetica", 14, "bold"))
        self.lbl_title.pack(pady=10)

        self.btn_select = tk.Button(root, text="Select Audio File", command=self.select_file)
        self.btn_select.pack(pady=5)

        self.lbl_file = tk.Label(root, text="No file selected", fg="gray")
        self.lbl_file.pack(pady=5)

        self.frame_boost = tk.Frame(root)
        self.frame_boost.pack(pady=10)

        self.lbl_boost = tk.Label(self.frame_boost, text="Boost (dB):")
        self.lbl_boost.pack(side=tk.LEFT, padx=5)

        self.boost_var = tk.DoubleVar(value=5.0)
        self.spin_boost = tk.Spinbox(self.frame_boost, from_=-20.0, to=50.0, increment=1.0, textvariable=self.boost_var, width=5)
        self.spin_boost.pack(side=tk.LEFT, padx=5)

        self.btn_boost = tk.Button(root, text="Boost and Save", command=self.process_audio, state=tk.DISABLED, bg="green", fg="white")
        self.btn_boost.pack(pady=10)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")

    def select_file(self):
        filetypes = (
            ("Audio files", "*.mp3 *.wav *.ogg *.flac"),
            ("All files", "*.*")
        )
        filepath = filedialog.askopenfilename(title="Open Audio File", initialdir="/", filetypes=filetypes)
        if filepath:
            self.filepath = filepath
            filename = os.path.basename(filepath)
            self.lbl_file.config(text=filename, fg="black")
            self.btn_boost.config(state=tk.NORMAL)

    def process_audio(self):
        if not self.filepath:
            return

        db_boost = self.boost_var.get()
        save_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")],
            title="Save Boosted File As"
        )

        if not save_path:
            return

        self.btn_boost.config(state=tk.DISABLED)
        self.progress.pack(pady=5)
        self.progress.start()

        # Run audio processing in a separate thread so GUI doesn't freeze
        threading.Thread(target=self._boost_audio_task, args=(self.filepath, save_path, db_boost), daemon=True).start()

    def _boost_audio_task(self, input_path, output_path, db_boost):
        try:
            # Load audio file
            ext = os.path.splitext(input_path)[1].lower().replace('.', '')
            audio = AudioSegment.from_file(input_path, format=ext if ext else None)

            # Boost volume
            boosted_audio = audio + db_boost

            # Export audio file
            out_ext = os.path.splitext(output_path)[1].lower().replace('.', '')
            boosted_audio.export(output_path, format=out_ext)

            self.root.after(0, self._on_success, output_path)

        except Exception as e:
            self.root.after(0, self._on_error, str(e))

    def _on_success(self, output_path):
        self.progress.stop()
        self.progress.pack_forget()
        self.btn_boost.config(state=tk.NORMAL)
        messagebox.showinfo("Success", f"Successfully saved boosted audio to:\n{output_path}")

    def _on_error(self, error_msg):
        self.progress.stop()
        self.progress.pack_forget()
        self.btn_boost.config(state=tk.NORMAL)
        messagebox.showerror("Error", f"Failed to process audio:\n{error_msg}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SoundBoosterApp(root)
    root.mainloop()
