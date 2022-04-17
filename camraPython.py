import cv2 as cv # IMPORTAMOS CV2

capturarVideo = cv.VideoCapture(0)  # 0: PARA BUSCAR CAMARAS CONECTADOS A LA PC (1: CAMARAS EXTERNAS)

if not capturarVideo.isOpened():    # SI NO RECONOCE LA CAPTURA DE VIDEO, SI NO HAY CAMARA.
    print("[-] No hay camara")      # MENSAJE DE AUSENCIA DE CAMARA
    exit()                          # TERMINA PROCESO Y SE CIERRA CAPTURA DE CAMARA

while True:                                     # EN CASO DE QUE HAYA CAMARA
    _,Camara = capturarVideo.read()             # INICIALIZAMOS CAPTURA DE VIDEO Y LO ALMAENAMOS EN CAMARA - READ ARROJA DOS VALORES: PERO COMO NO UTILIZAREMOS EL TIPO DE CAMARA LO OMITIMOS
    cv.imshow("[+] En directo",Camara)          # MOSTRARA LO QUE SE ESTA CAPTURANDO
    if cv.waitKey(1)==ord("q"):                 # ESTO SIRVE PARA DETENER VIDE0 (1: ES CONTINUO - CUANDO ES IMAGEN ESTATICA SERIA 0)
        break                                   # DEDIENE BLUCLE
                                                        
capturarVideo.release()                         # DETENEMOS EL VIDEO
cv.destroyAllWindows()                          # DESTRUIMOS TODAS LAS VENTANAS QUE SE HAYAN ABIERTO
