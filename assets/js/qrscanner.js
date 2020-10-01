/**
 To start scanning for a qrCode use the scanQrCode(element, callback) function
 - element is a htmlelement that you want to put the qr scanner under
 - callback is a function that returns the qr code after it has been read
 - Example function exampleCallback(code){...}

 Have to include both scripts
 <script src="qrscanner.js"></script>
 <script src="libs/jsQR.js"></script>

 Using https://github.com/cozmo/jsQR library for reading qr codes from image data

 */

scanQrCode = (function (element, callback) {
    /**
     To start scanning for a qrCode use the scanQrCode(element, callback) function
     :param element:    The html element to put the qr scanner under. For example the button the user pressed to start the scanner
     :param callback:   A function(qrCode) to run after the qr code has been read
     */

    // Different html elements that are set in setup() function
    var canvas;
    var canvasElement;
    var video;
    var qrInput;
    var qrConfirm;
    var qrContainer;
    var qrButtonDiv;
    // Variables to keep track of the state of scanning
    var qrConfirmed = false;
    var scrolledOnce = false;

    function confirmQr() {
        /**
         * Runs when confirm code button is pressed
         * - Runs the callback function
         * - Removes qr scanner from the page
         * - Stops camera
         */
        qrConfirmed = true;
        callback(parseInt(qrInput.value, 16));
        qrContainer.parentNode.parentNode.removeChild(qrContainer.parentNode);
        video.srcObject.getTracks().forEach(track => track.stop());
        video.srcObject = ""
    }

    function enterQrId() {
        /**
         * Runs when Enter Id Manually button is pressed
         * - Shows qrInput box and sets focus to it
         * - Shows confirm code button
         */
        qrInput.disabled = false;
        qrInput.focus();
        qrInput.style.background = '#deee';
        qrConfirm.style.visibility = 'visible'
    }

    function tick() {
        /**
         * Recursive method to
         * - Scroll down to qr scanner and set heights
         * - Update canvas with camera input
         * - Check if qr code is present in input
         * - If qr code is present show confirm code button
         * - Continue until user has pressed confirm code button
         */
        if (qrConfirmed) {
            return
        }
        if (video.readyState === video.HAVE_ENOUGH_DATA) {
            if (!scrolledOnce) {
                canvasElement.hidden = false;
                canvasElement.height = video.videoHeight;
                canvasElement.width = video.videoWidth;
                qrInput.style.top = (canvasElement.height - qrInput.style.height.slice(0, -2)) + "px";
                qrInput.style.width = canvasElement.width + 'px';
                qrButtonDiv.style.width = canvasElement.width + 'px';
                qrContainer.style.height = canvasElement.height + 'px';
                qrButtonDiv.scrollIntoView();
                scrolledOnce = true;
            }
            canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
            var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
            var code = jsQR(imageData.data, imageData.width, imageData.height, {
                inversionAttempts: "dontInvert",
            });
            if (code) {
                qrInput.value = code.data;
                qrInput.size = code.data.length;
                qrConfirm.style.visibility = 'visible'
            }
        }
        requestAnimationFrame(tick);
    }

    function setup() {
        /**
         * Setup function that
         * - Inserts qr scanner into webpage under element
         * - Initializes all the html elements as public variables
         * - Sets event listeners
         */
        var textStuff = '<div>'
            + '<div id="qrcontainer" style="position:relative; width:50%; height:10%; overflow: auto;">'
            + '<canvas width="50%" height="10%" id="qrcanvas" style="display:block;"></canvas>'
            + '<textarea disabled id="qrinput" style="position:absolute;top:200px;width:80%;height:200px;font-size:50pt;font-weight:bold;border:none;color:black;"></textarea>'
            + '</div>'
            + '<div id="qrButtonDiv">'
            + '<br><button id="qrenterid" class="btn btn-primary btn-lg mb-1">Enter Id Manually</button></br>'
            + '<button id="qrconfirm" class="btn btn-primary btn-lg mb-1"">Confirm Code</button>'
            + '</div></div>';
        var template = document.createElement('template');
        template.innerHTML = textStuff.trim();
        element.parentNode.insertBefore(template.content.firstChild, element.nextSibling);

        qrContainer = document.getElementById('qrcontainer');
        qrButtonDiv = document.getElementById('qrButtonDiv');
        qrInput = document.getElementById('qrinput');
        canvasElement = document.getElementById('qrcanvas');
        qrConfirm = document.getElementById('qrconfirm');

        qrConfirm.addEventListener('click', confirmQr);
        document.getElementById('qrenterid').addEventListener('click', enterQrId);

        qrInput.style.background = 'transparent';

        video = document.createElement("video");
        canvas = canvasElement.getContext("2d");
    }


    function start() {
        /**
         * Start function that runs setup(), gets camera input and starts running the recursive tick() method
         */
        setup();
        //Use facingMode: environment to attemt to get the front camera on phones
        navigator.mediaDevices.getUserMedia({video: {facingMode: "environment"}}).then(function (stream) {
            video.srcObject = stream;
            video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
            video.play();
            requestAnimationFrame(tick);
        });
    }

    // Start
    start();

});