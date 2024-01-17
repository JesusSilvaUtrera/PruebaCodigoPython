class colores:
    ELIMINAR_FORMATO = "\033[0m"
    NEGRO = "\033[0;30m"
    ROJO = "\033[0;31m"
    VERDE = "\033[0;32m"
    AMARILLO = "\033[0;33m"
    AZUL = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CIAN = "\033[0;36m"
    BLANCO = "\033[0;37m"
    NEGRITA_AMARILLO = "\033[1;33m"
    SUBRAYADO_AMARILLO = "\033[4;33m"
    CURSIVA_AMARILLO = "\033[3;33m"
    PARPADEO_AMARILLO = "\033[5;33m"
    FONDO_AMARILLO = "\033[7;33m"
    # AMARILLO también se podría ver como un MARRÓN
    # \033[<formato>;<color>m


logger = colores()
print(logger.AMARILLO + "HOLA" + logger.ELIMINAR_FORMATO)
