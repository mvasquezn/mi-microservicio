from fastapi import FastAPI
import elasticapm
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
import os

# Configuración APM desde variables de entorno
apm_config = {
    "SERVICE_NAME": "mi-microservicio",
    "SECRET_TOKEN": '',
    "SERVER_URL": "http://monitoreo.prophecyai.tech:8200",   
    "ENVIRONMENT": "Sandbox"
}

apm_client = make_apm_client(apm_config)

app = FastAPI()
app.add_middleware(ElasticAPM, client=apm_client)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hola desde OpenShift usando Elastic APM"}