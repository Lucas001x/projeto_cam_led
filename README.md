# projeto_cam_led

**Descrição do Projeto: HandConnectCtrl com Arduino**

Este projeto utiliza a biblioteca `cvzone` para rastrear as mãos em tempo real por meio da webcam, identificando movimentos específicos dos dedos. A aplicação interage com um dispositivo Arduino, enviando comandos com base nos gestos detectados.

**Recursos e Funcionalidades:**
- Rastreamento de mãos em tempo real.
- Contagem de dedos levantados e identificação de gestos.
- Integração com Arduino para controle de dispositivos ou aplicações.

**Instruções de Uso:**
1. Instale as dependências utilizando `pip install -r requirements.txt`.
2. Conecte o Arduino e ajuste a porta no script (`port='COM12'`).
3. Execute o script Python para iniciar o rastreamento.

**Requisitos:**
- Python 3.x
- Bibliotecas: cv2, cvzone, numpy, serial

**Exemplo de Aplicação:**
- Controle remoto utilizando gestos para manipular dispositivos ou aplicações.

**Observações:**
- Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o script.
- Ajuste a porta do Arduino de acordo com a configuração do seu sistema.

**Autor:**
LUCAS CESAR DE ARRUDA

**Contribuições:**
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.
