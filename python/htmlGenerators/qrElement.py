import pyqrcode
import io


def create_qr_info(qrid):
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
