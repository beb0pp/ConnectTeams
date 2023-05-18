#https://ativainvestimentos.webhook.office.com/webhookb2/fd047667-6a06-4149-bafc-1a6528f9baf7@974aa80e-fa9e-4278-a390-9064ec2f5050/IncomingWebhook/16ed76efa51a41ee96988bcfafde5be9/c427ccd7-2b82-4102-9f2e-69387a95c2c7
from fastapi import FastAPI, Request
from pymsteams import connectorcard

app = FastAPI()

webhook = 'https://ativainvestimentos.webhook.office.com/webhookb2/fd047667-6a06-4149-bafc-1a6528f9baf7@974aa80e-fa9e-4278-a390-9064ec2f5050/IncomingWebhook/16ed76efa51a41ee96988bcfafde5be9/c427ccd7-2b82-4102-9f2e-69387a95c2c7'

# Rota para receber as solicitações do Teams
@app.get("/teams/webhook")
async def teams_webhook(request: Request):
    data = await request.json()
    print("Dados recebidos:", data)

    # Processar a solicitação e responder ao Teams usando o pymsteams
    # Exemplo: enviar uma mensagem de confirmação de recebimento
    response_message = "Solicitação recebida com sucesso!"

    # Criar um novo card
    card = connectorcard.ConnectorCard()

    # Definir o texto da mensagem de resposta
    card.text(response_message)

    # Enviar a mensagem de resposta para o webhook do Teams
    card.send(data[f'{webhook}'])

    return {"message": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
