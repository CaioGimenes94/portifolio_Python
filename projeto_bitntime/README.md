# BiTnTime

**BiTnTime** é um projeto que monitora o valor do Bitcoin em tempo real e alerta o usuário sobre variações significativas. A ideia é fornecer uma maneira simples e eficaz de acompanhar o mercado de criptomoedas diretamente no seu dispositivo.

## Funcionalidades

- **Monitoramento do Bitcoin**: O valor do Bitcoin é atualizado em tempo real com um intervalo de consulta de até 30 segundos.
- **Alertas**: O usuário pode configurar uma variação percentual para receber notificações quando o valor do Bitcoin atingir esse limite.
- **Interface Web (Futura Implementação)**: O projeto está em andamento para ser acessado através de um site.

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para o processamento e consulta da API.
- **Flask**: Framework para construir a interface web (a ser implementada).
- **API de Criptomoedas**: Utilizada para obter os dados em tempo real sobre o valor do Bitcoin.
- **HTML/CSS**: Para a criação da interface do usuário.

## Estrutura do Projeto

```plaintext
projeto_bitcoin/
├── app/
│   ├── __init__.py
│   ├── api_handler.py
│   ├── price_monitor.py
├── static/
│   └── (arquivos CSS, JS)
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
└── README.md
```

## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/CaioGimenes94/portifolio_Python.git
   cd portifolio_Python/projeto_bitntime
   
2. **Instale as dependências:** Certifique-se de ter o Python instalado. Depois, instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   
3. **Execute o script:** Navegue até a pasta onde o arquivo main.py está localizado e execute o seguinte comando:
   ```bash
   cd projeto_bitntime
   python main.py
 
4. **Configuração de alertas:** O usuário pode configurar o alerta de variação percentual diretamente no código ou implementações futuras permitirão uma interface para isso.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
