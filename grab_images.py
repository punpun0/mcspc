from selenium import webdriver
import os


def grabImages():
    driver = webdriver.Firefox(executable_path=r".\geckodriver.exe")
    html = os.path.dirname(os.path.abspath(__file__)) + r"\offscreen_render.html"
    driver.get(html)

    images = driver.find_elements_by_tag_name("img")
    modelImages = []
    for image in images:
        modelImages.append(image.get_attribute("src"))

    driver.quit()

    return modelImages
