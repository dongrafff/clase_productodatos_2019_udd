
# Laboratorio: Detector de lentes un modelo de deep learning montado en Heroku

> A continuación se presenta mi primer Producto de Datos, es un aplicativo de detección de lentes, desarrollado en mi computador local y publicado en la plataforma heroku. El ejemplo disponible en https://detector-lentes.herokuapp.com/ 

## Algunas consideraciones realizadas en el aplicativo

> Este trabajo se realizó utilizo las fotografías desde google image. Luego de descargar las fotografías se realizó un filtro manual de tal forma que se obtuvieran efectivamente las fotos con las características requeridas. Lo anterior con la finalidad de encontrar un mejor ajuste al modelo y que la predicción sea la mejor posible.

> Se intento varias veces el modelo con diversos grupos de fotografías hasta que se obtuvo un ajuste con un error menor al 10%.

> Se modifico la presentación de heroku en el html de forma básica, dado el conocimiento el cual poseo, usted puede modificar el html a su gusto y poder complementarlo con todo lo que desee. Estos archivos html que puede modificar se encuentran en la carpeta template del repositorio.

> En el main frame del heroku se encuentra la contextualización del problema el cual lo soluciona el aplicativo presentado.

> Finamente a continuación se adjunta lo necesario para implementar el modelo y poder replicar el ejercicio con las modificaciones que desee implementar.


## Lo primero que se requiere

- Para poder realizar este laboratorio se necesita una cuenta en [GitHub](https://www.github.com/) y [Heroku](https://www.heroku.com/). Ambas son gratuitas y les serán muy útiles en el futuro.
- Se asume que el computador de cada estudiante tiene Python y Jupyter Notebook instalados (requisitos de varios cursos anteriores del programa). Si no es el caso, recomiendo seguir algún tutorial como esta [guía para instalar Jupyter Notebook en Windows 10](https://medium.com/@kswalawage/install-python-and-jupyter-notebook-to-windows-10-64-bit-66db782e1d02).

## Instalación de librerías necesarias

### Pytorch

- Seguir las [instrucciones oficiales](https://pytorch.org/get-started/locally/) seleccionando el sistema operativo correspondiente.

### fastai [(instrucciones)](https://docs.fast.ai/install.html)
```
pip install fastai
```

### Flask [(instrucciones)](https://flask.palletsprojects.com/en/1.1.x/installation/)
```
pip install Flask
```
### Si se desea modificar aún más la aplicación web, se recomienda usar un [ambiente virtual](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (además es una muy buena práctica al momento de programar en Python)

## Construcción del Modelo de Deep Learning

- Se deben seguir las instrucciones explicadas en este [notebook](https://github.com/aastroza/clase_productodatos_2019_udd/blob/master/notebooks/ejemplo_clasificador_fastai.ipynb).

## Modificación de la aplicación web

### Poner el modelo (archivo .pkl) en la carpeta `models` 

### Cambiar los nombres de las clases

- Abrir "app.py" y buscar la variable llamada `classes` y cambiar su contenido con las clases del clasificador propio.

### Modificaciones de la Interfaz

- Modificar los archivos en los directorios `templates` y `static`.

- `index.html` maneja la parte gráfica y `main.js` el comportamiento.



## Conexión con Heroku

- El primer paso es crear una aplicación y darle un nombre.

- En "Deployment Method" escoger "Connect to Github" y seguir las instrucciones.

- Una vez que esté listo, aparecerá un link para revisar la aplicacion en el navegador, como este: https://facemask-udd.herokuapp.com/

## Créditos

- La construcción del modelo está basada en las clases de [Francisco Ingham y Jeremy Howard](https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson2-download.ipynb). La aplicacion web está inspirada en el trabajo de [Shankar Jha](https://github.com/shankarj67/Water-classifier-fastai).

