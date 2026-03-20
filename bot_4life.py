from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    numero = request.values.get('From', '')

    resp = MessagingResponse()
    msg = resp.message()

    # MENÚ PRINCIPAL
    if incoming_msg in ['hola', 'menu', 'inicio']:
        msg.body(
            "🔥 Hola! Soy tu asesor 4Life 💪\n\n"
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
    elif incoming_msg == '1' or 'salud' in incoming_msg:
        msg.body(
            "💚 *SALUD 4LIFE*\n\n"
            "Nuestro producto estrella *Transfer Factor*:\n\n"
            "✅ Refuerza tu sistema inmune\n"
            "✅ Más energía diaria\n"
            "✅ Protección total\n\n"
            "🔥 RESULTADOS REALES\n\n"
            "👉 Escribe *3* para ver precios"
        )

    # NEGOCIO
    elif incoming_msg == '2' or 'negocio' in incoming_msg:
        msg.body(
            "💰 *NEGOCIO 4LIFE*\n\n"
            "Genera ingresos desde casa:\n\n"
            "📈 Sistema probado\n"
            "🌍 Negocio internacional\n"
            "📲 Solo con tu celular\n\n"
            "🔥 Personas ya están ganando dinero\n\n"
            "👉 Escribe *empezar*"
        )

    # PRECIOS
    elif incoming_msg == '3' or 'precio' in incoming_msg:
        msg.body(
            "💲 *PRECIOS*\n\n"
            "🔥 Transfer Factor desde:\n"
            "👉 S/ 150 (ejemplo)\n\n"
            "🎁 Promoción disponible HOY\n\n"
            "👉 Escribe *4* para comprar"
        )

    # COMPRA
    elif incoming_msg == '4' or 'comprar' in incoming_msg:
        msg.body(
            "🛒 *COMPRA AHORA* 🔥\n\n"
            "Envíame:\n\n"
            "👤 Nombre - Ciudad - Producto\n\n"
            "Ejemplo:\n"
            "Juan - Lima - Transfer Factor"
        )

    # GUARDAR CLIENTE
    elif '-' in incoming_msg:
        print(f"CLIENTE: {numero} - {incoming_msg}")

        msg.body(
            "✅ *PEDIDO RECIBIDO* 🔥\n\n"
            "📲 Te escribiremos en breve\n"
            "🚚 Envíos a todo el Perú\n\n"
            "🙏 Gracias por confiar"
        )

    # FOLLOW-UP
    elif 'empezar' in incoming_msg:
        msg.body(
            "🚀 *EMPEZAR ES FÁCIL*\n\n"
            "1️⃣ Registro\n"
            "2️⃣ Activación\n"
            "3️⃣ Ganancias\n\n"
            "💰 Puedes iniciar hoy mismo\n\n"
            "👉 Escribe *asesor*"
        )

    elif 'asesor' in incoming_msg:
        msg.body(
            "👨‍💼 Un asesor te contactará ahora 📲\n\n"
            "🔥 Prepárate para crecer"
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
