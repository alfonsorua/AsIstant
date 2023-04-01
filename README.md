# AsIstant [en]

A simple project about the use of various technologies to achieve a voiceBot that answers our questions.

To do this we will mainly use 3 technologies:

* **Whisper**, a library by OpenAI that can transcribe audio in different languages.
* **ChatGPT**, the well known chatBot also from OpenAI, we use it through its API (paid but very cheap).
* **TTS**, a library by Coqui created to read text like humans, it outperforms Google's gTTS (also used in this project) but it doesn't have all languages available so we are only useing it for English and Spanish.

For the interfacer it has a simple web managed directly with Flask library in python.


### INSTALL:

It is necessary to have python installed and then we will install the libraries we need with:

```
pip3 install -r requirements.txt
```

This can take a few minutes, after that, we need to modify the "claves.json" file to add our OpenAI API key, you can get it from [OpenAI](https://platform.openai.com/account/api-keys), but you must have a payment method configured. The cost after a few hours of use was around 0.01$ so we should not be worried about it.

Finally, we run the "app.py" file wich will creat the server by default on [localhost:5000](http://127.0.0.1:5000).

### USE:

The web is quite intuitive, when you click on "Grabar" button it starts to record, when you click on "Detener" it will stop. After this we must wait for the process to complete (first time it may take several minutes because it has to download all the models) and then it will play the audio with the answer.

Here an example of [Question](https://cf-media.sndcdn.com/esGPJZ5X6RxM?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vZXNHUEpaNVg2UnhNKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MDM4MjY4Mn19fV19&Signature=NjDh2XRiBR5s2MvN18M757sKfCjtm0vYyMHzn7-hjB4R3maqbOiX0pGgAYwZI~6pDfv2NQ8K3ayP8nInqezACkzK5to8nXUqm5SiJY7I5JfEeXp7gW-4n0paamycUr6jpLV5KVHcK22iYXk1rRT5CLtOY7b4wYRrg2QWXuRWjgR2sDxDnEcOkcZExQiWV18-tPp3AEZEZtmIwI~P-QaT-0QfOmhdD2MscMtFhOyi1N2UWmglaCV5aT6ZjY-viK5AHqzAbbm3ENVy4iWxVmw4FnhVixsPV3Ikze0QvzPvONrKVAT1L-CMvfFnTlB0Kv15ZlNk8SPyX~X1gOTTvlhjtw__&Key-Pair-Id=APKAI6TU7MMXM5DG6EPQ) y [Answer](https://cf-media.sndcdn.com/ftV3LVPt92h1?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vZnRWM0xWUHQ5MmgxKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MDM4Mjc5NX19fV19&Signature=a4JG7BToqvgd5fBYnAlEnXWeDBQKkv59lAXq-h3kSWze~Qcm~hxQdvXht8J4RTcLf5FVesJHYa4YE1Zv7anhFZYn7LiPqd4irV5hEK5btcdZe4TPqOFFlkKzAHgcHkc5v8Lnq~zD5UZ4biIq94fA5ECD8hszCWaLPDlIkJPGO5WwLkGRLD2rsH4Tq~jozGzp58YXE8qtaDQzBlf6wJwolw8Z68gYm58LLgcdnT3v1N~jtWd9-pCayVhWLMwT32ytAreConNQa~JT41Pz91~45CLqVCB0gaIXWiPo-83l1FSoB~DJDmNsTbPVtfne~f-4f26~xtuOGPcVi0GU0CB24w__&Key-Pair-Id=APKAI6TU7MMXM5DG6EP)

---

# AsIstant [es]

Un proyecto sencillo consistente en el uso de diversas tecnologías para lograr un voiceBot que conteste a nuestras preguntas.

Para ello usaremos principalmente 3 tecnologías:

* **Whisper**, una librería de OpenAi que puede transcribir conversaciones en distintos idiomas.
* **ChatGPT**, el más que conocido chatBot de OpenAi, lo usaremos mediante su API (es de pago pero bastante económica).
* **TTS**, una librería de la startup Coqui, creada para leer texto de forma más similar a los humanos, mejora a la librería gTTS de Google (la cual también usamos en este proyecto) pero con el inconveniente de no tener tantos idiomas disponibles.

En la parte de la interfaz tenemos una web simple gestionada directamente con python mediante la librería Flask.


### INSTALACION:

Para que funcione el proyecto es necesario tener instalado python, con el cual instalaremos las librerías que necesitamos:

```
pip3 install -r requirements.txt
```

Esto puede tardar unos minutos, tras ello, necesitamos modificar el archivo "claves.json" para añadir nuestra clave de la API de OpenAi, se puede obtener en [OpenAI](https://platform.openai.com/account/api-keys), pero se debe tener un metodo de pago activo. El gasto aproximado tras unas horas de uso fué de 0.01€, por lo que no debería preocuparnos en exceso.

Finalmente, ejecutamos el archivo "app.py", lo cual creará el servicio web por defecto en [localhost:5000](http://127.0.0.1:5000).

### USO:

La web es bastante intuitiva, al pulsar en el boton de "Grabar" comienza a escucharnos, y al pulsar en "Detener" parará. Tras esto debemos esperar a que se procese (la primera vez puede tardar varios minutos debido a que tiene que descargar todos los modelos) y despues se nos reproducirá el audio con la respuesta.

Este es un ejemplo de [Pregunta](https://cf-media.sndcdn.com/esGPJZ5X6RxM?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vZXNHUEpaNVg2UnhNKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MDM4MjY4Mn19fV19&Signature=NjDh2XRiBR5s2MvN18M757sKfCjtm0vYyMHzn7-hjB4R3maqbOiX0pGgAYwZI~6pDfv2NQ8K3ayP8nInqezACkzK5to8nXUqm5SiJY7I5JfEeXp7gW-4n0paamycUr6jpLV5KVHcK22iYXk1rRT5CLtOY7b4wYRrg2QWXuRWjgR2sDxDnEcOkcZExQiWV18-tPp3AEZEZtmIwI~P-QaT-0QfOmhdD2MscMtFhOyi1N2UWmglaCV5aT6ZjY-viK5AHqzAbbm3ENVy4iWxVmw4FnhVixsPV3Ikze0QvzPvONrKVAT1L-CMvfFnTlB0Kv15ZlNk8SPyX~X1gOTTvlhjtw__&Key-Pair-Id=APKAI6TU7MMXM5DG6EPQ) y [Respuesta](https://cf-media.sndcdn.com/ftV3LVPt92h1?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vZnRWM0xWUHQ5MmgxKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MDM4Mjc5NX19fV19&Signature=a4JG7BToqvgd5fBYnAlEnXWeDBQKkv59lAXq-h3kSWze~Qcm~hxQdvXht8J4RTcLf5FVesJHYa4YE1Zv7anhFZYn7LiPqd4irV5hEK5btcdZe4TPqOFFlkKzAHgcHkc5v8Lnq~zD5UZ4biIq94fA5ECD8hszCWaLPDlIkJPGO5WwLkGRLD2rsH4Tq~jozGzp58YXE8qtaDQzBlf6wJwolw8Z68gYm58LLgcdnT3v1N~jtWd9-pCayVhWLMwT32ytAreConNQa~JT41Pz91~45CLqVCB0gaIXWiPo-83l1FSoB~DJDmNsTbPVtfne~f-4f26~xtuOGPcVi0GU0CB24w__&Key-Pair-Id=APKAI6TU7MMXM5DG6EPQ)


---



# Web

![1](./doc/1.png)

![2](./doc/2.png)

![3](./doc/3.png)

![4](./doc/4.png)
