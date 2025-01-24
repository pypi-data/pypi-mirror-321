from qtpy import QtWidgets, QtGui, QtCore
import cv2
from datetime import datetime
from labelme import utils
from pathlib import Path
import numpy as np


class RecordingWidget(QtWidgets.QWidget):
    def __init__(self, canvas, fps=30, parent=None):
        super().__init__(parent)
        self.canvas = canvas
        self.fps = fps
        self.is_recording = False
        self.video_writer = None
        self.output_filename = None
        self.capture_timer = None
        self.here = Path(__file__).resolve().parent.parent
        self.record_icon = QtGui.QIcon(str(self.here / "icons/record.png"))
        self.stop_record_icon = QtGui.QIcon(
            str(self.here / "icons/stop_record.png"))

        # Add a record button to the toolbar
        self.record_action = QtWidgets.QAction(
            self.record_icon, "Record", self)
        self.record_action.setCheckable(True)
        self.record_action.toggled.connect(self.toggle_record)

    def toggle_record(self, checked):
        if checked:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        # Prompt the user to select a folder
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Folder")
        if not folder:
            QtWidgets.QMessageBox.warning(
                self, "No Folder Selected", "Please select a folder to save the recording.")
            self.record_action.setChecked(False)
            return

        self.is_recording = True
        self.record_action.setIcon(self.stop_record_icon)
        self.record_action.setText("Stop Recording")

        # Get the canvas pixmap dimensions
        pixmap = self.canvas.grab()
        width = pixmap.width()
        height = pixmap.height()
        fps = self.fps if self.fps is not None else 30  # Default to 30 if not available

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for .mp4
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Store the filename with selected folder
        self.output_filename = f"{folder}/canvas_recording_{timestamp}.mp4"
        self.video_writer = cv2.VideoWriter(
            self.output_filename, fourcc, fps, (width, height))

        if not self.video_writer.isOpened():
            QtWidgets.QMessageBox.critical(
                self, "Error", f"Could not open video writer for {self.output_filename}")
            self.is_recording = False
            self.record_action.setChecked(False)
            self.record_action.setIcon(self.record_icon)
            self.record_action.setText("Record")
            self.video_writer = None
            return

        # Start a timer to capture frames
        self.capture_timer = QtCore.QTimer(self)
        self.capture_timer.timeout.connect(self.capture_frame)
        self.capture_timer.start(int(1000 / fps))  # Interval in milliseconds

    def capture_frame(self):
        """Capture the current frame from the canvas."""
        if self.is_recording:
            # Get the current pixmap from the canvas
            pixmap = self.canvas.grab()
            qimage = pixmap.toImage()

            # Convert QImage to numpy array
            frame = utils.img_qt_to_arr(qimage)
            frame_bgr = frame[:, :, :3]
            # Write the frame to the video writer
            self.video_writer.write(frame_bgr)

    def stop_recording(self):
        self.is_recording = False
        self.record_action.setIcon(self.stop_record_icon)
        self.record_action.setText("Record")

        if self.capture_timer and self.capture_timer.isActive():
            self.capture_timer.stop()
            self.capture_timer.deleteLater()
            self.capture_timer = None

        if self.video_writer and self.video_writer.isOpened():
            self.video_writer.release()
            self.video_writer = None

        # Display message with the saved filename
        QtWidgets.QMessageBox.information(
            self, "Recording Saved", f"Canvas recording saved to {self.output_filename}")
