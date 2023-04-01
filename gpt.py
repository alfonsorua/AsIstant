import json
import openai
import whisper
from gtts import gTTS
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import site


def run(data):


    # Cargar la clave de la API
    openai.api_key = json.load(open('./claves.json'))["openAIclave"]

    data.save('input.wav')


    model = whisper.load_model("medium")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio('input.wav')
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions()
    resulta = whisper.decode(model, mel, options)




    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': resulta.text}
    ],
    temperature = 0  
    )
    respuesta=completion['choices'][0]['message']['content']

    ##crear audio
    if (resulta.language == 'es'):
        path = site.getsitepackages()[1]+"\TTS\.models.json"
        model_manager = ModelManager(path)
        model_path, config_path, model_item = model_manager.download_model("tts_models/es/css10/vits")
        syn = Synthesizer(
            tts_checkpoint=model_path,
            tts_config_path=config_path,
        )
        outputs = syn.tts(respuesta)
        syn.save_wav(outputs, "respuesta.wav")
    elif(resulta.language == 'en'):
        path = site.getsitepackages()[1]+"\TTS\.models.json"
        model_manager = ModelManager(path)
        model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")
        voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])
        syn = Synthesizer(
            tts_checkpoint=model_path,
            tts_config_path=config_path,
            vocoder_checkpoint=voc_path,
            vocoder_config=voc_config_path
        )        
        outputs = syn.tts(respuesta)
        syn.save_wav(outputs, "respuesta.wav")
    else:
        myobj = gTTS(text=respuesta, lang=resulta.language, slow=False)
        myobj.save("respuesta.wav")
  



