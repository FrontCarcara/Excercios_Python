import pywin32
import win32print

def configurar_impressora(nome_impressora, driver):
    # Obtém a lista de impressoras disponíveis
    impressoras = [printer[2] for printer in win32print.EnumPrinters(2)]

    # Verifica se a impressora desejada já está instalada
    if nome_impressora in impressoras:
        print(f"A impressora '{nome_impressora}' já está instalada.")
        return

    # Configura a impressora com o driver especificado
    try:
        win32print.AddPrinter(nome_impressora, 2, driver)
        print(f"Impressora '{nome_impressora}' configurada com sucesso.")
    except Exception as e:
        print(f"Erro ao configurar a impressora: {e}")

if __name__ == "__main__":
    # Substitua 'NomeDaImpressora' pelo nome da sua impressora e 'NomeDoDriver' pelo nome do driver
    configurar_impressora('NomeDaImpressora', 'NomeDoDriver')
