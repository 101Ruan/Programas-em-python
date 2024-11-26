 import sys
import os

# deletar arquivo desejado
os.remove("arquivo.txt")

# cria arquivo indesejado
open("arquivo.txt", "w").write("texto")

# consumir recursos
print("")
