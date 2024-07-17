import tkinter as tk
from tkinter import messagebox

class FrameRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frame Recorder")
        self.root.geometry("600x300")
        self.root.configure(bg="#E58FE5")  # Màu nền tùy chỉnh

        # Tạo nhãn tiêu đề
        self.title_label = tk.Label(root, text="Frame Recorder", font=("Arial", 24), bg="#E58FE5")
        self.title_label.pack(pady=10)

        # Tạo khung nhập FPS
        self.fps_frame = tk.Frame(root, bg="#E58FE5")
        self.fps_frame.pack(pady=20)

        self.fps_label = tk.Label(self.fps_frame, text="create an", font=("Arial", 14), bg="#E58FE5")
        self.fps_label.pack(side=tk.LEFT)

        self.fps_entry = tk.Entry(self.fps_frame, font=("Arial", 14), width=5)
        self.fps_entry.pack(side=tk.LEFT, padx=5)

        self.fps_label2 = tk.Label(self.fps_frame, text="fps video", font=("Arial", 14), bg="#E58FE5")
        self.fps_label2.pack(side=tk.LEFT)

        # Tạo các nút
        self.button_frame = tk.Frame(root, bg="#E58FE5")
        self.button_frame.pack(pady=20)

        self.pause_button = tk.Button(self.button_frame, text="Pause", font=("Arial", 14), command=self.pause_recording)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(self.button_frame, text="Start", font=("Arial", 14), command=self.start_recording)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.end_button = tk.Button(self.button_frame, text="End", font=("Arial", 14), command=self.end_recording)
        self.end_button.pack(side=tk.LEFT, padx=10)

        # Tạo nhãn trạng thái
        self.status_label = tk.Label(root, text="Recording Paused", font=("Arial", 14), bg="#E58FE5")
        self.status_label.pack(pady=10)

    def pause_recording(self):
        self.status_label.config(text="Recording Paused")
        messagebox.showinfo("Info", "Recording Paused")

    def start_recording(self):
        self.status_label.config(text="Recording Started")
        messagebox.showinfo("Info", "Recording Started")

    def end_recording(self):
        self.status_label.config(text="Recording Ended")
        messagebox.showinfo("Info", "Recording Ended")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrameRecorderApp(root)
    root.mainloop()
