'''
Descrição: Este script realiza a descompactação de alguns arquivos.
'''

import zipfile
import tarfile

def descompactar_arquivo(filepath, destino):
    if filepath.endswith('.zip'):
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(destino)
    elif filepath.endswith('.tar.gz') or filepath.endswith('.tgz'):
        with tarfile.open(filepath, 'r:gz') as tar_ref:
            tar_ref.extractall(destino)
    elif filepath.endswith('.tar.bz2') or filepath.endswith('.tbz2'):
        with tarfile.open(filepath, 'r:bz2') as tar_ref:
            tar_ref.extractall(destino)
    elif filepath.endswith('.tar.xz') or filepath.endswith('.txz'):
        with tarfile.open(filepath, 'r:xz') as tar_ref:
            tar_ref.extractall(destino)
    else:
        print(f"Formato de arquivo não suportado: {filepath}")