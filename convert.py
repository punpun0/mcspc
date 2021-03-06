import json
import os
import binascii
from datetime import datetime, timedelta
from create_page import createPage
from grab_images import grabImages

if __name__ == "__main__":
    try:
        with open("./input/skins.json", "r", encoding="utf-8") as f:
            skins_data = json.loads(f.read())
    except FileNotFoundError:
        print("'skins.json' not found. Did you place your skin pack without its folder?")
        input()
        exit
        
    data = {}
    images = []
    counter = 1
    timestamp = datetime.today()
    for s in skins_data["skins"]:
        timestamp -= timedelta(seconds=1)
        name = "skin_{}".format(counter)
        data[name] = {}
        data[name]["created"] = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        data[name]["id"] = name
        with open("./input/{}".format(s["texture"]), "rb") as img:
            ib64 = str(binascii.b2a_base64(img.read(), newline=False).decode("utf-8"))
        images.append("data:image/png;base64," + ib64)
        data[name]["modelImage"] = "data:image/png;base64,{}".format(ib64)
        data[name]["name"] = s["localization_name"]
        data[name]["skinImage"] = "data:image/png;base64,{}".format(ib64)
        if s["geometry"] == "geometry.humanoid.customSlim":
            data[name]["slim"] = True
        else:
            data[name]["slim"] = False
        data[name]["textureId"] = str(binascii.b2a_hex(os.urandom(32)).decode("utf-8"))
        data[name]["updated"] = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        counter += 1

    answer = input("If you want to render the skins, type 'yes' otherwise press ENTER: ")
    if answer == "yes":
        createPage(images)
        modelImages = grabImages()
        counter = 0
        for skin in data:
            data[skin]["modelImage"] = modelImages[counter]
            counter += 1

    json_data = json.dumps(data, indent=4)
    with open("launcher_skins.json", "w", encoding="utf-8") as file:
        file.write(json_data)

    print("Done")
