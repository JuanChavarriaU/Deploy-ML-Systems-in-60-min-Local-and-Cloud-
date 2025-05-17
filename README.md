# 🧠 Workshop IEEE CIS – De Modelado a Producción en 60 Minutos

Este proyecto demuestra cómo pasar de un modelo de Machine Learning entrenado localmente, hasta servirlo como una API pública desplegada en la nube usando herramientas modernas y gratuitas.

---

## 🔁 Estructura del Taller

### Parte 1: Entrenamiento y Despliegue Temporal (Colab + Flask + ngrok)

1. Entrenamos un modelo de clasificación usando el dataset **Iris** y `RandomForestClassifier` en Google Colab.
2. Creamos una API con **Flask** y la servimos con `ngrok` directamente desde Colab.
3. Probamos la API con entradas válidas e inválidas desde otra celda Colab.

📁 Archivo: [colab_temp_deployment.ipynb](https://colab.research.google.com/drive/1uJelL9UpgV8do4MYnROnIGsBWC5qZDVI?usp=sharing)


# Cómo configurar ngrok en Colab
1. Ve a [ngrok.com](https://ngrok.com/)
2. Crea una cuenta.
3. Una vez tengas la cuenta creada, ve a al menú -> Getting started -> Your authtoken.

![image](https://github.com/user-attachments/assets/20005bb9-4e23-4a4b-a229-6c2d2473ec73)

4. Copia tu llave.

![image](https://github.com/user-attachments/assets/76877a36-639d-46d8-93f4-a357247cbf71)

5. Ve al cuaderno en Google Colab y accede al icono de la llave 🗝️.

![image](https://github.com/user-attachments/assets/0489c8f3-1c0b-4dfa-9b1e-2a6652009f22)
  
6. Le das a añadir un nuevo secreto.

![image](https://github.com/user-attachments/assets/b557a6fe-7c9f-4c5e-8da8-994ee6d0ef75)

7. Le das un nombre o identificador a la llave, pega la clave que copiaste de ngrok en el campo de clave y activas el acceso desde cuaderno.

![image](https://github.com/user-attachments/assets/c62c30e6-c4e4-454e-bd60-55a2d4b24316)

8. De esta forma podrás usar correr el notebook sin problemas.
   
---

### Parte 2: Contenerización y Despliegue Real en la Nube (FastAPI + Docker + Azure)

📌 Modelo: regresión lineal para predicción de precios de viviendas.

- Cómo hacer la implementación en local.

> Requerimientos
> Windows subsystem for linux: En la terminal de powershell ejecuta el siguiente comando.

````
  wsl --install -d Ubuntu-24.04
````

> Docker Desktop: [Windows](https://docs.docker.com/desktop/setup/install/windows-install/) | [Mac](https://docs.docker.com/desktop/setup/install/mac-install/) | [Linux](https://docs.docker.com/desktop/setup/install/linux/)

> [Git](https://git-scm.com/downloads)

#### Una vez con estos requisitos instalados.
 - Abrir la terminal en su carpeta de proyectos preferida y clonar el repositorio.
 ````
  git clone https://github.com/JuanChavarriaU/Deploy-ML-Systems-in-60-min-Local-and-Cloud-.git
  ````
 - Moverse a la carpeta
   ````
   cd Deploy ML Systems in 60 min Local and Cloud
   ```` 
 - una vez dentro ejecutar el siguiente comando de Docker
   ````
    docker build -t pred-price-api .
   ````
- Luego de ejecutar esto, tendremos nuestra imagen con la api. ahora crearemos nuestro contenedor con esta imagen de base.
  ````
  docker run -rm --name ml-api -p 80:80 pred-price-api
  ````
  > Este comando va a levantar el contenedor con la imagen que previamente creamos estará disponible en el puerto 80 de nuestro localhost y una vez que detengamos el contenedor este se eliminará
  ````
  docker stop ml-api
  ````
 #### Una vez aquí podrás acceder a http://localhost:80.
  
1. **Entrenamos un nuevo modelo** (`LinearRegression`) y lo guardamos con `pickle`.
2. **Creamos una API con FastAPI** que expone un endpoint `/predict`.
3. **Contenerizamos la aplicación con Docker** y validamos que funcione localmente.
   ````
      docker build -t nombre_de_imagen:latest .
   ````
   
   - Comando básico para crear el contenedor, mapear el puerto 8000 del contenedor al de nuestra pc y -rm para que cuando lo detengamos este se elimine.  
     
   ````
      docker run -rm -p 8000:8000 image_name
   ````
4. **Subimos la imagen a Azure Container Registry (ACR)**:
   ```bash
   az acr login --name <registry_name>
   docker tag myimage <registry_name>.azurecr.io/myimage:latest
   docker push <registry_name>.azurecr.io/myimage:latest
6. Desplegamos el contenedor en Azure Container Instance (ACI):
  ````
az container create \
  --resource-group <rg-name> \
  --name <aci-name> \
  --image <registry-name>.azurecr.io/myimage:v1 \
  --dns-name-label <label> \
  --ports 80 \
  --os-type Linux \
  --cpu 1 \
  --memory 1.5 \
  --location eastus
  ````
6. Obtenemos el FQDN de acceso:
````
 http://<label>.eastus.azurecontainer.io/predict
````

> Nota: recuerda eliminar todos los recursos que hayas creado. 
   
