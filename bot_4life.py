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

    # SALUD (VENTA EMOCIONAL)
    elif '1' in incoming_msg or 'salud' in incoming_msg:
        msg.body(
            "💚 *SALUD 4LIFE*\n\n"
            "Nuestro producto estrella *Transfer Factor*:\n\n"
            "✅ Refuerza tu sistema inmune\n"
            "✅ Más energía diaria\n"
            "✅ Protección total\n\n"
            "🔥 RESULTADOS REALES desde la primera semana\n\n"
            "👉 Escribe *precio* para continuar"
        )

    # NEGOCIO (MENTALIDAD DINERO)
    elif '2' in incoming_msg or 'negocio' in incoming_msg:
        msg.body(
            "💰 *NEGOCIO 4LIFE*\n\n"
            "Genera ingresos desde casa:\n\n"
            "📈 Sistema probado\n"
            "🌍 Negocio internacional\n"
            "📲 Solo con tu celular\n\n"
            "🔥 Personas ya están ganando dinero\n\n"
            "👉 ¿Quieres empezar? Escribe *empezar*"
        )

    # PRECIOS (CIERRE)
    elif '3' in incoming_msg or 'precio' in incoming_msg:
        msg.body(
            "💲 *PRECIOS*\n\n"
            "🔥 Transfer Factor desde:\n"
            "👉 S/ XXX (coloca tu precio real)\n\n"
            "🎁 Promoción disponible HOY\n\n"
            "⚠️ Stock limitado\n\n"
            "👉 Escribe *comprar* para pedir ahora"
        )

    # COMPRA (CIERRE FINAL)
    elif '4' in incoming_msg or 'comprar' in incoming_msg:
        msg.body(
            "🛒 *COMPRA AHORA* 🔥\n\n"
            "Para procesar tu pedido envíame:\n\n"
            "👤 Nombre:\n"
            "📍 Ciudad:\n"
            "📦 Producto:\n\n"
            "Ejemplo:\n"
            "Juan - Lima - Transfer Factor\n\n"
            "💬 Te atenderé de inmediato"
        )

    # DETECTAR PEDIDO AUTOMÁTICO
    elif '-' in incoming_msg:
        with open("clientes.txt", "a") as f:
            f.write(f"{numero} - {incoming_msg}\n")

        msg.body(
            "✅ *PEDIDO RECIBIDO* 🔥\n\n"
            "📲 Te contactaremos en breve\n"
            "🚚 Envíos a todo el país\n\n"
            "🙏 Gracias por confiar en 4Life"
        )

    # FOLLOW-UP AUTOMÁTICO
    elif 'empezar' in incoming_msg:
        msg.body(
            "🚀 *EMPEZAR ES FÁCIL*\n\n"
            "Te guiaré paso a paso:\n\n"
            "1️⃣ Registro\n"
            "2️⃣ Activación\n"
            "3️⃣ Ventas\n\n"
            "💰 Puedes ganar desde el primer mes\n\n"
            "👉 ¿Quieres asesoría directa? Escribe *asesor*"
        )

    elif 'asesor' in incoming_msg:
        msg.body(
            "👨‍💼 Perfecto, un asesor te escribirá ahora mismo 📲\n\n"
            "🔥 Prepárate para comenzar tu negocio"
        )

    # RESPUESTA INTELIGENTE
    else:
        msg.body(
            "🤖 No entendí tu mensaje\n\n"
            "👉 Escribe *hola* para ver el menú"
        )

    return str(resp)

