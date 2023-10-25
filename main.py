import time
from datetime import datetime
from selenium import webdriver
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from decouple import config
import os

url = config("URL")
output_path = "./images/"
filename =  "screenshot.png"
timeBetweenSreenshots = 10

x = 400
y = 100
width = 1920-x-400
height = 1080-y-200

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--window-size=1920,1080")
options.add_argument("--enable-precise-memory-info")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-default-apps")
options.add_argument("--disable-cookies")
options.add_argument("test-type=browser")

driver = webdriver.Chrome(options=options)
driver.get(url)

if not os.path.exists(output_path):
    # Ha nem létezik, hozzuk létre
    os.makedirs(output_path)
    print(f"A '{output_path}' könyvtár létrehozva.")
else:
    print(f"A '{output_path}' könyvtár már létezik.")


try:
    while True:
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(BytesIO(screenshot))
        cropped_image = image.crop((x, y, x + width, y + height))

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        font = ImageFont.truetype("arial.ttf", 36)  # Betűtípus és méret kiválasztása

        draw = ImageDraw.Draw(cropped_image)
        #text_width, text_height = draw.textsize(timestamp, font)
        text_x = 20  # X pozíció
        text_y = 20  # Y pozíció
        text_color = (0, 0, 0)  # Szövegszín (fehér)
        draw.text((text_x, text_y), timestamp, fill=text_color, font=font)

        cropped_image.save(output_path + filename)
        print(f"Képernyőkép készült: {output_path}{filename} {timestamp}")
        time.sleep(timeBetweenSreenshots)

except KeyboardInterrupt:
    print("Program leállítva")

finally:
    driver.quit()
