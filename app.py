from gtts import gTTS
from playsound import playsound

#Diretório do áudio
audio = "audio.mp3"

#Linguagem que o audio será dito
language = 'pt-br'

#Texto para ser pronunciado no áudio
text = "Achei isto muito bacana hahaha"

#Criar o objeto com as informações passadas
sp = gTTS(text=text, lang=language, slow=False)

#Salvar o arquivo
sp.save(audio)

print("Audio criado com sucesso!")