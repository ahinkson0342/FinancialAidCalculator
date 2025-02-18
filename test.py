import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt6.QtGui import QIcon
from backend import calculate  # Import the function from backend.py


class FinancialAidCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Financial Aid Calculator")
        self.setGeometry(100, 100, 400, 350)  # Adjusted window height

        # Set window icon (ensure the file exists)
        icon_path = os.path.join("images", "GRC.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Create layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Financial Aid Calculator")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)

        # Input fields
        self.total_credits_label = QLabel("Total Program Credits:")
        self.total_credits_entry = QLineEdit()

        self.completed_credits_label = QLabel("Completed Credits:")
        self.completed_credits_entry = QLineEdit()

        self.target_gpa_label = QLabel("Target GPA:")
        self.target_gpa_entry = QLineEdit()

        self.current_gpa_label = QLabel("Current GPA:")
        self.current_gpa_entry = QLineEdit()

        layout.addWidget(self.total_credits_label)
        layout.addWidget(self.total_credits_entry)
        layout.addWidget(self.completed_credits_label)
        layout.addWidget(self.completed_credits_entry)
        layout.addWidget(self.target_gpa_label)
        layout.addWidget(self.target_gpa_entry)
        layout.addWidget(self.current_gpa_label)
        layout.addWidget(self.current_gpa_entry)

        # Calculate Button
        self.calculate_button = QPushButton("Calculate Required GPA")
        self.calculate_button.setStyleSheet(
            "background-color: #2C882B; color: white; font-size: 14px; padding: 8px;"
        )
        self.calculate_button.clicked.connect(self.calculate_required_gpa)
        layout.addWidget(self.calculate_button)

        # Set layout
        self.setLayout(layout)

    def calculate_required_gpa(self):
        try:
            # Get user inputs
            total_credits = float(self.total_credits_entry.text())
            completed_credits = float(self.completed_credits_entry.text())
            target_gpa = float(self.target_gpa_entry.text())
            current_gpa = float(self.current_gpa_entry.text())

            # Call backend function
            result = calculate(total_credits, completed_credits, target_gpa, current_gpa)

            # Show result in message box
            QMessageBox.information(self, "Required GPA", str(result))

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinancialAidCalculator()
    window.show()
    sys.exit(app.exec())
