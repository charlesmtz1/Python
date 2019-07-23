def convertidor_emojis(mensaje):
    lista = mensaje.split(' ')
    mensaje_convertido = ""

    emojis = {
        ":)" : "😄",
        ":(" : "️☹️",
        ":D" : "🎌"
    }
    
    for word in lista:
        mensaje_convertido += emojis.get(word, word) + " "

    return mensaje_convertido


mensaje = input(">")

print(convertidor_emojis(mensaje))