import os
from qtpy.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QProgressBar
)
from qtpy.QtCore import Qt, QThread, Signal
from annolid.annotation.labelme2yolo import Labelme2YOLO


class YOLOConverterWorker(QThread):
    finished = Signal()
    progress = Signal(int)
    message = Signal(str)
    error = Signal(str)

    def __init__(self, json_dir, val_size, test_size):
        super().__init__()
        self.json_dir = json_dir
        self.val_size = val_size
        self.test_size = test_size

    def run(self):
        try:
            self.progress.emit(10)
            self.message.emit("Starting conversion...")
            converter = Labelme2YOLO(self.json_dir)
            converter.convert(val_size=self.val_size, test_size=self.test_size)
            self.progress.emit(100)
            self.message.emit("Conversion successful!")
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))
            self.finished.emit()  # Emit finished even on error


class YOLOConverterWidget(QDialog):
    def __init__(self, parent=None):
        super(YOLOConverterWidget, self).__init__(parent)

        # Layout
        self.setWindowTitle("LabelMe to YOLO Converter")
        self.layout = QVBoxLayout()

        # Widgets for folder selection
        self.json_dir_label = QLabel("Select JSON Directory:")
        self.json_dir_input = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.select_json_directory)

        self.layout.addWidget(self.json_dir_label)
        self.layout.addWidget(self.json_dir_input)
        self.layout.addWidget(self.browse_button)

        # Validation and test size inputs
        self.val_size_label = QLabel("Validation Size (0.0 to 1.0):")
        self.val_size_input = QLineEdit("0.1")  # Default value is 10%
        self.test_size_label = QLabel("Test Size (0.0 to 1.0):")
        self.test_size_input = QLineEdit("0.1")  # Default value is 10%

        self.layout.addWidget(self.val_size_label)
        self.layout.addWidget(self.val_size_input)
        self.layout.addWidget(self.test_size_label)
        self.layout.addWidget(self.test_size_input)

        # Convert button
        self.convert_button = QPushButton("Convert to YOLO Format")
        self.convert_button.clicked.connect(self.run_conversion)
        self.layout.addWidget(self.convert_button)

        # Progress bar and message label
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

        self.message_label = QLabel("")
        self.layout.addWidget(self.message_label)

        self.setLayout(self.layout)

    def select_json_directory(self):
        """
        Opens a file dialog to select the directory containing JSON files.
        """
        json_dir = QFileDialog.getExistingDirectory(
            self, "Select JSON Directory")
        if json_dir:
            self.json_dir_input.setText(json_dir)

    def run_conversion(self):
        """
        Runs the LabelMe to YOLO conversion script.
        """
        json_dir = self.json_dir_input.text().strip()
        val_size = self.val_size_input.text().strip()
        test_size = self.test_size_input.text().strip()

        if not os.path.isdir(json_dir):
            QMessageBox.warning(
                self, "Error", "Please select a valid JSON directory.")
            return

        try:
            val_size = float(val_size)
            test_size = float(test_size)
            if not (0 <= val_size <= 1) or not (0 <= test_size <= 1):
                raise ValueError(
                    "Validation and test sizes must be between 0.0 and 1.0.")
        except ValueError:
            QMessageBox.warning(
                self, "Error", "Please enter valid numbers for validation and test sizes.")
            return

        self.convert_button.setEnabled(False)  # Disable the button

        self.worker = YOLOConverterWorker(json_dir, val_size, test_size)
        self.worker.finished.connect(self.on_conversion_finished)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.message.connect(self.message_label.setText)
        self.worker.error.connect(self.on_conversion_error)
        self.worker.start()

    def on_conversion_finished(self):
        self.convert_button.setEnabled(True)  # Re-enable the button
        QMessageBox.information(
            self, "Success", "YOLO dataset created successfully.")
        self.close()  # Close the dialog

    def on_conversion_error(self, error_message):
        self.convert_button.setEnabled(True)  # Re-enable the button
        self.progress_bar.setValue(0)
        self.message_label.setText(f"Error: {error_message}")
        QMessageBox.critical(
            self, "Error", f"An error occurred: {error_message}")
