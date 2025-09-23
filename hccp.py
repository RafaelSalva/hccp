import re
from datetime import datetime, timedelta


class Produto:
    def __init__(self, nome=None, armazenamento=None, exposto=None, obs=None):
        self.nome = nome
        self.exposto = exposto
        self.armazenamento = armazenamento
        self.obs = obs

    def vizualizar(self):
        print(f'''
        ------------------
             PRODUTO
        NOME:{self.nome}
        VALIDADE EXPOSTO:{self.exposto}
        VALIDADE ARMAZENAMENTO: {self.armazenamento}
        OBS: {self.obs}
        ------------------''')

    def pesquisar(self, lista):
        exibir = input('Digite o nome do produto: ')
        for obj in lista:
            if exibir.lower() == obj.nome.lower():
                obj.vizualizar()

    def vizualizar_hccp(self):
        print(f'''
        ------------------
        VALIDADE HCCP:
        PRODUTO:{self.nome}
        LOTE: {self.lote}
        EXPOSTO:{self.agora.strftime('Data: %d/%m/%y|| Hora: %H:%M')}
        VALIDADE:{self.validade.strftime('Data: %d/%m/%y|| Hora: %H:%M')}
        OBS: {self.obs}
        ------------------''')

    def hccp(self, lista):
        while True:
            artigo = input('Digite o nome do produto: ')
            self.lote = input('Digite o lote: ')
            self.agora = datetime.now()

            for obj in lista:
                if artigo.lower() == obj.nome.lower():
                    texto = obj.exposto.lower()

                    # procurar números no texto
                    dias = re.search(r"(\d+)\s*dias?", texto)
                    horas = re.search(r"(\d+)\s*horas?", texto)

                    self.validade = None

                    self.nome = obj.nome
                    self.obs = obj.obs

                    if "produto do dia" in texto:
                        # até o final do dia de hoje
                        self.validade = datetime(self.agora.year, self.agora.month, self.agora.day, 23, 59, 59)
                        self.vizualizar_hccp()

                    elif dias:
                        self.validade = self.agora + timedelta(days=int(dias.group(1)))
                        self.vizualizar_hccp()

                    elif horas:
                        self.validade = self.agora + timedelta(hours=int(horas.group(1)))
                        self.vizualizar_hccp()

            continuar = input('''
            Deseja gerar outra validade HCCP?
            A- Sim
            B- Não''')
            if continuar.lower() == 'b':
                break

    def programa(self):
        print('''
        -------------------------
        VALIDADES HCCP DOS FRECOS
        -------------------------''')
        while True:
            opcao = input(''''
            A - CONSULTAR VALIDADE
            B - GERAR VALIDADE 
            C - SAIR
            ''')

            if opcao.lower() == 'a':
                self.pesquisar(produtos)

            elif opcao.lower() == 'b':
                self.hccp(produtos)

            elif opcao.lower() == 'c':
                break


produtos = [
    Produto("Cubos de Atum", "10 dias", "produto do dia", "Conservar refrigerado"),
    Produto(
        "Espetadas de Salmão / Espetadas de Espadarte Preto, Pota e Salmão, Salmão e Atum, Lulas com Camarão e Pota",
        "10 dias", "produto do dia", "Conservar refrigerado"),
    Produto("Filetes de Dourada / Robalo / Bacalhau", "15 dias", "24 horas", "Conservar refrigerado"),
    Produto("Filete de Corvina", "15 dias", "24 horas", "Conservar refrigerado"),
    Produto("Filete de Peixe Espada Preto", "15 dias", "36 horas", "Conservar refrigerado"),
    Produto("Filete de Redfish descongelado", "15 dias", "36 horas", "Conservar refrigerado"),
    Produto("Lagosta Cozida", "15 dias", "produto do dia", "Conservar refrigerado")]

executar = Produto()

executar.programa()
