# GestSound
Controla tu musica con gesto de la mano en tiempo real, con una interfaz visual que muestra la cancion actual, el volumen y los gestos detectados.

---

## Descripción
GestSound es una aplicacion que permite controlar la reproduccion de música usando la camara web y gestos de la mano.
Puedes reproducir, pausar, adelantar o retroceder canciones, subir o bajar volumen, e incluso ver tu lista de música sin tocar el teclado ni el mouse.

---

## Funcionalidades
- **Gestos y acciones:**
- Dos dedos -> Play/Pause
- Dos dedos mover a  la derecha -> adelanta a una canción
- Dos dedos mover a la izquierda -> retroceder a una canción
- Apretar dos veces con los dedos índice y corazón -> adelantar 10 o 5 seg
- Apretar dos veces con los dedos anular y meñique(?) -> retroceder 10 o 5 seg
- Subir/Bajar los dedos indice y corazón -> Subir/Bajar volumen(medido a limite de 100)
- Bajar todo los dedos de la mano para arriba -> Ver lista de canciones
- Mover el dedo indice de izquierda a derecha -> Ir a un punto especifico de la canción

- **Interfaz visual:**
  - Mostrar canción actual
  - Mostrar volumen actual
  - Indicar gesto detectado
  - Lista de canciones disponible
 
---

### Tecnologías utilizadas
- **Python 3.10+**
- **OpenCV** → Captura de video en tiempo real
- **MediaPipe Hands** → Detección de manos y gestos
- **python-vlc** → Reproducción de música
- **Tkinter** → Interfaz gráfica de usuario

Opcional:
- Spotify API → Control de música en streaming
- TensorFlow / PyTorch → Entrenamiento de gestos personalizados

## Estructura del Proyecto

HandBeats/
│                                                        
├─ main.py # Archivo principal que inicia la aplicación                                                                                                 
├─ gestures.py # Código de detección y reconocimiento de gestos                                                                                              
├─ player.py # Funciones de reproducción de música (play, pause, skip, volume)                                                                                              
├─ gui.py # Interfaz gráfica                                                                                              
├─ music/ # Carpeta con archivos de música                                                                                              
└─ requirements.txt # Librerías necesarias                                                                                              

--- 

## Requisitos

- Cámara web o integrada
- Python 3.10+
- Librerías:  
```bash
pip install opencv-python mediapipe python-vlc


pip install -r requirements.txt

python main.py
```

### Roadmap de desarrollo

Fase 1: Reproducción de música y pruebas con VLC.

Fase 2: Detección de gestos básicos con MediaPipe.

Fase 3: Asociar gestos con acciones de música.

Fase 4: Crear interfaz gráfica y mostrar información.

Fase 5: Pruebas, mejoras y detección de gestos avanzados.

---

### Ideas futuras

- Entrenamiento de gestos personalizados.
- Integración con Spotify o YouTube Music.
- Reconocimiento de gestos múltiples o combinados.
- Mejora de la interfaz con PyQt o diseño más moderno.

## Autor
Kjaris Alfaro Pachas
Correo: kjarisalfaro14@gmail.com
