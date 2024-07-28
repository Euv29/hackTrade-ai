# HACKTRADE AI

Este é um projeto de Trading Dashboard que utiliza TensorTrade para criar uma inteligência artificial que analisa gráficos junto com a API da Binance. Ele fornece análises em tempo real, sinais de compra ou venda, bem como informações sobre o ativo, timeframe e horário, exibidos em uma página HTML.

## Estrutura do Projeto

    trading-project/
    │
    ├── binance_data.py # Script para coletar dados da Binance
    ├── trading_env.py # Script para configurar o ambiente de trading e treinar o modelo
    ├── app.py # Backend Flask para servir a API e a página HTML
    ├── models/ # Diretório para armazenar modelos treinados
    │   └── trading_model.zip # Modelo treinado pelo TensorTrade
    │
    ├── templates/ # Diretório para arquivos HTML
    │   └── index.html # Página HTML para exibir gráficos e sinais
    │
    ├── static/ # Diretório para arquivos estáticos (CSS, JS, imagens)
    │   ├── css/
    │   │   └── styles.css # Arquivo CSS para estilos
    │   └── js/
    │       └── main.js # (Opcional) Arquivo JavaScript separado se necessário
    │
    ├── requirements.txt # Arquivo com lista de dependências
    └── README.md # Arquivo de documentação do projeto.

## Requisitos

- Python 3.6 ou superior
- pip

## Instalação

1. **Faça o Fork e Clone o repositório:**

```bash
git clone git@github.com:username/hackTrade-ai.git
cd hackTrade-ai
```
Certifique-se de substituir `username` pelo seu nome de usuário no GitHub.

2. **Crie e ative um ambiente virtual:**

```python
python -m venv trading-env
```

```
source trading-env/bin/activate  # Para Linux/Mac
trading-env\Scripts\activate  # Para Windows
```
Use este comando no terminal para ativar o ambiente virtual no Linux ou Mac. No Windows, use `trading-env\Scripts\activate`.

3. **Instale as dependências:**

```pip
pip install -r requirements.txt
```
Este comando instalará todas as dependências necessárias listadas no arquivo `requirements.txt`.

## Coletar Dados e Treinar o Modelo

1. **Coletar dados da Binance:**

O script **'binance_data.py'** coleta dados históricos da Binance. Certifique-se de que está configurado corretamente para o ativo e timeframe desejados.

2. **Treinar o modelo**

Execute o script **'trading_env.py'** para configurar o ambiente de trading e treinar o modelo:

```python
python trading_env.py
```

Isso criará e salvará o modelo treinado no diretório **'models/'**.

## Executar o Servidor

1. **Inicie o servidor Flask:**

```python
python app.py
```

2. **Acesse a aplicação:**

Abra o navegador e vá para <http://localhost:5000> para ver o dashboard de trading.

## Estrutura de Arquivos

1. binance_data.py: Script para coletar dados históricos da Binance.
2. trading_env.py: Script para configurar o ambiente de trading com TensorTrade e treinar o modelo.
3. app.py: Script principal do Flask que serve a API e a página HTML.
4. models/: Diretório para armazenar modelos treinados.
5. templates/index.html: Página HTML para exibir gráficos e sinais de trading.
6. static/css/styles.css: Arquivo CSS para estilos.
7. requirements.txt: Arquivo que lista todas as dependências do projeto.

## Funcionalidades

1. Análise em Tempo Real: A IA analisa gráficos em tempo real usando dados da Binance.
2. Sinais de Trading: Fornece sinais de compra ou venda baseados em aprendizado por reforço.
3. Dashboard Interativo: Exibe gráficos de preços e sinais de trading em uma página HTML.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
4. Faça push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença `MIT` - veja o arquivo LICENSE para detalhes.

Este `README` cobre os principais aspectos do seu projeto, desde a instalação e configuração até a execução e contribuição. Sinta-se à vontade para ajustá-lo conforme necessário para melhor se adequar ao seu projeto e suas necessidades.
