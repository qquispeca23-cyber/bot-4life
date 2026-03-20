from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from datetime import datetime

app = Flask(__name__)

def guardar_cliente(numero, mensaje):
    with open("clientes.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {numero} | {mensaje}\n")

@app.route("/whatsapp", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    numero = request.values.get('From', '')

    resp = MessagingResponse()
    msg = resp.message()

    # MENÚ PRINCIPAL
    if incoming_msg in ['hola', 'menu', 'inicio']:
        msg.body(
            "🔥 *BIENVENIDO AL SISTEMA 4LIFE* 💪\n\n"
            "💚 Mejora tu salud\n"
            "⚡ Aumenta tu energía\n"
            "💰 Genera ingresos\n\n"
            "👉 Elige una opción:\n"
            "1️⃣ Salud\n"
            "2️⃣ Negocio\n"
            "3️⃣ Precios\n"
            "4️⃣ Comprar"
        )

    # SALUD
    elif incoming_msg in ['1', 'salud']:
        msg.body(
            "💚 *SALUD 4LIFE*\n\n"
            "Transfer Factor:\n\n"
            "✅ Refuerza tu sistema inmune\n"
            "✅ Más energía diaria\n"
            "✅ Mejor calidad de vida\n\n"
            "🔥 RESULTADOS REALES\n\n"
            "👉 Escribe *3* para ver precios"
        )
        msg.media("https://i.imgur.com/8Km9tLL.jpg")  # cambia por tu imagen

    # NEGOCIO
    elif incoming_msg in ['2', 'negocio']:
        msg.body(
            "💰 *NEGOCIO 4LIFE*\n\n"
            "Gana dinero desde casa:\n\n"
            "📈 Sistema probado\n"
            "🌍 Negocio internacional\n"
            "📲 Solo con tu celular\n\n"
            "👉 Escribe *empezar*"
        )

    # PRECIOS
    elif incoming_msg in ['3', 'precio', 'precios']:
        msg.body(
            "💲 *PROMOCIÓN HOY* 🔥\n\n"
            "Transfer Factor desde:\n"
            "👉 S/ 290\n\n"
            "🎁 Bonos incluidos HOY\n\n"
            "👉 Escribe *4* para comprar"
        )

    # COMPRA
    elif incoming_msg in ['4', 'comprar']:
        msg.body(
            "🛒 *COMPRA AHORA* 🔥\n\n"
            "Envíame:\n\n"
            "👤 Nombre - Ciudad - Producto\n\n"
            "Ejemplo:\n"
            "Juan - Lima - Transfer Factor"
        )

    # GUARDAR CLIENTE
    elif '-' in incoming_msg and len(incoming_msg.split('-')) >= 3:
        guardar_cliente(numero, incoming_msg)

        msg.body(
            "✅ *PEDIDO CONFIRMADO* 🔥\n\n"
            "📲 Un asesor te escribirá en breve\n"
            "🚚 Envíos a todo el Perú\n\n"
            "🙏 Gracias por confiar en 4Life"
        )

    # FOLLOW-UP
    elif incoming_msg == 'empezar':
        msg.body(
            "🚀 *EMPEZAR ES FÁCIL*\n\n"
            "1️⃣ Registro\n"
            "2️⃣ Activación\n"
            "3️⃣ Ganancias\n\n"
            "👉 Escribe *asesor*"
        )

    elif incoming_msg == 'asesor':
        msg.body(
            "👨‍💼 Un asesor te contactará ahora 📲\n\n"
            "🔥 Prepárate para crecer"
        )

    elif incoming_msg == 'quiero':
        msg.body(
            "🔥 Excelente decisión\n\n"
            "📲 Te escribiré personalmente para ayudarte\n"
            "💰 Hoy puedes empezar\n\n"
            "👉 Mantente atento"
        )

    # DEFAULT
    else:
        msg.body(
            "🤖 No entendí tu mensaje\n\n"
            "👉 Escribe *hola* para iniciar"
        )

    return str(resp)

@app.route("/")
def home():
    return "BOT ACTIVO 4LIFE 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
