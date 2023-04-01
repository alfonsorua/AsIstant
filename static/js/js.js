
const recordButton = document.getElementById("recordButton");
const stopButton = document.getElementById("stopButton");
const audioFile = document.getElementById('audioFile');
const player = document.getElementById("player");
const downloadLink = document.getElementById("downloadLink");
const carga = document.getElementById("cargaDiv");

let recorder;
let stream;

recordButton.addEventListener("click", async () => {
  player.classList.add('hidden');
  stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  recorder = new MediaRecorder(stream);
  recorder.start();
  recordButton.disabled = true;
  stopButton.disabled = false;

  
});

stopButton.addEventListener("click", async () => {
  recorder.stop();
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
    stream = null;
  }
  carga.classList.remove('hidden');
  recorder.addEventListener("dataavailable", async (e) => {


    const audioData = e.data;
    const formData = new FormData();
    formData.append('audio', audioData);
    

    //esperamos por la respuesta del servidor
    const audio2 = await python(formData);
    const audioURL=URL.createObjectURL(audio2);
    
    //const audioURL = URL.createObjectURL(audioRespuesta);
    player.src = audioURL;
    player.classList.remove('hidden');
    player.play();
    carga.classList.add('hidden');
    

  });

  recordButton.disabled = false;
  stopButton.disabled = true;
  
  
});


async function python(formData) {
    const response= await fetch('http://localhost:5000/answer', {
        method: 'POST',
        body: formData
    });

    const audio2 = await response.blob();
    return audio2;

}




