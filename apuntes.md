# Templates

> Se recomienda utilizar un template base del que el resto de templates vayan heredando, sobretodo si quieres tener una página web con fluidez en su diseño.

* El template base funciona igual que cualquier archivo html.
* En un template base, se definen bloques en forma de `{% block name %}{% endblock %}` para determinar las partes modificables por los templates heredados.
* Es buena práctica cerrar los bloques con el nombre: `{% block name %}{% endblock name %}` para hacer más legible el código.

> Templates heredados

* Un template heredado no requiere tener toda la construcción html, pues está heredándola desde un template base, utilizando `{% extends "ruta/template_base.html" %}`
* Si un template heredado no contiene cierto bloque, se utilizará el template base como _fallback_ (se usará en su lugar)
* En un template heredado se puede redefinir los bloques colocados en `template_base.html` utilizando la misma estructura `{% block name %}{% endblock name%}`

# Models y Base de Datos

> Para utilizar una BD, se tiene que primero configurar en `settings.py` del proyecto.
  > En nuestro caso, para MySQL:
  ```py
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'django_demo',
      'USER': 'root',
      'PASSWORD': ''
    }
  }
  ```
> Para poder conectarse a la base de datos se requiere el uso de MariaDB 10.5 o superior. Usualmente se tiene que actualizar manualmente en Xampp

* Luego de eso, se define el model en el `models.py` de cualquier aplicación. 
  * La clase debe heredar de models.Model
  * Los atributos utilizan factores de models. E.J.: `models.CharField(length: int)`

# Repaso uso GIT

* Configurar GIT (para que los commits sean atribuidos correctamente)
  `git config --global user.name "Your Name"`
  `git config --global user.email "your.email@example.com"`
* Iniciar repositorio local
  `git init`
* Añadir archivos al repositorio de cambios
  * Archivo individual: `git add filename.ext`
  * Todos los archivos: `git add .`
* Confirmar cambios
  `git commit -m "Texto de Confirmación describiendo Cambios"`
* Añadir repositorio remoto (Github)
  `git remote add origin https://github.com/username/repository-name.git`
* Revisar conexión al repositorio remoto
  `git remote -v`
* Subir cambios al repositorio remoto
  `git push origin main`

## Deshacer cambios (en caso de error)
  * Quitar archivos del repositorio de cambios:
  `git reset filename.ext`
  * Deshacer el último commit:
  `git reset --soft HEAD~1`
  * Crear un commit que reemplace uno anterior:
  `git revert commit-hash`