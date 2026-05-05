import os
import shutil
from datetime import datetime

pasta_alvo = os.path.dirname(os.path.abspath(__file__))

print("Iniciando organizador...")
print(f"Pasta selecionada: {pasta_alvo}")
tipos = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".jpeg", ".png"],
    "Planilhas" : [".xlsx", ".csv"],
    "Documentos" : [".doc", ".docx"],
    "Apresentacoes" : [".ppt", ".pptx"]

}