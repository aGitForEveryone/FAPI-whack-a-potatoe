import pyautogui

import script

pyautogui.screenshot(
    imageFilename="img/region_test.png", region=script.search_region_on_screen
)
