from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    numero = request.values.get('From', '')

    resp = MessagingResponse()
    msg = resp.message()

    # MENÚ PRINCIPAL
    if 'hola' in incoming_msg:
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

    # OPCIÓN SALUD
    elif incoming_msg == '1' or 'salud' in incoming_msg:
        msg.body(
            "💊 SALUD 4LIFE\n\n"
            "🔥 Transfer Factor fortalece tu sistema inmune\n"
            "⚡ Más energía diaria\n"
            "🛡️ Mayor protección\n\n"
            "👉 Escribe 3 para ver precios\n"
            "👉 Escribe 4 para comprar"
        )

    # OPCIÓN NEGOCIO
    elif incoming_msg == '2' or 'negocio' in incoming_msg:
        msg.body(
            "💰 NEGOCIO 4LIFE\n\n"
            "🚀 Gana dinero desde casa\n"
            "📈 Sin experiencia\n"
            "🌎 Negocio internacional\n\n"
            "👉 ¿Quieres empezar?\n"
            "Escribe: empezar"
        )

    # PRECIOS
    elif incoming_msg == '3' or 'precio' in incoming_msg:
        msg.body(
            "💵 PRECIOS\n\n"
            "🔹 Transfer Factor: Consultar\n"
            "🔹 Colágeno: Consultar\n"
            "🔹 Energía: Consultar\n\n"
            "🔥 Promoción disponible hoy\n\n"
            "👉 Escribe 4 para comprar"
        )

    # COMPRAR
    elif incoming_msg == '4' or 'comprar' in incoming_msg:
        msg.body(
            "🛒 COMPRA AHORA 🔥\n\n"
            "Envíame tus datos así:\n\n"
            "Nombre - Ciudad - Producto"
        )

    # GUARDAR CLIENTES
    elif '-' in incoming_msg:
        with open("clientes.txt", "a") as f:
            f.write(f"{numero} - {incoming_msg}\n")

        msg.body(
            "✅ Pedido recibido 🔥\n\n"
            "📞 Te contactaremos pronto\n"
            "🚀 Gracias por confiar en 4Life"
        )

    # RESPUESTA POR DEFECTO
    else:
        msg.body(
            "🤖 No entendí tu mensaje\n\n"
            "👉 Escribe 'hola' para ver el menú"
        )

    return str(resp)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


