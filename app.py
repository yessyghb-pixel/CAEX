import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la plataforma
st.set_page_config(page_title="CAEX & Fresco Express OS", layout="wide")

# Estilo personalizado para mejorar la visualización
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Título y Logo (Simulado por las fuentes [1])
st.title("🚀 Centro de Control Operativo: CAEX & Fresco Express")
st.sidebar.image("https://via.placeholder.com/150", caption="Logotipo Corporativo")

# Menú Lateral - El Nuevo Organigrama [2]
menu = st.sidebar.selectbox("Módulo de Gestión", 
    ["Dashboard Gerencial (BCG)", "Ventas & SFA (Asistente 1)", "Compras & Proveedores (Asistente 2)", "WMS & Inventario (Logística)", "Tesorería Automatizada"])

# 1. DASHBOARD GERENCIAL (Mejora de reuniones mensuales [5, 6])
if menu == "Dashboard Gerencial (BCG)":
    st.header("📊 Inteligencia de Negocios")
    col1, col2, col3 = st.columns(3)
    col1.metric("Ventas Mes", "$45,200", "+12%")
    col2.metric("Eficiencia de Entrega", "94%", "+2%")
    col3.metric("Stock en Riesgo", "5 items", "-15%")

    st.subheader("Matriz BCG Dinámica (Rotación vs Rentabilidad)")
    # Simulación de datos de rotación [7]
    df_bcg = pd.DataFrame({
        'Producto': ['Queso Fresco', 'Yogurt 1L', 'Mantequilla', 'Leche Especial'],
        'Crecimiento': [2, 6, 8, 9],
        'Participación': [4],
        'Categoría': ['Estrella', 'Perro', 'Vaca', 'Incógnita']
    })
    fig = px.scatter(df_bcg, x="Participación", y="Crecimiento", text="Producto", color="Categoría", size_max=60)
    st.plotly_chart(fig, use_container_width=True)

# 2. VENTAS & SFA (Reemplazo de "Master Madre" y WhatsApp [10, 11])
elif menu == "Ventas & SFA (Asistente 1)":
    st.header("📱 Módulo de Ventas en Tiempo Real")
    with st.expander("Registrar Nuevo Pedido (SFA)"):
        vendedor = st.selectbox("Vendedor", ["Franck", "Jorge", "Manuel"])
        ruta = st.selectbox("Ruta/Unidad", ["VAN", "GACELA", "FURGON", "TRANSPORTE 1"])
        cliente = st.text_input("Nombre del Cliente")
        monto = st.number_input("Monto total", min_value=0.0)
        pago = st.radio("Método de Pago", ["Contado", "Billetera Digital", "Crédito (Firma)"])
        if st.button("Sincronizar Pedido"):
            st.success(f"Pedido de {cliente} enviado a Picking y registrado en la Nube.")

    st.subheader("Estado de Rutas actual")
    st.table(pd.DataFrame({
        'Unidad': ['VAN', 'GACELA', 'FURGON'],
        'Pedidos': [2-4],  # He añadido números de ejemplo aquí
        'Estado': ['En Ruta', 'Cargando', 'Finalizado'],
        'Monto': [2500.0, 1800.0, 1200.0]  # He añadido montos de ejemplo aquí
    }))

# 3. WMS & INVENTARIO (Control de Javas y Productos [14, 15])
elif menu == "WMS & Inventario (Logística)":
    st.header("📦 Warehouse Management System (WMS)")
    tab1, tab2 = st.tabs(["Control de Stock", "Préstamos de Activos (Javas/Pallets)"])
    
    with tab1:
        st.subheader("Inventario de Productos Dañados [14]")
        st.info("Escanee el código QR del producto para registrar merma.")
        st.data_editor(pd.DataFrame({
            'Producto': ['Queso', 'Yogurt'],
            'Stock Sistema': ,
            'Físico': ,
            'Diferencia': [0, -2]
        }))

    with tab2:
        st.subheader("Registro de Préstamos (Ever) [14, 16]")
        st.write("Vinculado automáticamente a la Nota de Venta de S/. 0.01")
        st.text_input("ID de Java/Pallet")
        st.date_input("Fecha de Retorno Programada")

# 4. TESORERÍA (Eliminación de validación manual de "pulgar arriba" [4, 11])
elif menu == "Tesorería Automatizada":
    st.header("💰 Conciliación Bancaria y Flujo de Caja")
    st.write("El sistema detecta automáticamente depósitos bancarios y los cruza con las facturas.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Pendientes de Cobro (Firmas) [9]")
        st.warning("Hay 3 facturas vencidas. Se ha enviado recordatorio automático a los vendedores.")
    
    with col_b:
        st.subheader("Cuadre del Día [4]")
        st.metric("Efectivo en Caja", "S/. 4,500", "Coincide con Sistema")

# Pie de página con acceso jerárquico [1, 2]
st.sidebar.markdown("---")
st.sidebar.write(f"Usuario: **Gerencia**")
st.sidebar.write("Nivel de Acceso: **Total**")
