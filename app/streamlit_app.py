import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Price Increase Risk Simulator",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Simulador de Incremento de Precio basado en Riesgo de Churn")

st.markdown("""
Esta app permite explorar distintos escenarios de incremento de precio y evaluar su impacto estimado sobre el riesgo de churn y el revenue esperado.
""")

# Datos de escenarios obtenidos del análisis
data = {
    "price_increase_pct": [0, 3, 5, 8, 10, 15],
    "avg_churn_risk": [26.6, 26.8, 26.9, 27.0, 27.1, 27.4],
    "expected_revenue": [316162, 324687, 330338, 338767, 344353, 358206],
    "high_risk_customers": [982, 1010, 1024, 1039, 1049, 1078]
}

scenario_df = pd.DataFrame(data)

st.sidebar.header("Configuración del escenario")

selected_increase = st.sidebar.selectbox(
    "Selecciona incremento de precio",
    scenario_df["price_increase_pct"].tolist(),
    format_func=lambda x: f"{x}%"
)

selected_row = scenario_df[
    scenario_df["price_increase_pct"] == selected_increase
].iloc[0]

baseline = scenario_df[scenario_df["price_increase_pct"] == 0].iloc[0]

incremental_revenue = selected_row["expected_revenue"] - \
    baseline["expected_revenue"]
churn_uplift = selected_row["avg_churn_risk"] - baseline["avg_churn_risk"]
additional_high_risk = selected_row["high_risk_customers"] - \
    baseline["high_risk_customers"]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Incremento de precio",
    f"{selected_row['price_increase_pct']}%"
)

col2.metric(
    "Riesgo promedio de churn",
    f"{selected_row['avg_churn_risk']:.1f}%",
    f"{churn_uplift:.1f} pp"
)

col3.metric(
    "Revenue esperado",
    f"${selected_row['expected_revenue']:,.0f}",
    f"${incremental_revenue:,.0f}"
)

col4.metric(
    "Clientes alto riesgo",
    f"{selected_row['high_risk_customers']:,.0f}",
    f"+{additional_high_risk:,.0f}"
)

st.subheader("Resultados por escenario")

st.dataframe(
    scenario_df.style.format({
        "avg_churn_risk": "{:.1f}%",
        "expected_revenue": "${:,.0f}",
        "high_risk_customers": "{:,.0f}"
    }),
    use_container_width=True
)

st.subheader("Revenue esperado por escenario")

st.line_chart(
    scenario_df.set_index("price_increase_pct")["expected_revenue"]
)

st.subheader("Riesgo promedio de churn por escenario")

st.line_chart(
    scenario_df.set_index("price_increase_pct")["avg_churn_risk"]
)

st.subheader("Recomendación ejecutiva")

if selected_increase >= 15:
    st.warning(
        "El escenario de 15% maximiza el revenue esperado, pero debe aplicarse de forma segmentada y validarse con pruebas controladas."
    )
elif selected_increase >= 8:
    st.info(
        "Este escenario muestra buen potencial de revenue con incremento moderado de riesgo. Recomendado para segmentos leales de bajo riesgo."
    )
elif selected_increase > 0:
    st.success(
        "Escenario conservador. Puede ser adecuado para una primera prueba con menor exposición al riesgo."
    )
else:
    st.info(
        "Escenario base sin incremento de precio."
    )

st.markdown("""
## Conclusión

Los aumentos de precio no deberían aplicarse de manera uniforme. La estrategia recomendada es priorizar segmentos leales con contratos de largo plazo y validar los incrementos mediante pruebas A/B o grupos de control.
""")
