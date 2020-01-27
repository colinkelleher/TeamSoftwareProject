from PIL import Image, ImageDraw, ImageFont


def draw_point(path_to_blank_map, x, y, output_path, point_size=20, color=(255, 0, 0), location_name="Generic Storage"):
    """
    Function to the location on the map.
    :param path_to_blank_map: String path to empty to map
    :param x: Int representing the x cord of the center of the point
    :param y: Int representing the y cord of the center of the point
    :param output_path: String representing the path to the output file
    :param point_size: Int representing the size of the point to be drawn
    :param color: Tuple representing the rgb color of the point.
    :param location_name: String representing the title to be added to the image
    :return: None
    """
    map_image = Image.open(path_to_blank_map)
    draw = ImageDraw.Draw(map_image)
    draw.ellipse((x, y, x + point_size, y + point_size), fill=color)
    font = ImageFont.truetype("/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf", 16)
    draw.text((10, 10), location_name, color, font=font)
    del draw

    map_image.save(output_path, "PNG")


if __name__ == "__main__":
    draw_point("../images/locations/main.png", 100, 100, "test.png")
