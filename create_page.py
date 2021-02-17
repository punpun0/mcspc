# Credits to:
# https://github.com/bs-community/skinview3d


# I understand this is super messy and not the way you should do it, but it will have to do because I have zero experience in javascript


def createPage(images):
    text = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <title>skinview3d / offscreen-render</title>
</head>

<body>
    <div id="rendered_imgs"></div>
    <script src="./js/skinview3d.bundle.js"></script>
    <script>
        const configurations = [
            """

    for i in range(0, len(images)):
        if i == len(images) - 1:
            skin = """
            {
                skin: "%s",
                cape: null
            }""" % (
                images[i]
            )
        else:
            skin = """
            {
                skin: "%s",
                cape: null
            },""" % (
                images[i]
            )
        text += skin

    text += """
        ];

        (async function () {
            const skinViewer = new skinview3d.SkinViewer({
                width: 288,
                height: 384,
                renderPaused: true
            });
            skinViewer.camera.rotation.x = -0.620;
            skinViewer.camera.rotation.y = 0.534;
            skinViewer.camera.rotation.z = 0.348;
            skinViewer.camera.position.x = 30.5;
            skinViewer.camera.position.y = 22.0;
            skinViewer.camera.position.z = 42.0;

            for (const config of configurations) {
                await Promise.all([
                    skinViewer.loadSkin(config.skin),
                    skinViewer.loadCape(config.cape, { backEquipment: config.backEquipment })
                ]);
                skinViewer.render();
                const image = skinViewer.canvas.toDataURL();
				console.log(image);
                const imgElement = document.createElement("img");
                imgElement.src = image;
                imgElement.width = skinViewer.width;
                imgElement.height = skinViewer.height;
                document.getElementById("rendered_imgs").appendChild(imgElement);
            }

            skinViewer.dispose();
        })();
    </script>
</body>

</html>
    """
    with open("offscreen_render.html", "w", encoding="utf-8") as f:
        f.write(text)
