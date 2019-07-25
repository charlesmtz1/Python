def fin_de_ejecucion():
    print("\n----------------------------")
    print("------Fin de ejecucion------")
    print("----------------------------")


try:
    f = open("Prueba.txt", "w")
except FileExistsError:
    print("El archivo ya existe!")
else:
    f.write("Hello World, this a file example!\n\n")
    num_miembro = 1
    muse = list(("Honoka Kohsaka", "Kotori Minami", "Umi Sonoda", "Hanayo Koizumi",
                    "Rin Hoshizora", "Maki Nishikino", "Nico Yazawa", "Eri Ayase", "Nozomi Touhou"))

    aqours = list(("Chika Takami", "You Watanabe", "Riko Sakurauchi", "Hanamaru Kunikida",
                    "Yoshiko Tsushima", "Ruby Kurosawa", "Mari Ohara", "Dia Kurosawa", "Kanan Matsuura"))

    f.write("u's members:\n")
    for miembro in muse:
        f = open("Prueba.txt", "a")
        f.write(f'{num_miembro}.- {miembro}\n')
        num_miembro += 1

    num_miembro = 1

    f.write("\naqours members:")
    for miembro in aqours:
        f = open("Prueba.txt", "a")
        f.write(f'\n{num_miembro}.- {miembro}')
        num_miembro += 1 

    f.write("\n\nEOF")

    f.close()
