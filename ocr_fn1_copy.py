import pytesseract
import pyautogui
import cv2
import numpy as np
import keyboard
import time
import pyperclip
import os

# ✅ Set the path to Tesseract executable (update if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_and_copy_text():
    try:
        # 📸 Take screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

        # 🎨 Convert to grayscale
        image = cv2.imread("screenshot.png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 🔍 OCR using Tesseract
        text = pytesseract.image_to_string(gray)

        # 📋 Copy to clipboard
        pyperclip.copy(text.strip())
        print("✅ Text copied to clipboard:\n")
        print(text.strip())
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 OCR Tool Running...\nPress F1 (Fn+1) to capture and copy text.\nPress ESC to quit.")

# 🌀 Loop and wait for hotkeys
while True:
    try:
        if keyboard.is_pressed("f1"):
            print("🕒 Processing screenshot...")
            capture_and_copy_text()
            time.sleep(1.5)  # Prevent rapid re-triggers
        elif keyboard.is_pressed("esc"):
            print("👋 Exiting.")
            break
    except KeyboardInterrupt:
        break
