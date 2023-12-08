import winreg, os

# Caminho do registro onde você deseja adicionar as chaves/valores
caminhoChaveBase = "AppProjetos"
caminhoChaveSubPasta = os.path.join(caminhoChaveBase, 'Parametros')

nomeValorChave = 'txtTemaPadrao'
valorChave = 'superhero'

nomeValorChaveMulti = 'txtListaTemasPadroes'
valorChaveMulti = ["cosmo", "darkly", "morph", "superhero"]

novoValor = 'darkly'


# Verificar se a chave existe
def verificaChave(validaCaminho):    
    try:
        validaRegistroExistente = winreg.OpenKey(winreg.HKEY_CURRENT_USER, validaCaminho)
        winreg.CloseKey(validaRegistroExistente)
        return 1
    except FileNotFoundError:
        return 0

# Criar uma chave no registro
def criarNovaChave(caminhoChave): #A nova chave pode ser entendida também, como a subpasta a ser criada, neste exemplo, no registro HKEY_CURRENT_USER
    if not verificaChave(caminhoChave):
        try:
            chaveRegistro = winreg.CreateKey(winreg.HKEY_CURRENT_USER, caminhoChave)
            winreg.CloseKey(chaveRegistro)
            return 1
        except Exception as e:
            print(f"Erro ao criar chave: {e}")
            return 0
    else:
        print("Chave já existe, não é necessário criar.")
        return 1

# Adicionar um valor à chave
def adicionarValorSimples(nomeValorChave, valorChave):
    try:
        chaveRegistro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminhoChaveSubPasta, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(chaveRegistro, f"{nomeValorChave}", 0, winreg.REG_SZ, f"{valorChave}")
        winreg.CloseKey(chaveRegistro)
        return 1
    except Exception as e:
        print(f"Erro ao adicionar valor: {e}")
        return 0

def adicionarValorMulti(nomeValorChaveMulti, valorChaveMulti):
    try:
        chaveRegistro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminhoChaveSubPasta, 0, winreg.KEY_SET_VALUE)
        # Adiciona os valores à chave como REG_MULTI_SZ
        winreg.SetValueEx(chaveRegistro, f"{nomeValorChaveMulti}", 0, winreg.REG_MULTI_SZ, valorChaveMulti)
        
        winreg.CloseKey(chaveRegistro)
        return 1
    except Exception as e:
        print(f"Erro ao adicionar valores: {e}")
        return 0

# Atualizar um valor existente na chave
def atualizarValor(nomeValorChave, novoValor):
    try:
        chaveRegistro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminhoChaveSubPasta, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(chaveRegistro, nomeValorChave, 0, winreg.REG_SZ, novoValor)
        winreg.CloseKey(chaveRegistro)
        print(f"Valor '{nomeValorChave}' atualizado com sucesso para '{novoValor}'!")
        return 1
    except Exception as e:
        print(f"Erro ao atualizar valor: {e}")
        return 0

def consultarValorSimples(nomeValorChave):
    try:
        chaveRegistro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminhoChaveSubPasta, 0, winreg.KEY_READ)
        valor, tipo = winreg.QueryValueEx(chaveRegistro, nomeValorChave)
        winreg.CloseKey(chaveRegistro)
        print(f"Valor recuperado: {valor}")
    except Exception as e:
        print(f"Erro ao recuperar valor: {e}")

def consultarValorMulti(nomeValorChaveMulti):
    try:
        chaveRegistro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminhoChaveSubPasta, 0, winreg.KEY_READ)
        
        # Recupera o valor da chave
        valores, tipo = winreg.QueryValueEx(chaveRegistro, "txtListaTemasPadroes")
        
        winreg.CloseKey(chaveRegistro)
        
        # Exibe os valores recuperados
        print(f"Valores recuperados: {valores}")
    except Exception as e:
        print(f"Erro ao recuperar valores: {e}")

criarNovaChave(caminhoChaveBase)
criarNovaChave(caminhoChaveSubPasta)
adicionarValorSimples(nomeValorChave, valorChave)
adicionarValorMulti(nomeValorChaveMulti, valorChaveMulti)
atualizarValor(nomeValorChave, novoValor)
consultarValorSimples(nomeValorChave)
consultarValorMulti(nomeValorChaveMulti)