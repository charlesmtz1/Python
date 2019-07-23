
mensaje = "Hola a todos! :)"
lista = mensaje.split(' ')

emojis = {
    ":)" : "😄",
    ":(" : "️☹️"
}

mensaje_convertido = ""
for word in lista:
    mensaje_convertido += emojis.get(word, word) + " "

print(mensaje_convertido)