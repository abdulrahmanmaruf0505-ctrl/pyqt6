import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My First PyQt6 App")
window.resize(400, 220)

layout = QVBoxLayout()
layout.setSpacing(8)
layout.setContentsMargins(20, 15, 20, 15)

username_label = QLabel("Username")
username_input = QLineEdit()

password_label = QLabel("Password")
password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.EchoMode.Password)
forget_label = QLabel("<a href='#'>Forget Password?</a>")

login_btn = QPushButton("Login")
signup_btn = QPushButton("Sign Up")

# Buttons side by side
button_layout = QHBoxLayout()
button_layout.setSpacing(10)
button_layout.addWidget(login_btn)
button_layout.addWidget(signup_btn)

# eye password button
eyeButton = QPushButton("👁")
eyeButton.setFixedWidth(40)

eyeButton.pressed.connect(lambda: password_input.setEchoMode(QLineEdit.EchoMode.Normal))

eyeButton.released.connect(
    lambda: password_input.setEchoMode(QLineEdit.EchoMode.Password)
)

password_layout = QHBoxLayout()
password_layout.setSpacing(5)

password_layout.addWidget(password_input)
password_layout.addWidget(eyeButton)


# show massage
def login():
    username = username_input.text().strip()
    password = password_input.text()
    if not username or not password:
        QMessageBox.warning(
            window, "Input Error", "Please enter both username and password."
        )
    else:
        QMessageBox.information(window, "Login Successful", "Welcome, dear!")


login_btn.clicked.connect(login)


# Style the buttons
login_btn.setStyleSheet(
    "color: white; background-color: #007BFF; border-radius: 5px; padding: 5px 10px; font-weight: bold; font-size: 14px;"
)
signup_btn.setStyleSheet(
    "color: white; background-color: #28A745; border-radius: 5px; padding: 5px 10px; font-weight: bold; font-size: 14px;"
)
username_input.setStyleSheet(
    "border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;"
)
password_input.setStyleSheet(
    "border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14px;"
)
username_label.setStyleSheet("font-size: 14px; font-weight: bold;")
password_label.setStyleSheet("font-size: 14px; font-weight: bold;")

layout.addWidget(username_label)
layout.addWidget(username_input)
layout.addWidget(password_label)
layout.addLayout(password_layout)
layout.addWidget(forget_label)
layout.addLayout(button_layout)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
