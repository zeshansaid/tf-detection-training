import sys
import os
import tensorflow as tf
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from helper_functions import run_odt_and_draw_results
import config

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input_image_label = QLabel()
        self.input_image_label.setMaximumSize(720, 300)  # Adjust maximum size of input image label
        self.layout.addWidget(self.input_image_label)

        self.output_image_label = QLabel()
        self.output_image_label.setMaximumSize(720, 300)  # Adjust maximum size of output image label
        self.output_image_label.setStyleSheet("background-color: lightgreen; color: black; font-size: 14px; padding: 10px;")
     
        self.layout.addWidget(self.output_image_label)

        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)
        self.layout.addWidget(self.open_button)

    def open_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setDirectory('.')
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            input_image_pixmap = QPixmap(file_path)
            self.input_image_label.setPixmap(input_image_pixmap)
            self.input_image_label.setScaledContents(True)

            # Process the image
            output_image_path = self.process_image(file_path)
            output_image_pixmap = QPixmap(output_image_path)
            self.output_image_label.setPixmap(output_image_pixmap)
            self.output_image_label.setScaledContents(True)

    def process_image(self, input_image_path):
        cwd = os.getcwd()
        MODEL_PATH = config.MODEL_PATH
        MODEL_NAME = config.MODEL_NAME
        DETECTION_THRESHOLD = 0.4

        # Create result directory if it does not exist
        result_dir = os.path.join(cwd, 'result')
        os.makedirs(result_dir, exist_ok=True)

        # Open and resize the input image
        im = Image.open(input_image_path)
        im.thumbnail((512, 512), Image.LANCZOS)  # Use Image.LANCZOS for high-quality downsampling
        input_image_path = os.path.join(result_dir, 'input.png')
        im.save(input_image_path, 'PNG')

        # Load the TFLite model
        model_path = os.path.join(MODEL_PATH, MODEL_NAME)
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()

        # Run inference and draw detection result on the resized image
        detection_result_image = run_odt_and_draw_results(
            input_image_path,
            interpreter,
            threshold=DETECTION_THRESHOLD
        )

        # Save the detection result
        output_image_path = os.path.join(result_dir, 'output.png')
        img = Image.fromarray(detection_result_image)
        img.save(output_image_path)

        return output_image_path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
