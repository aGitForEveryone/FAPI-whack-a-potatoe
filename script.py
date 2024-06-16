from pathlib import Path

import pyautogui
import keyboard

running, isHolding = False, False
startStopKey = "f8"
confidence_level = 0.8
search_region_on_screen = (350, 280, 620, 570)
important_potato_eye = Path(__file__).parent / "img" / "eye.png"
normal_potato_eye = Path(__file__).parent / "img" / "eye_normal.png"


if __name__ == "__main__":
    print("Starting WhackaMoler@1.0.0")
    print(f"{startStopKey} - Start / Stop")
    print("-" * 20)
    print("🟩 Running" if running else "🛑 Stopped")

    while True:
        if keyboard.is_pressed(startStopKey):
            if not isHolding:
                isHolding = True
                print("\033[A                             \033[A")
                print("🛑 Stopped" if running else "🟩 Running")
                running = not running
        else:
            isHolding = False

        if running:
            image_found = False
            location = None
            try:
                location = pyautogui.locateOnScreen(
                    image=str(important_potato_eye),
                    confidence=confidence_level,
                    region=search_region_on_screen,
                )
                image_found = True
            except pyautogui.ImageNotFoundException:
                try:
                    if normal_potato_eye.exists():
                        location = pyautogui.locateOnScreen(
                            image=str(normal_potato_eye),
                            confidence=confidence_level,
                            region=search_region_on_screen,
                        )
                        image_found = True
                except pyautogui.ImageNotFoundException:
                    pass

            if image_found and location:
                pyautogui.click(location)
