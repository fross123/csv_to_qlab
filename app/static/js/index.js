// JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                var validFileExtensions = [".csv"];
                var fileElement = document.getElementById('csv_file');
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });

        document.getElementById("csv_file").onchange = function () {

            ValidateSingleInput(document.getElementById("csv_file"))
        }
    }, false);
})();

var _validFileExtensions = [".csv"];
function ValidateSingleInput(oInput) {
    if (oInput.type == "file") {
        var sFileName = oInput.value;
        if (sFileName.length > 0) {
            var blnValid = false;
            for (var j = 0; j < _validFileExtensions.length; j++) {
                var sCurExtension = _validFileExtensions[j];
                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                    blnValid = true;
                    break;
                }
            }

            if (blnValid) {
                oInput.classList.remove('is-invalid')
                oInput.classList.add('is-valid');
                return false;
            } else {
                oInput.classList.remove('is-valid');
                oInput.classList.add('is-invalid');
                return false;
            }
        }
    }
    return true;
}

document.addEventListener('DOMContentLoaded', (e) => {
    var ql5v = document.querySelector('#passcode-switch');
    var ql5group = document.querySelector('#passcode-group')
    ql5v.addEventListener('click', (e) => {
        if (ql5group.hidden) { // if the form is hidden
            ql5group.hidden = false;
        } else { // hide group
            ql5group.hidden = true;
        }
    })
})