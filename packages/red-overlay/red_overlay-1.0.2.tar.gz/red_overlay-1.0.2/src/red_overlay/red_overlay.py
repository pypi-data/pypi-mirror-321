from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class REDOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Set window flags: topmost, borderless, and click-through
        self.setWindowFlags(
            Qt.FramelessWindowHint |  # Remove borders
            Qt.WindowStaysOnTopHint |  # Always on top
            Qt.Tool |  # Hide from taskbar
            Qt.WindowTransparentForInput  # Ignore mouse clicks
        )

        # Set window background to fully transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Add a label with text
        self.label = QLabel("RED Overlay", self)
        self.label.setStyleSheet("font-size: 24px; color: white; background: transparent;")
        self.label.setAlignment(Qt.AlignCenter)

        # Set the initial text and adjust window size/position
        self.set_text("RED Overlay")

        # Add a shadow effect to the text (optional)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(2, 2)
        self.label.setGraphicsEffect(shadow)

    def set_text(self, text):
        """Update the text displayed in the window."""
        self.label.setText(text)
        self.label.adjustSize()  # Resize the label to fit the new text
        self.resize(self.label.size())  # Resize the window to fit the label
        self.move_to_top_center()  # Re-center the window

    def move_to_top_center(self):
        """Position the window at the top center of the screen."""
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = 0  # Top of the screen
        self.move(x, y)


class REDOverlayCommunicate(QObject):
    update_text_signal = pyqtSignal(str)  # Signal to update the text in the GUI

# Example usage:
# # if __name__ == "__main__":
#     # Create the application
#     app = QApplication(sys.argv)
#
#     # Create and show the window
#     overlay = REDOverlay()
#     overlay.show()
#
#     # Create a communication object for signals
#     comm = REDOverlayCommunicate()
#
#     # Connect the signal to the window's set_text method
#     comm.update_text_signal.connect(overlay.set_text)
#
#     def monitor_process():
#         while something:
#             try:
#                 # do something
#             except Exception as e:
#                 handle_error(e)
#                 QApplication.quit()
#                 break
#         QApplication.quit()
#
#     monitor_thread = threading.Thread(target=monitor_process)
#     monitor_thread.daemon = True
#     monitor_thread.start()
#
#     # Run the event loop
#     sys.exit(app.exec_())