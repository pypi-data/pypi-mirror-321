# Camalis Python Lib

## Sobre a biblioteca

- A Camalis Python Lib é uma biblioteca Python que permite que o usuário interaja com o Camalis.

## Instalação da biblioteca

Para instalar a biblioteca, use o comando abaixo:

```python
pip install camalis
```

## Como usar ?

Fora do ambiente do Camalis a biblioteca necessita de alguns parâmetros no seu metodo construtor:

```python
from camalis import Camalis
camalis = Camalis(api_url="endereco-da-api", token="token-de-integracao-do-usuario")
```

## Principais comandos:

- Carregar variável:

```python camalis.variable.get(path="path-da-variavel") ``` 

Esse método permite que o usuário possa carregar na instância uma única variável. Uma vez carregado a variável o usuário poderá solicitar um snapshot (último valor disponível na variável) ou um histórico.

- Snapshot

```python 
from camalis import Camalis
camalis = Camalis(api_url="endereco-da-api", token="token-de-integracao-do-usuario")

tempo = camalis.variable.get(path='GERAL/LITERAL/PRODUTOR/TEMPO')

print(tempo.snapshot())
```

- Histórico:

```python 
from camalis import Camalis
camalis = Camalis(api_url="endereco-da-api", token="token-de-integracao-do-usuario")

tempo = camalis.variable.get(path='GERAL/LITERAL/PRODUTOR/TEMPO')

start_date = datetime.now(timezone.utc)
end_date = start_date + timedelta(days=6)

print(tempo.historic(start_time=start_date, end_time=end_date))
```

- Escrever variável especialista:

Com o Camalis Python Lib o usuário também poderá efetuar a escrita do valor em uma variável especialista.

```python 
import random
from datetime import datetime, timezone
from camalis import Camalis

camalis = Camalis(api_url="endereco-da-api", token="token-de-integracao-do-usuario")
variaveis = camalis.variable.list(path='GERAL/LITERAL/PRODUTOR/RISCO_EXPLOSAO')
variavel1 = variaveis[0]
timestamp = datetime.now(timezone.utc)

variavel1.write(random.randint(0, 100), timestamp)

print(variavel1.snapshot())
```