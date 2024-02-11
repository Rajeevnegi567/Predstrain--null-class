import cv2
import imutils
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Human_Detection import Detector


class HumanDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Human Detection App")

        self.load_button = tk.Button(
            root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=700, height=500)
        self.canvas.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            img = cv2.imread(file_path)
            img = imutils.resize(img, width=700)
            img = Detector(img)

            if img is not None:
                self.display_image(img)
            else:
                messagebox.showerror(
                    "Error", "No humans detected in the image!")

    def display_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_tk = imutils.opencv2tkinter(img_rgb)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk


def main():
    root = tk.Tk()
    app = HumanDetectionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
