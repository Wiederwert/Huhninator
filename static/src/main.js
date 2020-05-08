const huhn = document.getElementById('huhn');
const out = document.getElementById('output');
const audio = document.getElementById('audio');
var id;

const getCite = function() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/cites');

    xhr.onload = function() {
        let data = JSON.parse(xhr.response);

        if (id != data.id) {
            id = data.id;
            out.innerText = data.text;
        }
        else {
            getCite();
        }
        
    };

    xhr.send();
    audio.play();
}

huhn.addEventListener('click', getCite);
