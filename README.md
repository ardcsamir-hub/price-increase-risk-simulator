# Simulador de Incremento de Precio basado en Riesgo de Churn

## Problema de negocio

Las empresas suelen necesitar aumentar precios para mejorar ingresos, pero aplicar el mismo aumento a todos los clientes puede elevar el riesgo de deserción. Este proyecto simula distintos escenarios de incremento de precio e identifica qué segmentos de clientes podrían tolerar aumentos con menor riesgo de churn.

## Objetivo

Construir un simulador de pricing basado en un modelo de churn para estimar el impacto de distintos aumentos de precio sobre el riesgo de deserción y el revenue esperado.

## Dataset

Se utilizó el dataset **Telco Customer Churn**.

Variables principales utilizadas:

- Antigüedad del cliente
- Cargo mensual
- Cargo total acumulado
- Tipo de contrato
- Método de pago
- Servicio de internet
- Soporte técnico
- Churn

## Metodología

1. Limpieza y preparación de datos.
2. Análisis exploratorio de churn.
3. Segmentación de clientes por precio y antigüedad.
4. Entrenamiento de un modelo de churn con Regresión Logística.
5. Simulación de incrementos de precio entre 0% y 15%.
6. Recomendaciones de pricing por segmento.

## Herramientas utilizadas

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- Jupyter Notebook

## Entregables principales

- Modelo predictivo de churn.
- Simulación de escenarios de incremento de precio.
- Recomendaciones de pricing por segmento.
- Conclusiones ejecutivas orientadas a negocio.

## Resultados principales

El simulador evaluó escenarios de incremento de precio desde 0% hasta 15%.

| Incremento de precio | Riesgo promedio de churn | Revenue esperado | Clientes de alto riesgo |
|---:|---:|---:|---:|
| 0% | 26.6% | $316,162 | 982 |
| 3% | 26.8% | $324,687 | 1,010 |
| 5% | 26.9% | $330,338 | 1,024 |
| 8% | 27.0% | $338,767 | 1,039 |
| 10% | 27.1% | $344,353 | 1,049 |
| 15% | 27.4% | $358,206 | 1,078 |

## Mejor escenario simulado

El escenario con incremento de precio del **15%** generó el mayor revenue esperado:

- Revenue esperado: **$358,206**
- Revenue incremental vs. escenario base: **$42,044**
- Riesgo promedio de churn: **27.4%**
- Incremento del riesgo de churn vs. escenario base: **+0.8 puntos porcentuales**
- Clientes adicionales en alto riesgo: **+96**

## Hallazgos por segmento

Los mejores candidatos para incremento de precio fueron clientes leales con contratos de uno o dos años, especialmente aquellos con bajo riesgo estimado de churn.

Ejemplos de segmentos con bajo riesgo identificados por el simulador:

| Contrato | Segmento de antigüedad | Segmento de precio | Servicio de internet | Clientes | Riesgo promedio de churn | Incremento de precio | Recomendación |
|---|---|---|---|---:|---:|---:|---|
| Two year | Loyal | High price | Fiber optic | 386 | 7.4% | 15% | Aplicar aumento |
| Two year | Loyal | Mid-high price | DSL | 270 | 2.1% | 15% | Aplicar aumento |
| Two year | Loyal | Mid-low price | DSL | 244 | 1.5% | 15% | Aplicar aumento |
| Two year | Loyal | Low price | No | 463 | 0.5% | 15% | Aplicar aumento |
| One year | Loyal | High price | Fiber optic | 383 | 19.1% | 15% | Aplicar aumento |

## Recomendación de negocio

El análisis sugiere que los aumentos de precio no deberían aplicarse de manera uniforme a toda la base de clientes.

Los clientes leales con contratos de uno o dos años presentan menor riesgo de churn y son mejores candidatos para aumentos de precio más altos. En cambio, los clientes nuevos y los clientes con contratos mensuales deberían tratarse con mayor cautela, utilizando grupos de control, pruebas A/B o acciones de retención antes de aplicar incrementos agresivos.

La estrategia recomendada es priorizar aumentos en segmentos leales de bajo riesgo y probar aumentos moderados en segmentos de riesgo medio.

## Estructura del repositorio

price-increase-risk-simulator/
│
├── data/
├── notebooks/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore

## Desempeño del modelo
```text
El modelo de churn fue entrenado usando Regresión Logística. La métrica principal utilizada fue ROC AUC, ya que permite evaluar la capacidad del modelo para diferenciar entre clientes que desertan y clientes que permanecen.

- Modelo: Regresión Logística
- Métrica principal: ROC AUC
- ROC AUC obtenido: X.XX