import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Human_Detection import Detector


class HumanDetectionVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Human Detection Video App")

        self.load_button = tk.Button(
            root, text="Load Video", command=self.load_video)
        self.load_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.cap = None

    def load_video(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            if self.cap is not None:
                self.cap.release()

            self.cap = cv2.VideoCapture(file_path)

            if not self.cap.isOpened():
                messagebox.showerror("Error", "Failed to open video file.")
                self.cap = None
                return

            self.process_video()

    def process_video(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = Detector(frame)

            if frame is not None:
                self.display_frame(frame)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

    def display_frame(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_tk = self.opencv2tkinter(img_rgb)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk

    def opencv2tkinter(self, img):
        import PIL.Image
        import PIL.ImageTk

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)
        img_tk = PIL.ImageTk.PhotoImage(image=img)
        return img_tk


def main():
    root = tk.Tk()
    app = HumanDetectionVideoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
