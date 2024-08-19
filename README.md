# Scripts de Detecção Básicos - OpenCV + Mediapipe
Esse conjunto de scripts compõe um exemplo de uso dos sistema de detecção corporal e facial do Mediapipe usando OpenCV.

## Requisitos
* Python 3.x
* Mediapipe
* OpenCV

Você pode instalar as dependências necessárias com:
```bash
pip install -r requirements.txt
```

## Overview dos Scripts
1. **hand_detection.py:** Mostra apenas um exoesqueleto acima das mãos identificadas em vídeo;
2. **face_grid_detection:** Mostra uma malha de pontos e linhas em cima do rosto do usuário;
3. **body_stuff/body_detection:** Mostra uma malha de pontos e linhas em cima do corpo todo do usuário;
4. **body_stuff/body_counting:** Mostra a quantidade de corpos que passaram pela tela. Este script não possui nenhum tipo de lógica, então não diferencia corpos, apenas conta quantos passaram pela câmera em qualquer direção.
5. **body_stuff/body_alert:** Script mostra um alerta na tela caso um corpo seja detectado na direta da área da câmera.

## Como usar
1. **Endereçamento da Câmera:** Todos os scripts são de fácil execução, a única mudança (talvez) necessária é o endereçamento da câmera usada.

A linha para isso se parece com esta em todos os scripts:
```python
cap = cv2.VideoCapture(0)
```
Se estiver em um notebook, "0" é o endereço da câmera imbutida do aparelho. Se outra câmera for usada, o endereço dela pode mudar para "1" (ou "2" ou "3"...)

2. **Configurar Tradução Geral:** O retorno textual do sistema está em inglês, mas esse texto pode ser facilmente traduzido caso necessário.

Dicas como essa estão espalhadas pelo código:
```python
# -- you can translate the text right here:
        cv2.putText(image, f'Counting: {body_count}',
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 0),
                    2,
                    cv2.LINE_AA)
```
        
2. **Executar o Script:** Conecte sua câmera e execute o script com o comando:
```bash
python nome_do_arquivo.py
```

3. **Interagir com a Janela**: O vídeo da câmera será exibido em uma janela chamada "Window".

4. **Finalizar:** Para parar a execução do script, pressione a tecla 'k'.

## Licença
Este projeto é distribuído sob a [Licença MIT](LICENSE).