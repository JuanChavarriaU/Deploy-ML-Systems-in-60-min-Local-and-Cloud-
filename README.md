# 🧠 Workshop IEEE CIS – De Modelado a Producción en 60 Minutos

Este proyecto demuestra cómo pasar de un modelo de Machine Learning entrenado localmente, hasta servirlo como una API pública desplegada en la nube usando herramientas modernas y gratuitas.

---

## 🔁 Estructura del Taller

### Parte 1: Entrenamiento y Despliegue Temporal (Colab + Flask + ngrok)

1. Entrenamos un modelo de clasificación usando el dataset **Iris** y `RandomForestClassifier` en Google Colab.
2. Creamos una API con **Flask** y la servimos con `ngrok` directamente desde Colab.
3. Probamos la API con entradas válidas e inválidas desde otra celda Colab.

📁 Archivo: [`colab_temp_deployment.ipynb`]([colab_temp_deployment.py](https://colab.research.google.com/drive/1uJelL9UpgV8do4MYnROnIGsBWC5qZDVI?usp=sharing))

---

### Parte 2: Contenerización y Despliegue Real en la Nube (FastAPI + Docker + Azure)

📌 Modelo: regresión lineal para predicción de precios de viviendas.

1. **Entrenamos un nuevo modelo** (`LinearRegression`) y lo guardamos con `pickle`.
2. **Creamos una API con FastAPI** que expone un endpoint `/predict`.
3. **Contenerizamos la aplicación con Docker** y validamos que funcione localmente.
4. **Subimos la imagen a Azure Container Registry (ACR)**:
   ```bash
   az acr login --name <registry_name>
   docker tag myimage <registry_name>.azurecr.io/myimage:latest
   docker push <registry_name>.azurecr.io/myimage:latest
5. Desplegamos el contenedor en Azure Container Instance (ACI):
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
   
