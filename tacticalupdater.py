import os
import json
import urllib.parse

# --- SUAS CONFIGURAÇÕES ---
REPO_USER = "manthuso"
REPO_NAME = "tactical-mcupdater"
BRANCH = "main"  # Se der erro de 404, verifique se o github criou como 'master'
# --------------------------

base_url = f"https://github.com/{REPO_USER}/{REPO_NAME}/raw/{BRANCH}/"
mods_lista = []

print(f"--- Gerando lista para {REPO_NAME} ---")

# Varre a pasta atual procurando .jar
for arquivo in os.listdir():
    if arquivo.endswith(".jar"):
        # Encode resolve problemas com espaços no nome do arquivo (ex: "mod v1.jar" vira "mod%20v1.jar")
        url_segura = base_url + urllib.parse.quote(arquivo)
        
        # Estrutura padrão. Se o Simple Mod Sync pedir campos diferentes, altere aqui.
        mod_info = {
            "filename": arquivo,
            "downloadUrl": url_segura
        }
        mods_lista.append(mod_info)
        print(f"[+] Adicionado: {arquivo}")

# Salva o arquivo modlist.json
nome_arquivo_json = "modlist.json"
with open(nome_arquivo_json, "w") as f:
    json.dump({"mods": mods_lista}, f, indent=2)

print(f"\nSUCESSO! Arquivo '{nome_arquivo_json}' gerado com {len(mods_lista)} mods.")
print("Agora rode: git add . && git commit -m 'update' && git push")