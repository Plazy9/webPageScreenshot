import time
from selenium import webdriver
from PIL import Image
from io import BytesIO
from decouple import config

url = config("URL")
output_path = "./images/screenshot.png"

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

try:
    while True:


        screenshot = driver.get_screenshot_as_png()
        image = Image.open(BytesIO(screenshot))
        cropped_image = image.crop((x, y, x + width, y + height))
        cropped_image.save(output_path)

        print(f"Képernyőkép készült: {output_path}")
        # Időzítés (2 perc = 120 másodperc)
        time.sleep(120)

except KeyboardInterrupt:
    print("Program leállítva")

finally:
    driver.quit()
