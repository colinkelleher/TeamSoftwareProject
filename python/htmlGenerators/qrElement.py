import pyqrcode
import io


def create_qr_info(qrid):
    img = pyqrcode.create(qrid)
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
        """ % (svg, qrid)


if __name__ == '__main__':
    print(create_qr_info(123456789))
