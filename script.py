import pyautogui
import keyboard

running, isHolding = False, False
startStopKey = "f8"

print("Starting WhackaMoler@1.0.0")
print(f"{startStopKey} - Start / Stop")
print("-" * 20)
print("🟩 Running" if running else "🛑 Stopped")

confidence_level = 0.8
search_region_on_screen = (350, 280, 620, 570)

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
                image="img/eye.png", confidence=confidence_level, region=search_region_on_screen
            )
            image_found = True
        except pyautogui.ImageNotFoundException:
            try:
                location = pyautogui.locateOnScreen(
                    image="img/eye_normal.png",
                    confidence=confidence_level,
                    region=search_region_on_screen,
                )
                image_found = True
            except pyautogui.ImageNotFoundException:
                pass

        if image_found and location:
            pyautogui.click(location)
