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
def organizar():
    for item in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, item)
        if os.path.isfile(caminho_completo):
            nome, extensao = os.path.splitext(item)
            for pasta, extensoes in tipos.items():
                if extensao.lower() in extensoes:
                    destino = os.path.join(pasta_alvo, pasta)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(caminho_completo, destino)