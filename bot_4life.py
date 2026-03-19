from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingResponse()
    msg = resp.message()

    if 'hola' in incoming_msg:
        msg.body("🔥 Hola! Soy tu asesor 4Life 💪\n\n✅ Mejora tu sistema inmune\n⚡ Más energía\n💰 Genera ingresos\n\n👉 ¿Qué te interesa?\n1. Salud\n2. Negocio")

    elif '1' in incoming_msg or 'salud' in incoming_msg:
        msg.body("💊 Perfecto 👍\nNuestros productos fortalecen tu sistema inmune.\n🔥 Producto estrella: Transfer Factor\n\n¿Quieres precio?")

    elif '2' in incoming_msg or 'negocio' in incoming_msg:
        msg.body("💰 Excelente 🔥\nCon 4Life puedes generar ingresos desde casa.\n\n¿Quieres empezar hoy?")

    elif 'precio' in incoming_msg:
        msg.body("💬 Claro 👍\nDime qué producto te interesa:\nTransfer Factor, Colágeno o Energía")

    elif 'comprar' in incoming_msg:
        msg.body("🛒 Perfecto 🔥\nEnvíame:\n👉 Nombre\n👉 Ciudad\n👉 Producto")

    else:
    msg.body("🤖 Escribe: hola, salud, negocio o comprar")

return str(resp)
