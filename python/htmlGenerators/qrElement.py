import pyqrcode
import io


def create_qr_info(qrid):
    """
    :param qrid Integer id of whatever the qr code will be showing
    Function to create a div with the qr code svg image of the id and its hex representation
    Returns an html string
    """
    hex_id = ("0x%08X" % qrid)[2:].upper()
    img = pyqrcode.create(hex_id)
    buffer = io.BytesIO()
    img.svg(buffer)
    value = buffer.getvalue().decode()

    svg = value[len('<?xml version="1.0" encoding="UTF-8"?>') + 1:]

    return """
        <div class="idView">
                %s
                <br>
                <p>%s</p>
        </div>
        """ % (svg, hex_id)


if __name__ == '__main__':
    print(create_qr_info(123456789))
