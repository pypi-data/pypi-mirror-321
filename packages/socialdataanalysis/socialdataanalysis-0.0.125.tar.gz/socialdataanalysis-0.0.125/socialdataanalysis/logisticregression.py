import pandas as pd
import numpy as np
import statsmodels.api as sm
from tabulate import tabulate
from scipy import stats
from scipy.stats import norm
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, auc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import itertools
from statsmodels.formula.api import glm
from scipy.stats import chi2, norm

def analyze_glm_binomial(df, dependent_var, independent_vars):
    """
    Ajusta um modelo GLM binomial (logístico) a partir de um DataFrame, exibindo medidas de ajuste,
    testes do modelo e estimativas dos parâmetros.

    Parâmetros:
    - df: DataFrame com dados
    - dependent_var: Nome da variável dependente (binária, 0/1)
    - independent_vars: Lista de nomes de variáveis independentes

    A função valida a existência das variáveis, ajusta o modelo completo,
    realiza testes (Omnibus, LR de efeito), gera tabelas de ajuste e estimativas.
    """

    # Validação das variáveis
    all_vars = [dependent_var] + independent_vars
    for var in all_vars:
        if var not in df.columns:
            raise ValueError(f"A variável '{var}' não existe no DataFrame.")

    # Agrupar os dados pelas variáveis independentes e contar sucessos e fracassos
    grouped = df.groupby(independent_vars)[dependent_var].agg(['sum', 'count']).reset_index()
    grouped.columns = independent_vars + ['Success', 'Total']
    grouped['Failure'] = grouped['Total'] - grouped['Success']

    n_groups = len(grouped)
    n_total = df.shape[0]

    # Preparar as matrizes de design
    X_full = grouped[independent_vars]
    y = grouped[['Success', 'Failure']]
    X_full = sm.add_constant(X_full)

    # Ajustar o modelo completo
    model_full = sm.GLM(y, X_full, family=sm.families.Binomial())
    result_full = model_full.fit()
    deviance_full = result_full.deviance
    df_resid = result_full.df_resid
    df_model = result_full.df_model
    k = len(result_full.params)
    pearson_chi2 = np.sum(result_full.resid_pearson**2)
    log_likelihood_full = result_full.llf

    # Critérios de informação
    aic = -2 * log_likelihood_full + 2 * k
    bic = -2 * log_likelihood_full + k * np.log(n_total)
    AICc = aic + (2 * k * (k + 1)) / (n_total - k - 1)
    CAIC = aic + (np.log(n_total) + 1) * k

    # Estimação do parâmetro de escala (usando a deviance)
    scale = deviance_full / df_resid  # Método da Deviance

    # Ajuste dos erros padrão
    adjusted_bse = result_full.bse * np.sqrt(scale)

    # Recalcular Wald Chi-Quadrado e p-valores com os erros padrão ajustados
    wald_chi2 = (result_full.params / adjusted_bse) ** 2
    p_values = 1 - stats.chi2.cdf(wald_chi2, df=1)
    wald_chi2 = pd.Series(wald_chi2, index=result_full.params.index)
    p_values = pd.Series(p_values, index=result_full.params.index)

    # Testes tipo III (Likelihood Ratio) para cada parâmetro
    LR_stats = {}
    p_values_lr = {}
    for var in ['const'] + independent_vars:
        if var == 'const':
            # Modelo sem intercepto
            X_reduced = grouped[independent_vars]  # sem adicionar constante
        else:
            # Modelo sem a variável atual
            vars_reduced = [v for v in independent_vars if v != var]
            X_reduced = grouped[vars_reduced]
            X_reduced = sm.add_constant(X_reduced)

        model_reduced = sm.GLM(y, X_reduced, family=sm.families.Binomial())
        result_reduced = model_reduced.fit()
        deviance_reduced = result_reduced.deviance
        LR_stat = (deviance_reduced - deviance_full) / scale
        p_value_lr = 1 - stats.chi2.cdf(LR_stat, df=1)
        LR_stats[var] = LR_stat
        p_values_lr[var] = p_value_lr

    # Funções auxiliares de formatação
    def format_number(x):
        if isinstance(x, (int, float, np.float64, np.int64)):
            return f"{x:.3f}"
        else:
            return x

    def format_p_value(p):
        return "<0.001" if p < 0.001 else f"{p:.3f}"

    def create_goodness_of_fit_table():
        """
        Cria e exibe a tabela de "Goodness of Fit" com notas explicativas.
        """
        def add_superscript(text, superscripts):
            return f"{text}^{superscripts}"

        title = add_superscript('Goodness of Fit', 'a,b,c,d')
        log_likelihood_label = add_superscript('Log Likelihood', 'b,c')
        adjusted_log_likelihood_label = add_superscript('Adjusted Log Likelihood', 'd')

        # Usar escala fixa em 1 para Scaled Deviance (opcional)
        scale_fixed = 1
        scaled_deviance = df_resid * scale_fixed
        # Scaled Pearson: relação do Pearson Chi2 com a deviance
        scaled_pearson_chi2 = pearson_chi2 * (df_resid / deviance_full)

        adjusted_log_likelihood = -0.5 * scaled_deviance

        table = [
            ['Deviance', deviance_full, df_resid, deviance_full / df_resid],
            ['Scaled Deviance', scaled_deviance, df_resid, ''],
            ['Pearson Chi-Square', pearson_chi2, df_resid, pearson_chi2 / df_resid],
            ['Scaled Pearson Chi-Square', scaled_pearson_chi2, df_resid, ''],
            [log_likelihood_label, log_likelihood_full, '', ''],
            [adjusted_log_likelihood_label, adjusted_log_likelihood, '', ''],
            ["Akaike's Information Criterion (AIC)", aic, '', ''],
            ['Finite Sample Corrected AIC (AICc)', AICc, '', ''],
            ['Bayesian Information Criterion (BIC)', bic, '', ''],
            ['Consistent AIC (CAIC)', CAIC, '', '']
        ]
        headers = [title, 'Value', 'df', 'Value/df']

        formatted_table = []
        for row in table:
            formatted_row = [row[0]] + [format_number(x) for x in row[1:]]
            formatted_table.append(formatted_row)

        print(tabulate(formatted_table, headers=headers))

        footnotes = [
            "a. Information criteria are in smaller-is-better form.",
            "b. The full log likelihood function is displayed and used in computing information criteria.",
            "c. The log likelihood is based on a scale parameter fixed at 1.",
            "d. The adjusted log likelihood is based on the residual deviance and dispersion scaling."
        ]
        print('\n' + '\n'.join(footnotes))

    def create_omnibus_test_table():
        """
        Cria e exibe a tabela do teste Omnibus, comparando o modelo completo com o modelo nulo.
        """
        X_null = pd.DataFrame({'const': np.ones(grouped.shape[0])})
        model_null = sm.GLM(y, X_null, family=sm.families.Binomial())
        result_null = model_null.fit()
        deviance_null = result_null.deviance

        LR_stat_omnibus = (deviance_null - deviance_full) / scale
        p_value_omnibus = 1 - stats.chi2.cdf(LR_stat_omnibus, df=len(independent_vars))
        table = [
            [format_number(LR_stat_omnibus), len(independent_vars), format_p_value(p_value_omnibus)]
        ]
        headers = ['Likelihood Ratio Chi-Square', 'df', 'Sig.']
        print("Omnibus Tests of Model Coefficients")
        print(tabulate(table, headers=headers))

        footnotes = [
            "a. Compares the fitted model against the intercept-only model.",
            f"Dependent Variable: {dependent_var}",
            f"Model: (Intercept), {', '.join(independent_vars)}"
        ]
        print('\n' + '\n'.join(footnotes))

    def create_test_of_model_effects_table():
        """
        Cria e exibe a tabela com Testes Tipo III de Efeitos do Modelo (LR Tests).
        """
        df1 = 1
        df2 = df_resid

        table = []
        for var in ['const'] + independent_vars:
            source_name = '(Intercept)' if var == 'const' else var
            row = [
                source_name,
                format_number(LR_stats[var]),
                df1,
                format_p_value(p_values_lr[var]),
                format_number(LR_stats[var]),
                df1,
                format_number(df2),
                format_p_value(p_values_lr[var])
            ]
            table.append(row)

        headers = ['Source', 'Type III LR Chi-Square', 'df', 'Sig.', 'F', 'df1', 'df2', 'Sig.']
        print("Tests of Model Effects")
        print(tabulate(table, headers=headers))

        footnotes = [
            f"Dependent Variable: {dependent_var}",
            f"Model: (Intercept), {', '.join(independent_vars)}"
        ]
        print('\n' + ', '.join(footnotes))

    def create_parameter_estimates_table():
        """
        Cria e exibe a tabela de estimativas dos parâmetros, incluindo intervalos de confiança,
        razão de chances (Exp(B)) e testes de significância.
        """
        conf_int = result_full.conf_int()
        conf_int.columns = ['Lower', 'Upper']
        # Ajuste dos intervalos com os erros padrão escalonados
        conf_int['Lower'] = result_full.params - stats.norm.ppf(0.975) * adjusted_bse
        conf_int['Upper'] = result_full.params + stats.norm.ppf(0.975) * adjusted_bse

        exp_coef = np.exp(result_full.params)
        exp_conf_int_lower = np.exp(conf_int['Lower'])
        exp_conf_int_upper = np.exp(conf_int['Upper'])

        table = []
        for i in range(len(result_full.params)):
            param_name = result_full.params.index[i]
            row = [
                param_name if param_name != 'const' else '(Intercept)',
                format_number(result_full.params.iloc[i]),
                format_number(adjusted_bse.iloc[i]),
                format_number(conf_int.iloc[i]['Lower']),
                format_number(conf_int.iloc[i]['Upper']),
                format_number(wald_chi2[param_name]),
                1,
                format_p_value(p_values[param_name]),
                format_number(exp_coef.iloc[i]),
                format_number(exp_conf_int_lower.iloc[i]),
                format_number(exp_conf_int_upper.iloc[i])
            ]
            table.append(row)

        # Adicionar linha do parâmetro de escala
        table.append([
            '(Scale)',
            format_number(scale),
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ])

        headers = [
            'Parameter', 'B', 'Std. Error',
            'Lower', 'Upper',
            'Wald Chi-Square', 'df', 'Sig.',
            'Exp(B)', 'Lower', 'Upper'
        ]
        print("Parameter Estimates (Adjusted for Deviance)")
        print(tabulate(table, headers=headers))

        footnotes = [
            f"Dependent Variable: {dependent_var}",
            f"Model: (Intercept), {', '.join(independent_vars)}",
            "a. Scale parameter estimated using the deviance."
        ]
        print('\n' + '\n'.join(footnotes))

    # Exibir resultados
    print(f"Número de observações: {n_total}")
    print(f"Número de grupos (combinações únicas): {n_groups}\n")
    create_goodness_of_fit_table()
    print()
    create_omnibus_test_table()
    print()
    create_test_of_model_effects_table()
    print()
    create_parameter_estimates_table()


def analyze_glm_binomial_plots(df, dependent_var, independent_vars):
    """
    Ajusta um modelo GLM binomial (logístico) e plota:
    - logit(p) versus a variável independente
    - Probabilidade prevista versus a variável independente

    Parâmetros:
    - df: DataFrame com dados
    - dependent_var: Nome da variável dependente (binária)
    - independent_vars: Lista de variáveis independentes (assume apenas uma, neste exemplo)

    Retorno:
    - Figura plotly com dois subplots.
    """

    # Validação
    all_vars = [dependent_var] + independent_vars
    for var in all_vars:
        if var not in df.columns:
            raise ValueError(f"A variável '{var}' não existe no DataFrame.")

    # Agrupar e montar o modelo
    grouped = df.groupby(independent_vars)[dependent_var].agg(['sum', 'count']).reset_index()
    grouped.columns = independent_vars + ['Success', 'Total']
    grouped['Failure'] = grouped['Total'] - grouped['Success']

    X_full = grouped[independent_vars]
    y = grouped[['Success', 'Failure']]
    X_full = sm.add_constant(X_full)

    model = sm.GLM(y, X_full, family=sm.families.Binomial())
    result = model.fit()

    intercept = result.params['const']
    coef = result.params[independent_vars[0]]
    equation = f"logit(p) = {intercept:.3f} + {coef:.5f} * {independent_vars[0]}"

    # Criar uma cópia explícita do DataFrame para evitar SettingWithCopyWarning
    df_copy = df.copy()

    # Adicionar colunas previstas ao DataFrame
    df_copy.loc[:, 'predicted_prob'] = result.predict(sm.add_constant(df_copy[independent_vars]))
    df_copy.loc[:, 'logit_p'] = np.log(df_copy['predicted_prob'] / (1 - df_copy['predicted_prob']))
    df_sorted = df_copy.sort_values(by=independent_vars[0])

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(f"Logit(p) vs {independent_vars[0]}", f"Predicted Probability vs {independent_vars[0]}")
    )

    # Logit(p)
    fig.add_trace(go.Scatter(
        x=df_sorted[independent_vars[0]],
        y=coef * df_sorted[independent_vars[0]] + intercept,
        mode='lines', name='Logit Regression Line', line=dict(color='orange')
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=df_sorted[independent_vars[0]],
        y=df_sorted['logit_p'], mode='markers', name='logit(p)',
        marker=dict(color='red', size=3)
    ), row=1, col=1)
    
    # Probabilidade prevista
    fig.add_trace(go.Scatter(
        x=df_sorted[independent_vars[0]],
        y=df_sorted['predicted_prob'], mode='lines', name='Predicted Probability',
        line=dict(color='lightblue')
    ), row=1, col=2)

    fig.add_trace(go.Scatter(
        x=df_sorted[independent_vars[0]],
        y=df_sorted['predicted_prob'], mode='markers', name='Highlighted Points',
        marker=dict(color='blue', size=3)
    ), row=1, col=2)

    fig.update_layout(
        title_text="Logistic Regression Analysis (GLM Binomial)",
        width=1200,
        height=600,
        annotations=[
            dict(
                x=0.25,
                y=1.05,
                showarrow=False,
                text=equation,
                xref="paper",
                yref="paper",
                font=dict(size=12),
            )
        ],
        xaxis1_title=independent_vars[0],
        yaxis1_title="logit(p)",
        xaxis2_title=independent_vars[0],
        yaxis2_title="Predicted Probability",
    )

    fig.show()
    
    return df_copy


def classification_table(df, actual_col, predicted_prob_col, threshold=0.5):
    """
    Gera uma tabela de classificação a partir de um threshold para as probabilidades preditas.

    Parâmetros:
    - df: DataFrame com dados
    - actual_col: Nome da coluna com valores observados (0 ou 1)
    - predicted_prob_col: Nome da coluna com probabilidades previstas
    - threshold: ponto de corte

    Retorna:
    - Exibe a tabela de classificação formatada.
    """
    df = df.copy()
    df['predicted_class'] = np.where(df[predicted_prob_col] >= threshold, 1, 0)
    
    tn, fp, fn, tp = confusion_matrix(df[actual_col], df['predicted_class']).ravel()
    
    total = tn + fp + fn + tp
    total_nao = tn + fp
    total_sim = fn + tp
    total_previsto_nao = tn + fn
    total_previsto_sim = fp + tp

    especificidade = (tn / total_nao * 100) if total_nao != 0 else 0
    sensibilidade = (tp / total_sim * 100) if total_sim != 0 else 0
    precisao = (tp / total_previsto_sim * 100) if total_previsto_sim != 0 else 0

    table = [
        ["Real\\Previsão", "Previsto Não (0)", "Previsto Sim (1)", "Total"],
        ["Real Não (0)", tn, fp, total_nao],
        ["Real Sim (1)", fn, tp, total_sim],
        ["Total", total_previsto_nao, total_previsto_sim, total],
        ["", "", "", ""],
        ["Especificidade", f"{especificidade:.2f}%", ""],
        ["Sensibilidade", f"{sensibilidade:.2f}%", ""],
        ["Precisão", f"{precisao:.2f}%", ""],
    ]
    
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def auc_roc_table(df, actual_col, predicted_prob_col):
    """
    Gera uma tabela da AUC da curva ROC com IC 95%.

    Parâmetros:
    - df: DataFrame com dados
    - actual_col: Nome da coluna com valores observados (0 ou 1)
    - predicted_prob_col: Nome da coluna com probabilidades previstas

    Retorna:
    - Exibe a tabela formatada da AUC.
    """
    df = df.copy()
    auc_value = roc_auc_score(df[actual_col], df[predicted_prob_col])

    n1 = np.sum(df[actual_col] == 1)
    n2 = np.sum(df[actual_col] == 0)
    if n1 == 0 or n2 == 0:
        raise ValueError("Classes positivas e negativas não podem estar vazias.")

    # Fórmulas de Hanley & McNeil (1982)
    Q1 = auc_value / (2 - auc_value)
    Q2 = (2 * auc_value**2) / (1 + auc_value)
    auc_se = np.sqrt((auc_value * (1 - auc_value) + (n1 - 1)*(Q1 - auc_value**2) + (n2 - 1)*(Q2 - auc_value**2)) / (n1*n2))
    
    z = 1.96
    lower_bound = max(0, auc_value - z * auc_se)
    upper_bound = min(1, auc_value + z * auc_se)

    z_value = (auc_value - 0.5) / auc_se
    p_value = 2 * (1 - norm.cdf(abs(z_value)))

    table = [
        ["Área (AUC)", "Erro Padrão", "95% IC Inferior", "95% IC Superior", "Significância"],
        [f"{auc_value:.3f}", f"{auc_se:.4f}", f"{lower_bound:.3f}", f"{upper_bound:.3f}", f"{p_value:.3f}"]
    ]

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print("a. Sob a suposição não-paramétrica\nb. Hipótese nula: área verdadeira = 0.5")


def plot_roc_curve_with_best_threshold(df, actual_col, predicted_prob_col, critical_col):
    """
    Plota a curva ROC, calcula o melhor threshold (Youden), exibe a AUC, e gera tabela com resultados.

    Parâmetros:
    - df: DataFrame com dados
    - actual_col: nome da coluna com valores observados
    - predicted_prob_col: nome da coluna com probabilidades previstas
    - critical_col: nome da coluna crítica associada ao threshold
    """
    df = df.copy()
    for col in [actual_col, predicted_prob_col, critical_col]:
        if col not in df.columns:
            raise ValueError(f"A coluna '{col}' não existe no DataFrame.")

    fpr, tpr, thresholds = roc_curve(df[actual_col], df[predicted_prob_col])
    roc_auc = auc(fpr, tpr)

    n1 = np.sum(df[actual_col] == 1)
    n2 = np.sum(df[actual_col] == 0)
    if n1 == 0 or n2 == 0:
        raise ValueError("Classes positivas e negativas não podem estar vazias.")

    youden_index = tpr - fpr
    best_idx = np.argmax(youden_index)
    best_threshold = thresholds[best_idx]
    best_fpr = fpr[best_idx]
    best_tpr = tpr[best_idx]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr,
        mode='lines', name=f'ROC Curve (AUC = {roc_auc:.3f})',
        line=dict(color='blue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=[best_fpr], y=[best_tpr],
        mode='markers', name=f'Melhor Ponto (Threshold={best_threshold:.3f})',
        marker=dict(color='red', size=10)
    ))
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1],
        mode='lines', name='Modelo Aleatório',
        line=dict(dash='dash', color='gray')
    ))

    fig.update_layout(
        title=f"Curva ROC (AUC = {roc_auc:.3f})",
        xaxis_title="1 - Especificidade (FPR)",
        yaxis_title="Sensibilidade (TPR)",
        width=600,
        height=600,
        showlegend=True
    )
    fig.show()

    best_critical_value = df.loc[df[predicted_prob_col] >= best_threshold, critical_col].min()

    table = [
        ["Melhor Threshold", f"{best_threshold:.3f}"],
        ["FPR no Melhor Ponto", f"{best_fpr:.3f}"],
        ["TPR no Melhor Ponto", f"{best_tpr:.3f}"],
        [f"Valor Crítico ({critical_col})", best_critical_value]
    ]
    print(tabulate(table, headers=["Descrição", "Valor"], tablefmt="grid"))
    
    # Exibir tabela de classificação para o melhor threshold
    classification_table(df, actual_col, predicted_prob_col, threshold=best_threshold)


def plot_odds_ratio_increments(df, dependent_var, independent_var, increment_steps=10, max_increment=100):
    """
    Gera um gráfico suave do efeito de incrementos na variável independente sobre o OR.

    Parâmetros:
    - df: DataFrame com dados
    - dependent_var: variável dependente (0/1)
    - independent_var: variável independente
    - increment_steps: passo dos incrementos
    - max_increment: incremento máximo
    """
    if dependent_var not in df.columns:
        raise ValueError(f"A variável dependente '{dependent_var}' não existe no DataFrame.")
    if independent_var not in df.columns:
        raise ValueError(f"A variável independente '{independent_var}' não existe no DataFrame.")

    grouped = df.groupby(independent_var)[dependent_var].agg(['sum', 'count']).reset_index()
    grouped.columns = [independent_var, 'Success', 'Total']
    grouped['Failure'] = grouped['Total'] - grouped['Success']

    X_full = grouped[[independent_var]]
    y = grouped[['Success', 'Failure']]
    X_full = sm.add_constant(X_full)

    model = sm.GLM(y, X_full, family=sm.families.Binomial())
    result = model.fit()

    intercept = result.params['const']
    coef = result.params[independent_var]

    increments = np.arange(0, max_increment + increment_steps, increment_steps)
    or_values = np.exp(coef * increments)
    increment_percentages = (or_values - 1) * 100

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=increments, y=or_values,
        mode='lines+markers', name='OR',
        line=dict(color='blue'), marker=dict(size=8)
    ))
    fig.update_layout(
        title=f"Efeito da variação em {independent_var} sobre o OR",
        xaxis_title=f"Incrementos em {independent_var} (u.m.)",
        yaxis_title="Odds Ratio (OR)",
        width=800, height=500
    )
    fig.show()

    table = [
        [round(inc, 3), round(or_val, 3), f"{round(perc, 1)}%"]
        for inc, or_val, perc in zip(increments, or_values, increment_percentages)
    ]
    print(tabulate(
        table,
        headers=[f"Incrementos em {independent_var} (u.m.)", "Odds Ratio (OR)", "Acréscimo (%)"],
        tablefmt="grid"
    ))


def calculate_independent_values_for_probabilities(df, dependent_var, independent_var, probabilities):
    """
    Dadas probabilidades desejadas, calcula quais valores da variável independente
    gerariam essas probabilidades no modelo logístico ajustado.

    Parâmetros:
    - df: DataFrame com dados
    - dependent_var: variável dependente (0/1)
    - independent_var: variável independente
    - probabilities: lista de probabilidades desejadas

    Retorna:
    - Exibe uma tabela com o valor do independente para cada p.
    """
    if dependent_var not in df.columns:
        raise ValueError(f"A variável dependente '{dependent_var}' não existe no DataFrame.")
    if independent_var not in df.columns:
        raise ValueError(f"A variável independente '{independent_var}' não existe no DataFrame.")

    grouped = df.groupby(independent_var)[dependent_var].agg(['sum', 'count']).reset_index()
    grouped.columns = [independent_var, 'Success', 'Total']
    grouped['Failure'] = grouped['Total'] - grouped['Success']

    X_full = grouped[[independent_var]]
    y = grouped[['Success', 'Failure']]
    X_full = sm.add_constant(X_full)

    model = sm.GLM(y, X_full, family=sm.families.Binomial())
    result = model.fit()

    intercept = result.params['const']
    coef = result.params[independent_var]

    def find_indep_value(p):
        return (np.log(p / (1 - p)) - intercept) / coef

    indep_values = [find_indep_value(p) for p in probabilities]

    table = [
        [f"{p:.3f}", f"{val:.3f}"] for p, val in zip(probabilities, indep_values)
    ]

    print(tabulate(
        table,
        headers=["Probabilidade (p)", f"Valor de {independent_var} (u.m.)"],
        tablefmt="grid"
    ))


def validate_logistic_model(df, dependent_var, independent_var, test_size=0.3, random_state=42):
    """
    Valida o modelo de regressão logística dividindo a amostra em treino e teste,
    estimando AUC na amostra de teste e exibindo uma tabela com IC e p-valor.

    Parâmetros:
    - df: DataFrame com dados
    - dependent_var: variável dependente (0/1)
    - independent_var: variável independente
    - test_size: proporção de teste (default=0.3)
    - random_state: semente para reprodutibilidade
    """
    if dependent_var not in df.columns:
        raise ValueError(f"A variável dependente '{dependent_var}' não existe no DataFrame.")
    if independent_var not in df.columns:
        raise ValueError(f"A variável independente '{independent_var}' não existe no DataFrame.")

    df = df.copy()
    np.random.seed(random_state)
    df['random'] = np.random.rand(len(df))

    train = df.loc[df['random'] > test_size].copy()
    test = df.loc[df['random'] <= test_size].copy()

    X_train = train[[independent_var]]
    y_train = train[dependent_var]
    X_train = sm.add_constant(X_train)

    X_test = test[[independent_var]]
    y_test = test[dependent_var]
    X_test = sm.add_constant(X_test)

    model = sm.Logit(y_train, X_train)
    result = model.fit(disp=False)

    test['Predicted_Prob'] = result.predict(X_test)

    auc = roc_auc_score(y_test, test['Predicted_Prob'])
    n1 = sum(y_test == 1)
    n2 = sum(y_test == 0)

    # Fórmula de Hanley & McNeil
    Q1 = auc / (2 - auc)
    Q2 = (2 * auc**2) / (1 + auc)
    auc_se = np.sqrt((auc * (1 - auc) + (n1 - 1)*(Q1 - auc**2) + (n2 - 1)*(Q2 - auc**2)) / (n1*n2))

    z = norm.ppf(0.975)
    lower_bound = auc - z * auc_se
    upper_bound = auc + z * auc_se
    if upper_bound > 1.0:
        upper_bound = 1.0

    z_score = (auc - 0.5) / auc_se
    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    validation_table = [
        ["Área", f"{auc:.3f}", f"{auc_se:.3f}", f"{p_value:.3f}", f"{lower_bound:.3f}", f"{upper_bound:.3f}"]
    ]

    print(tabulate(
        validation_table,
        headers=["", "Area", "Std. Error", "Sig.", "Lower Bound (95%)", "Upper Bound (95%)"],
        tablefmt="grid",
        numalign="center"
    ))
    print("\na. Under the nonparametric assumption")
    print("b. Null hypothesis: true area = 0.5")

def validate_logistic_model_compare_auc(df, dependent_var, independent_var, test_size=0.3, random_state=42):
    """
    Ajusta um modelo de regressão logística, calcula AUC no treino e teste, IC 95%, 
    e compara a AUC de treino com a AUC de teste.
    """

    # Verificação de colunas
    if dependent_var not in df.columns:
        raise ValueError(f"A variável dependente '{dependent_var}' não existe no DataFrame.")
    if independent_var not in df.columns:
        raise ValueError(f"A variável independente '{independent_var}' não existe no DataFrame.")

    df = df.copy()
    np.random.seed(random_state)
    df['random'] = np.random.rand(len(df))

    train = df.loc[df['random'] > test_size].copy()
    test = df.loc[df['random'] <= test_size].copy()

    X_train = train[[independent_var]]
    y_train = train[dependent_var]
    X_train = sm.add_constant(X_train)

    X_test = test[[independent_var]]
    y_test = test[dependent_var]
    X_test = sm.add_constant(X_test)

    model = sm.Logit(y_train, X_train)
    result = model.fit(disp=False)

    train['Predicted_Prob'] = result.predict(X_train)
    test['Predicted_Prob'] = result.predict(X_test)

    def auc_confidence_interval(y_true, y_pred):
        auc_value = roc_auc_score(y_true, y_pred)
        n1 = np.sum(y_true == 1)
        n2 = np.sum(y_true == 0)
        Q1 = auc_value / (2 - auc_value)
        Q2 = (2 * auc_value**2) / (1 + auc_value)
        auc_se = np.sqrt((auc_value * (1 - auc_value) + (n1 - 1)*(Q1 - auc_value**2) + (n2 - 1)*(Q2 - auc_value**2)) / (n1*n2))
        z = norm.ppf(0.975)
        lower_bound = auc_value - z * auc_se
        upper_bound = auc_value + z * auc_se
        lower_bound = max(0, lower_bound)
        upper_bound = min(1, upper_bound)
        # Teste de hipótese (AUC != 0.5)
        z_score = (auc_value - 0.5) / auc_se
        p_value = 2 * (1 - norm.cdf(abs(z_score)))
        return auc_value, auc_se, p_value, lower_bound, upper_bound

    # Calcular AUC para treino e teste
    train_auc, train_auc_se, train_p_value, train_lower, train_upper = auc_confidence_interval(y_train, train['Predicted_Prob'])
    test_auc, test_auc_se, test_p_value, test_lower, test_upper = auc_confidence_interval(y_test, test['Predicted_Prob'])

    # Comparação direta das duas AUCs (assumindo independência entre as amostras)
    diff = train_auc - test_auc
    diff_se = np.sqrt(train_auc_se**2 + test_auc_se**2)
    z_diff = diff / diff_se
    p_diff = 2 * (1 - norm.cdf(abs(z_diff)))  # teste bicaudal se diff != 0

    validation_table = [
        ["Treino", f"{train_auc:.3f}", f"{train_auc_se:.3f}", f"{train_p_value:.3f}", f"{train_lower:.3f}", f"{train_upper:.3f}"],
        ["Teste", f"{test_auc:.3f}", f"{test_auc_se:.3f}", f"{test_p_value:.3f}", f"{test_lower:.3f}", f"{test_upper:.3f}"],
        ["Diferença (Treino - Teste)", f"{diff:.3f}", f"{diff_se:.3f}", f"{p_diff:.3f}", "-", "-"]
    ]

    # Observação: Para a diferença, não faz sentido IC usando o mesmo método direto, 
    # mas poderíamos apresentar um IC normal:
    # IC normal 95% da diferença:
    diff_lower = diff - norm.ppf(0.975)*diff_se
    diff_upper = diff + norm.ppf(0.975)*diff_se
    # Atualizar a linha da diferença com IC
    validation_table[-1][-2] = f"{diff_lower:.3f}"
    validation_table[-1][-1] = f"{diff_upper:.3f}"

    print(tabulate(
        validation_table,
        headers=["Amostra", "Área", "Std. Error", "Sig.", "Lower Bound (95%)", "Upper Bound (95%)"],
        tablefmt="grid",
        numalign="center"
    ))
    print("\na. Under the nonparametric assumption")
    print("b. Null hypothesis: true area = 0.5")
    print("c. For the difference: Null hypothesis: AUC_train = AUC_test")
    

def bootstrap_auc_difference(y_train, pred_train, y_test, pred_test, n_boot=1000, random_state=42):
    """
    Realiza um teste de bootstrap para a diferença entre AUCs de treino e teste.
    Retorna a diferença observada, o intervalo de confiança bootstrap e um p-valor aproximado.
    """
    np.random.seed(random_state)
    # Diferença observada
    observed_diff = roc_auc_score(y_train, pred_train) - roc_auc_score(y_test, pred_test)

    diffs = []
    n_train = len(y_train)
    n_test = len(y_test)

    # Reamostragem
    for _ in range(n_boot):
        # Amostra bootstrap para treino
        idx_train = np.random.choice(np.arange(n_train), size=n_train, replace=True)
        # Amostra bootstrap para teste
        idx_test = np.random.choice(np.arange(n_test), size=n_test, replace=True)

        y_train_boot = y_train[idx_train]
        pred_train_boot = pred_train[idx_train]

        y_test_boot = y_test[idx_test]
        pred_test_boot = pred_test[idx_test]

        auc_train_boot = roc_auc_score(y_train_boot, pred_train_boot)
        auc_test_boot = roc_auc_score(y_test_boot, pred_test_boot)

        diffs.append(auc_train_boot - auc_test_boot)

    diffs = np.array(diffs)
    # IC 95% pelo percentil
    lower_bound = np.percentile(diffs, 2.5)
    upper_bound = np.percentile(diffs, 97.5)

    # Cálculo do p-valor
    # p-valor bicaudal: proporção de vezes que |diffs| >= |observed_diff|
    p_value = np.mean(np.abs(diffs) >= np.abs(observed_diff))

    return observed_diff, lower_bound, upper_bound, p_value

def validate_logistic_model_compare_auc_bootstrap(df, dependent_var, independent_var, test_size=0.3, random_state=42, n_boot=1000):
    """
    Ajusta um modelo de regressão logística, calcula AUC no treino e teste, IC 95%,
    e compara a diferença entre AUC_treino e AUC_teste usando um teste de bootstrap.
    """

    if dependent_var not in df.columns:
        raise ValueError(f"A variável dependente '{dependent_var}' não existe no DataFrame.")
    if independent_var not in df.columns:
        raise ValueError(f"A variável independente '{independent_var}' não existe no DataFrame.")

    df = df.copy()
    np.random.seed(random_state)
    df['random'] = np.random.rand(len(df))

    train = df.loc[df['random'] > test_size].copy()
    test = df.loc[df['random'] <= test_size].copy()

    X_train = train[[independent_var]]
    y_train = train[dependent_var].values  # vetor numpy
    X_train = sm.add_constant(X_train)

    X_test = test[[independent_var]]
    y_test = test[dependent_var].values  # vetor numpy
    X_test = sm.add_constant(X_test)

    model = sm.Logit(y_train, X_train)
    result = model.fit(disp=False)

    train['Predicted_Prob'] = result.predict(X_train)
    test['Predicted_Prob'] = result.predict(X_test)

    pred_train = train['Predicted_Prob'].values
    pred_test = test['Predicted_Prob'].values

    auc_train = roc_auc_score(y_train, pred_train)
    auc_test = roc_auc_score(y_test, pred_test)

    # Teste de bootstrap para diferença entre AUCs
    observed_diff, diff_lower, diff_upper, p_diff = bootstrap_auc_difference(y_train, pred_train, y_test, pred_test, n_boot=n_boot, random_state=random_state)

    # Calcular IC individuais das AUCs usando método Hanley & McNeil
    def auc_confidence_interval(y_true, y_pred):
        auc_value = roc_auc_score(y_true, y_pred)
        n1 = np.sum(y_true == 1)
        n2 = np.sum(y_true == 0)
        Q1 = auc_value / (2 - auc_value)
        Q2 = (2 * auc_value**2) / (1 + auc_value)
        auc_se = np.sqrt((auc_value * (1 - auc_value) + (n1 - 1)*(Q1 - auc_value**2) + (n2 - 1)*(Q2 - auc_value**2)) / (n1*n2))
        z = norm.ppf(0.975)
        lower_bound = auc_value - z * auc_se
        upper_bound = auc_value + z * auc_se
        lower_bound = max(0, lower_bound)
        upper_bound = min(1, upper_bound)
        # Teste de hipótese (AUC != 0.5)
        z_score = (auc_value - 0.5) / auc_se
        p_value = 2 * (1 - norm.cdf(abs(z_score)))
        return auc_value, auc_se, p_value, lower_bound, upper_bound

    train_auc, train_auc_se, train_p_value, train_lower, train_upper = auc_confidence_interval(y_train, pred_train)
    test_auc, test_auc_se, test_p_value, test_lower, test_upper = auc_confidence_interval(y_test, pred_test)

    validation_table = [
        ["Treino", f"{train_auc:.3f}", f"{train_auc_se:.3f}", f"{train_p_value:.3f}", f"{train_lower:.3f}", f"{train_upper:.3f}"],
        ["Teste", f"{test_auc:.3f}", f"{test_auc_se:.3f}", f"{test_p_value:.3f}", f"{test_lower:.3f}", f"{test_upper:.3f}"],
        ["Diferença (Treino - Teste)", f"{observed_diff:.3f}", "-", f"{p_diff:.3f}", f"{diff_lower:.3f}", f"{diff_upper:.3f}"]
    ]

    print(tabulate(
        validation_table,
        headers=["Amostra", "Área", "Std. Error", "Sig.", "Lower Bound (95%)", "Upper Bound (95%)"],
        tablefmt="grid",
        numalign="center"
    ))
    print("\na. Under the nonparametric assumption")
    print("b. Null hypothesis: true area = 0.5 (para AUC individuais)")
    print("c. Null hypothesis: AUC_train = AUC_test (para diferença)")
    print("d. Diferença: IC 95% bootstrap")
    
    
def binomial_logistic_analysis(
    df,
    col_resp,
    col_freq="Freq",
    cols_explicativas=None,
    max_interaction_order=None,
    max_p_value=0.05,
    return_table=True,
    classification_threshold=0.5,
    critical_col=None,
    # Parâmetros para ativar/desativar validação
    do_validation=False,
    test_size=0.3,
    random_state=42,
    # Parâmetros para controlar o que será exibido
    show_saturated_model_summary=True,
    show_final_model_summary=True,
    show_comparison=True,
    show_params_table=True,
    show_classification_table=True,
    show_auc_table=True,
    show_roc_plot=True,
    show_best_threshold_table=True
):
    """
    1) "Explode" (transforma df_grouped -> df_line), repetindo cada linha pela frequência ('col_freq'),
       caso 'col_freq' não seja None. Caso contrário, assume que o DataFrame já está no formato desejado.
    2) Se do_validation=True, divide df_line em train e test. Ajusta o modelo (com eliminação para trás) somente em train.
    3) Exibe sumários, tabelas de classificação, ROC etc. para o conjunto de treino.
    4) Se do_validation=True, calcula AUC na amostra de teste e compara com a AUC de treino.
    5) Retorna um dicionário com informações do modelo, dados de treino e teste (se solicitado).
    """

    # ------------------------------------------------------------------
    # 1) EXPLODE DF_GROUPED -> DF_LINE
    # ------------------------------------------------------------------
    if col_freq is not None:
        # Repete cada linha 'Freq' vezes (expansão)
        df_line = df.loc[df.index.repeat(df[col_freq])].drop(columns=col_freq).reset_index(drop=True)
    else:
        # Se col_freq é None, assume que o dataframe já está "explodido"
        df_line = df.copy()

    # ------------------------------------------------------------------
    # 2) Se do_validation=True, dividir em treino e teste.
    #    Senão, "train" = df_line inteiro, e não haverá "test".
    # ------------------------------------------------------------------
    if do_validation:
        np.random.seed(random_state)
        df_line['rand_split'] = np.random.rand(len(df_line))
        train = df_line[df_line['rand_split'] > test_size].copy()
        test = df_line[df_line['rand_split'] <= test_size].copy()
        # Remove a coluna rand_split para não atrapalhar
        train.drop(columns=['rand_split'], inplace=True)
        test.drop(columns=['rand_split'], inplace=True)
    else:
        train = df_line.copy()
        test = None

    # ------------------------------------------------------------------
    # Identifica colunas explicativas, se não informadas
    # ------------------------------------------------------------------
    if cols_explicativas is None:
        cols_explicativas = [c for c in train.columns if c != col_resp]

    # Força 'Viagens' como categórica, se existir
    if 'Viagens' in cols_explicativas:
        train['Viagens'] = train['Viagens'].astype('category')
        if test is not None and 'Viagens' in test.columns:
            test['Viagens'] = test['Viagens'].astype('category')

    # ------------------------------------------------------------------
    # Função para gerar interações até max_interaction_order
    # ------------------------------------------------------------------
    def gerar_interacoes(preds, max_ord):
        if max_ord is None:
            max_ord = len(preds)
        interactions = []
        for order in range(2, len(preds) + 1):
            if order > max_ord:
                break
            for combo in itertools.combinations(preds, order):
                interactions.append(':'.join(combo))
        return interactions

    # ------------------------------------------------------------------
    # Ajuste do modelo saturado na amostra de TREINO
    # ------------------------------------------------------------------
    # Modelo saturado (sem limitar ordem de interação)
    all_predictors_saturated = cols_explicativas + gerar_interacoes(cols_explicativas, None)
    formula_saturada = f"{col_resp} ~ {' + '.join(all_predictors_saturated)}"

    modelo_saturado = glm(
        formula=formula_saturada,
        data=train,
        family=sm.families.Binomial()
    ).fit()

    # Mostra o resumo do modelo saturado, se habilitado
    if show_saturated_model_summary:
        print("=== MODELO SATURADO (TREINO) ===")
        print(modelo_saturado.summary())

    # ------------------------------------------------------------------
    # Eliminação para trás (backward) na amostra de TREINO
    # ------------------------------------------------------------------
    adjusted_predictors = cols_explicativas + gerar_interacoes(cols_explicativas, max_interaction_order)

    import re

    while True:
        formula_ajustada = f"{col_resp} ~ {' + '.join(adjusted_predictors)}"
        modelo_ajustado = glm(
            formula=formula_ajustada,
            data=train,
            family=sm.families.Binomial()
        ).fit()

        pvals = modelo_ajustado.pvalues.drop(labels='Intercept', errors='ignore')
        worst_p_value = pvals.max() if len(pvals) > 0 else 0

        if worst_p_value <= max_p_value:
            break

        # Identify worst predictor
        worst_term = pvals.idxmax()

        # "Limpa" o label do termo, se for algo como C(X)[T.x] ou X:Y
        base_worst = re.sub(r'C\((.*?)\)\[T.*?\]', r'\1', worst_term)
        base_worst = re.sub(r'\[T.*?\]', '', base_worst)

        # Remove do adjusted_predictors
        if base_worst in adjusted_predictors:
            adjusted_predictors.remove(base_worst)
        else:
            if worst_term in adjusted_predictors:
                adjusted_predictors.remove(worst_term)
            else:
                parts = base_worst.split(":")
                for p in parts:
                    if p in adjusted_predictors:
                        adjusted_predictors.remove(p)

    # Modelo final (TREINO)
    modelo_final = glm(
        formula=f"{col_resp} ~ {' + '.join(adjusted_predictors)}",
        data=train,
        family=sm.families.Binomial()
    ).fit()

    if show_final_model_summary:
        print("\n=== MODELO FINAL APÓS ELIMINAÇÃO (TREINO) ===")
        print(modelo_final.summary())

    # ------------------------------------------------------------------
    # Comparação saturado vs final (apenas no TREINO)
    # ------------------------------------------------------------------
    if show_comparison:
        print("\n=== COMPARAÇÃO ENTRE MODELOS (Saturado vs. Final) ===")
        print(f"AIC do Modelo Saturado (treino): {modelo_saturado.aic:.2f}")
        print(f"AIC do Modelo Final (treino):    {modelo_final.aic:.2f}")
        lr_stat = 2 * (modelo_saturado.llf - modelo_final.llf)
        df_diff = len(modelo_saturado.params) - len(modelo_final.params)
        p_lr = chi2.sf(lr_stat, df_diff)
        print("\nTeste de Razão de Verossimilhança (LRT) no TREINO:")
        print(f" LR stat = {lr_stat:.3f}")
        print(f" Diferença de parâmetros = {df_diff}")
        print(f" p-value = {p_lr:.4f}")

    # ------------------------------------------------------------------
    # 3) Tabela final de parâmetros do modelo (opcional)
    #    (apenas do modelo final, ajustado em TREINO)
    # ------------------------------------------------------------------
    if show_params_table and return_table:
        coefs = modelo_final.params
        ses = modelo_final.bse
        zvals = modelo_final.tvalues
        pvals = modelo_final.pvalues
        wald_stats = zvals**2
        exp_coefs = np.exp(coefs)
        conf_int = modelo_final.conf_int()
        conf_int_exp = np.exp(conf_int)

        tabela = pd.DataFrame({
            'Variable': coefs.index.tolist(),
            'B': coefs.values,
            'Std. Error': ses.values,
            'Wald': wald_stats.values,
            'Sig.': pvals.values,
            'Exp(B)': exp_coefs.values,
            'Lower Bound': conf_int_exp[0].values,
            'Upper Bound': conf_int_exp[1].values
        })

        def format_p(p):
            return "<0.001" if p < 0.001 else f"{p:.4f}"

        tabela['Sig.'] = tabela['Sig.'].apply(format_p)
        tabela['B'] = tabela['B'].round(5)
        tabela['Std. Error'] = tabela['Std. Error'].round(5)
        tabela['Wald'] = tabela['Wald'].round(3)
        tabela['Exp(B)'] = tabela['Exp(B)'].round(3)
        tabela['Lower Bound'] = tabela['Lower Bound'].round(3)
        tabela['Upper Bound'] = tabela['Upper Bound'].round(3)

        # Renomear intercept
        tabela.loc[tabela['Variable']=='Intercept', 'Variable'] = 'const'
        tabela.reset_index(drop=True, inplace=True)

        print("\n=== TABELA FINAL ===")
        print(tabulate(tabela, headers=tabela.columns, tablefmt='psql', showindex=False))

    # ------------------------------------------------------------------
    # 4) Avaliação do modelo final na amostra de TREINO
    # ------------------------------------------------------------------
    df_result_train = train.copy()
    df_result_train['predicted_prob'] = modelo_final.predict(df_result_train)

    # 4.1) Tabela de classificação (threshold fixo) - TREINO
    df_tmp = df_result_train.copy()
    df_tmp['predicted_class'] = (df_tmp['predicted_prob'] >= classification_threshold).astype(int)

    tn, fp, fn, tp = confusion_matrix(df_tmp[col_resp], df_tmp['predicted_class']).ravel()
    total = tn + fp + fn + tp
    total_nao = tn + fp
    total_sim = fn + tp
    total_previsto_nao = tn + fn
    total_previsto_sim = fp + tp

    especificidade = (tn / total_nao * 100) if total_nao != 0 else 0
    sensibilidade = (tp / total_sim * 100) if total_sim != 0 else 0
    precisao = (tp / total_previsto_sim * 100) if total_previsto_sim != 0 else 0

    if show_classification_table:
        print(f"\n=== TABELA DE CLASSIFICAÇÃO (TREINO) threshold={classification_threshold} ===")
        table_clf = [
            ["Real\\Previsão", "Previsto Não (0)", "Previsto Sim (1)", "Total"],
            ["Real Não (0)", tn, fp, total_nao],
            ["Real Sim (1)", fn, tp, total_sim],
            ["Total", total_previsto_nao, total_previsto_sim, total],
            ["", "", "", ""],
            ["Especificidade", f"{especificidade:.2f}%", ""],
            ["Sensibilidade", f"{sensibilidade:.2f}%", ""],
            ["Precisão", f"{precisao:.2f}%", ""],
        ]
        print(tabulate(table_clf, headers="firstrow", tablefmt="grid"))

    # 4.2) AUC no TREINO e IC 95%
    auc_value_train = roc_auc_score(df_tmp[col_resp], df_tmp['predicted_prob'])
    n1 = np.sum(df_tmp[col_resp] == 1)
    n2 = np.sum(df_tmp[col_resp] == 0)
    if n1 == 0 or n2 == 0:
        raise ValueError("Não há dados suficientes (classe 0 ou 1 ausente) para calcular AUC (treino).")

    Q1 = auc_value_train / (2 - auc_value_train)
    Q2 = (2 * auc_value_train**2) / (1 + auc_value_train)
    auc_se_train = np.sqrt(
        (auc_value_train*(1 - auc_value_train) + (n1 - 1)*(Q1 - auc_value_train**2) + (n2 - 1)*(Q2 - auc_value_train**2))
        / (n1*n2)
    )
    z = 1.96
    lower_bound_train = max(0, auc_value_train - z * auc_se_train)
    upper_bound_train = min(1, auc_value_train + z * auc_se_train)

    # Teste de p-valor se AUC == 0.5 (no TREINO)
    z_value = (auc_value_train - 0.5) / auc_se_train
    p_value_train = 2 * (1 - norm.cdf(abs(z_value)))

    if show_auc_table:
        print("\n=== AUC-ROC (TREINO) (com IC 95%) ===")
        table_auc = [
            ["Área (AUC)", "Erro Padrão", "95% IC Inf", "95% IC Sup", "Significância"],
            [f"{auc_value_train:.3f}", f"{auc_se_train:.4f}", f"{lower_bound_train:.3f}", f"{upper_bound_train:.3f}", f"{p_value_train:.3f}"]
        ]
        print(tabulate(table_auc, headers="firstrow", tablefmt="grid"))
        print("a. Sob a suposição não-paramétrica\nb. Hipótese nula: área verdadeira = 0.5")

    # 4.3) Curva ROC (TREINO) e melhor threshold (Youden)
    fpr, tpr, thresholds = roc_curve(df_tmp[col_resp], df_tmp['predicted_prob'])
    roc_area_train = auc(fpr, tpr)

    # Índice de Youden: TPR + (1 - FPR) - 1
    youden_index = tpr + (1 - fpr) - 1
    best_idx = np.argmax(youden_index)
    best_threshold_train = thresholds[best_idx]
    best_fpr = fpr[best_idx]
    best_tpr = tpr[best_idx]

    if show_roc_plot:
        print("\n=== Curva ROC (TREINO) e Melhor Threshold (Youden) ===")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=fpr,
            y=tpr,
            mode='lines',
            name=f'ROC Curve (AUC = {roc_area_train:.3f})',
            line=dict(color='blue', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=[best_fpr],
            y=[best_tpr],
            mode='markers',
            name=f'Melhor Ponto (Threshold={best_threshold_train:.3f})',
            marker=dict(color='red', size=10)
        ))
        fig.add_trace(go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode='lines',
            name='Modelo Aleatório',
            line=dict(dash='dash', color='gray')
        ))
        fig.update_layout(
            title=f"Curva ROC (TREINO) (AUC = {roc_area_train:.3f})",
            xaxis_title="1 - Especificidade (FPR)",
            yaxis_title="Sensibilidade (TPR)",
            width=600,
            height=600,
            showlegend=True
        )
        fig.show()

    # 4.4) Valor crítico (TREINO) se informado
    best_critical_value_train = None
    if critical_col is not None and critical_col in df_tmp.columns:
        mask = df_tmp['predicted_prob'] >= best_threshold_train
        if mask.any():
            if pd.api.types.is_numeric_dtype(df_tmp[critical_col]):
                best_critical_value_train = df_tmp.loc[mask, critical_col].min()
            else:
                best_critical_value_train = df_tmp.loc[mask, critical_col].astype(str).min()
        else:
            best_critical_value_train = None

    if show_best_threshold_table:
        table_best = [
            ["Melhor Threshold (TREINO)", f"{best_threshold_train:.3f}"],
            ["FPR no Melhor Ponto (TREINO)", f"{best_fpr:.3f}"],
            ["TPR no Melhor Ponto (TREINO)", f"{best_tpr:.3f}"],
            [f"Valor Crítico ({critical_col})", best_critical_value_train if best_critical_value_train is not None else "-"]
        ]
        print(tabulate(table_best, headers=["Descrição", "Valor"], tablefmt="grid"))

        # Tabela de classificação com o best threshold (TREINO)
        print("\n=== TABELA DE CLASSIFICAÇÃO (TREINO) (Best Threshold) ===")
        df_tmp['predicted_class_best'] = (df_tmp['predicted_prob'] >= best_threshold_train).astype(int)

        tn_b, fp_b, fn_b, tp_b = confusion_matrix(df_tmp[col_resp], df_tmp['predicted_class_best']).ravel()
        total_b = tn_b + fp_b + fn_b + tp_b
        total_nao_b = tn_b + fp_b
        total_sim_b = fn_b + tp_b
        total_previsto_nao_b = tn_b + fn_b
        total_previsto_sim_b = fp_b + tp_b

        espec_b = (tn_b / total_nao_b * 100) if total_nao_b != 0 else 0
        sensib_b = (tp_b / total_sim_b * 100) if total_sim_b != 0 else 0
        prec_b = (tp_b / total_previsto_sim_b * 100) if total_previsto_sim_b != 0 else 0

        table_best_clf = [
            ["Real\\Previsão", "Previsto Não (0)", "Previsto Sim (1)", "Total"],
            ["Real Não (0)", tn_b, fp_b, total_nao_b],
            ["Real Sim (1)", fn_b, tp_b, total_sim_b],
            ["Total", total_previsto_nao_b, total_previsto_sim_b, total_b],
            ["", "", "", ""],
            ["Especificidade", f"{espec_b:.2f}%", ""],
            ["Sensibilidade", f"{sensib_b:.2f}%", ""],
            ["Precisão", f"{prec_b:.2f}%", ""],
        ]
        print(tabulate(table_best_clf, headers="firstrow", tablefmt="grid"))

    # ------------------------------------------------------------------
    # 5) Se do_validation=True, avaliar na amostra de TESTE
    # ------------------------------------------------------------------
    # Aqui incorporamos a lógica de "validate_glm_model" resumidamente,
    # mas *sem* refazer eliminação de variáveis (pois já foi feita no TREINO).
    # Apenas prevemos no TESTE, calculamos AUC e comparamos com a AUC de TREINO.
    # ------------------------------------------------------------------
    auc_value_test = None
    auc_se_test = None
    p_value_test = None
    diff_auc = None
    p_diff = None
    validation_table = None

    if do_validation and test is not None and len(test) > 0:
        # Previsões no TESTE com o modelo final (treino)
        test = test.copy()
        test['predicted_prob'] = modelo_final.predict(test)

        # AUC no TESTE
        y_test = test[col_resp]
        y_score_test = test['predicted_prob']

        if y_test.nunique() < 2:
            # Se só tem uma classe no teste, não é possível calcular AUC
            auc_value_test = np.nan
            print("\nAviso: A amostra de teste não possui as 2 classes. AUC não pode ser calculada.")
        else:
            auc_value_test = roc_auc_score(y_test, y_score_test)

            # IC 95% para AUC de teste
            n1_test = np.sum(y_test == 1)
            n2_test = np.sum(y_test == 0)
            Q1_test = auc_value_test / (2 - auc_value_test)
            Q2_test = (2 * auc_value_test**2) / (1 + auc_value_test)
            auc_se_test = np.sqrt(
                (auc_value_test*(1 - auc_value_test) + (n1_test - 1)*(Q1_test - auc_value_test**2) + (n2_test - 1)*(Q2_test - auc_value_test**2))
                / (n1_test*n2_test)
            )
            z_test = (auc_value_test - 0.5) / auc_se_test if auc_se_test != 0 else 0
            p_value_test = 2 * (1 - norm.cdf(abs(z_test)))

            # Comparação entre AUC de treino e teste (aproximação)
            diff_auc = auc_value_train - auc_value_test
            diff_se = np.sqrt((auc_se_train**2) + (auc_se_test**2)) if auc_se_test else np.nan
            z_diff = (diff_auc / diff_se) if (diff_se and diff_se != 0) else np.nan
            p_diff = 2 * (1 - norm.cdf(abs(z_diff))) if not np.isnan(z_diff) else np.nan

            # Monta tabela
            def fmt(x):
                return "nan" if x is None or np.isnan(x) else f"{x:.3f}"

            validation_table = [
                ["TREINO", fmt(auc_value_train), fmt(auc_se_train), fmt(p_value_train), fmt(lower_bound_train), fmt(upper_bound_train)],
                ["TESTE",  fmt(auc_value_test),  fmt(auc_se_test),  fmt(p_value_test),  "-", "-"],
                ["Diferença (Train - Test)", fmt(diff_auc), fmt(diff_se), fmt(p_diff), "-", "-"]
            ]
            # Para IC da diferença (opcional)
            if diff_se and not np.isnan(diff_se):
                z975 = norm.ppf(0.975)
                diff_lower = diff_auc - z975*diff_se
                diff_upper = diff_auc + z975*diff_se
                validation_table[-1][-2] = fmt(diff_lower)
                validation_table[-1][-1] = fmt(diff_upper)

            # Exibir tabela
            print("\n=== VALIDAÇÃO NO TESTE ===")
            print(tabulate(
                validation_table,
                headers=["Amostra", "AUC", "Std. Error", "p-value", "Lower (95%)", "Upper (95%)"],
                tablefmt="grid",
                numalign="center"
            ))
            print("\na. Sob a suposição não-paramétrica")
            print("b. Hipótese nula: área verdadeira = 0.5")
            print("c. Para a diferença: Hipótese nula: AUC_treino = AUC_teste")
    elif do_validation and (test is None or len(test) == 0):
        print("\nAviso: Após split, a amostra de teste ficou vazia. Não foi possível validar.")

    # ------------------------------------------------------------------
    # 6) Retorno
    # ------------------------------------------------------------------
    return {
        'modelo_saturado': modelo_saturado,
        'modelo_final': modelo_final,
        'adjusted_predictors': adjusted_predictors,
        'df_line': df_line,              # DataFrame expandido completo
        'df_result_train': df_result_train,  # Base de treino com predicted_prob
        'df_test': test,                    # Base de teste (caso do_validation=True)
        'best_threshold_train': best_threshold_train,
        'best_critical_value_train': best_critical_value_train,
        'auc_train': auc_value_train,
        'auc_test': auc_value_test,
        'diff_auc': diff_auc,
        'p_diff_auc': p_diff,
        'validation_table': validation_table
    }
    
import numpy as np
import pandas as pd
import itertools
from tabulate import tabulate
from sklearn.metrics import confusion_matrix, roc_auc_score
from scipy.stats import norm
import statsmodels.formula.api as smf


def compute_auc_ci_multiclass_bootstrap(
    y_true, 
    pred_probs, 
    n_bootstraps=1000, 
    random_seed=42, 
    multi_class="ovr", 
    average="macro"
):
    """
    Calcula AUC multiclasse (One-vs-Rest ou One-vs-One), média (macro/micro/weighted),
    e seu IC 95% via bootstrap.

    Retorna:
        auc_mean: média da AUC
        se_auc: erro padrão aproximado
        ci_lower: limite inferior (IC95%)
        ci_upper: limite superior (IC95%)
    """
    # Verifica se todos os y_true são inteiros (categorias)
    y_true = np.array(y_true)
    # Precisamos garantir que pred_probs seja um array [n amostras, n_classes]
    # e que y_true tenha mesmo n_classes contidas.
    classes_ = np.unique(y_true)
    rng = np.random.RandomState(random_seed)

    # AUC base
    try:
        auc_base = roc_auc_score(
            y_true, 
            pred_probs, 
            multi_class=multi_class, 
            average=average
        )
    except ValueError:
        # Se for impossível calcular (ex.: uma só classe)
        return np.nan, np.nan, np.nan, np.nan

    # Bootstrap
    bootstrapped_scores = []
    n = len(y_true)
    for _ in range(n_bootstraps):
        # amostragem com reposição
        indices = rng.randint(0, n, n)
        y_boot = y_true[indices]
        p_boot = pred_probs[indices, :]
        try:
            score = roc_auc_score(
                y_boot, 
                p_boot, 
                multi_class=multi_class, 
                average=average
            )
            bootstrapped_scores.append(score)
        except ValueError:
            # ocasionalmente pode dar erro se alguma classe sumir no bootstrap
            # => ignora essa amostra
            continue

    if len(bootstrapped_scores) < 2:
        return auc_base, np.nan, np.nan, np.nan

    auc_array = np.array(bootstrapped_scores)
    auc_mean = auc_array.mean()
    se_auc = auc_array.std(ddof=1)  # desvio padrão amostral
    
    # IC 95%
    z975 = norm.ppf(0.975)
    ci_lower = auc_mean - z975 * se_auc
    ci_upper = auc_mean + z975 * se_auc

    return auc_mean, se_auc, ci_lower, ci_upper


def multinomial_logistic_analysis(
    df,
    col_resp,
    cols_explicativas=None,
    col_freq=None,
    baseline_value=None,
    max_interaction_order=1,
    max_p_value=0.05,
    do_validation=False,
    test_size=0.3,
    random_state=42,
    show_saturated_model_summary=True,
    show_final_model_summary=True,
    show_params_table=True,
    show_classification_table=True,
    # Parâmetros para AUC multiclasse
    multi_class_method="ovr",    # "ovr" ou "ovo"
    average_method="macro",      # "macro", "micro", "weighted"
    n_bootstraps=1000
):
    """
    Executa uma análise de Regressão Logística Multinomial (MNLogit) com:
      1) Explosão do DataFrame pela coluna de frequência (opcional)
      2) Conversão automática da coluna resposta para códigos [0..K-1]
         (possibilidade de escolher 'baseline_value' para mapear como 0)
      3) Divisão em treino e teste (opcional)
      4) Geração de interações até 'max_interaction_order'
      5) Eliminação para trás (Backward) com p-valor > 'max_p_value'
      6) Exibição opcional de sumários e matriz de confusão
      7) Cálculo de AUC multiclasse (one-vs-rest ou one-vs-one, etc.) por bootstrap,
         com IC 95% e comparação entre AUC de treino e teste.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame original.
    col_resp : str
        Nome da coluna de resposta (numérica: ex. 1,2,3).
        Será recodificada para 0,1,2,...
    cols_explicativas : list(str) ou None
        Quais colunas usar como preditoras. Se None, usa todas, exceto col_resp.
    col_freq : str ou None
        Se não for None, "explode" o DataFrame repetindo as linhas
        conforme a frequência.
    baseline_value : int ou float ou None
        Se informado, essa categoria vira 0 no mapeamento (baseline).
        Ex.: baseline_value=1 => mapeia "1" -> 0.
    max_interaction_order : int
        Gera interações até essa ordem (ex.: 2 => 2ª ordem).
    max_p_value : float
        Limiar de p-valor para remover variáveis no Backward.
    do_validation : bool
        Se True, faz split em treino/teste e calcula AUC.
    test_size : float
        Proporção de teste (ex.: 0.3 => 30%).
    random_state : int
        Semente para replicabilidade do split.
    show_saturated_model_summary : bool
        Exibe sumário do modelo saturado antes do Backward.
    show_final_model_summary : bool
        Exibe sumário do modelo final após Backward.
    show_params_table : bool
        Exibe uma tabela com os coeficientes do modelo final.
    show_classification_table : bool
        Exibe a matriz de confusão no treino (e no teste, se do_validation=True).
    multi_class_method : str
        Modo de cálculo de AUC multiclasse para roc_auc_score ("ovr" ou "ovo").
    average_method : str
        Tipo de média para agregação da AUC multiclasse ("macro", "micro", "weighted").
    n_bootstraps : int
        Número de reamostragens para o bootstrap da AUC.

    Retorna:
    --------
    dict:
        Contendo modelo final, preditores finais, DataFrame de treino/teste, etc.
    """

    # ------------------------------------------------------------
    # 1) Explodir se houver col_freq
    # ------------------------------------------------------------
    if col_freq is not None:
        df_expanded = df.loc[df.index.repeat(df[col_freq])].drop(columns=col_freq).reset_index(drop=True)
    else:
        df_expanded = df.copy()

    # ------------------------------------------------------------
    # 2) Converter a coluna resposta para códigos [0..k-1],
    #    com a opção de baseline_value -> 0
    # ------------------------------------------------------------
    df_expanded[col_resp] = df_expanded[col_resp].astype(int)
    original_cats = np.sort(df_expanded[col_resp].unique())

    if baseline_value is not None:
        if baseline_value not in original_cats:
            raise ValueError(
                f"Valor '{baseline_value}' não existe em df['{col_resp}']. "
                f"Categorias encontradas: {list(original_cats)}"
            )
        new_order = [baseline_value] + [x for x in original_cats if x != baseline_value]
    else:
        new_order = list(original_cats)

    cat_map = {}
    for i, val in enumerate(new_order):
        cat_map[val] = i

    col_resp_code = col_resp + "_code"
    df_expanded[col_resp_code] = df_expanded[col_resp].map(cat_map)

    # ------------------------------------------------------------
    # 3) Split train/test, se do_validation=True
    # ------------------------------------------------------------
    if do_validation:
        np.random.seed(random_state)
        df_expanded['rand_split'] = np.random.rand(len(df_expanded))
        train = df_expanded[df_expanded['rand_split'] > test_size].copy()
        test = df_expanded[df_expanded['rand_split'] <= test_size].copy()
        train.drop(columns=['rand_split'], inplace=True)
        test.drop(columns=['rand_split'], inplace=True)
    else:
        train = df_expanded.copy()
        test = None

    # ------------------------------------------------------------
    # 4) Identifica cols_explicativas se não fornecido
    # ------------------------------------------------------------
    if cols_explicativas is None:
        cols_explicativas = [c for c in train.columns if c not in [col_resp, col_resp_code]]

    # ------------------------------------------------------------
    # 5) Gera interações até max_interaction_order
    # ------------------------------------------------------------
    def gerar_interacoes(preds, max_ord):
        interactions = []
        if max_ord is None:
            max_ord = len(preds)
        for order in range(2, len(preds) + 1):
            if order > max_ord:
                break
            for combo in itertools.combinations(preds, order):
                interactions.append(':'.join(combo))
        return interactions

    all_predictors_saturated = cols_explicativas + gerar_interacoes(cols_explicativas, None)
    adjusted_predictors = cols_explicativas + gerar_interacoes(cols_explicativas, max_interaction_order)

    # ------------------------------------------------------------
    # 6) Ajuste do modelo
    # ------------------------------------------------------------
    import re

    def fit_mnlogit(formula, data):
        return smf.mnlogit(formula=formula, data=data).fit(disp=False)

    formula_saturada = f"{col_resp_code} ~ {' + '.join(all_predictors_saturated)}"
    modelo_saturado = fit_mnlogit(formula_saturada, train)

    if show_saturated_model_summary:
        print("=== MODELO SATURADO ===")
        print(modelo_saturado.summary())

    # Backward
    while True:
        formula_ajustada = f"{col_resp_code} ~ {' + '.join(adjusted_predictors)}"
        modelo_ajustado = fit_mnlogit(formula_ajustada, train)

        pvals_df = modelo_ajustado.pvalues
        mask_intercept = pvals_df.index.to_series().str.contains("Intercept")
        pvals_df = pvals_df.loc[~mask_intercept]

        if pvals_df.empty:
            worst_p_value = 0
            worst_term = None
        else:
            pvals_series = pvals_df.stack()
            worst_p_value = pvals_series.max()
            worst_term = pvals_series.idxmax()[0]

        if worst_term is None or worst_p_value <= max_p_value:
            break

        base_worst = re.sub(r'C\((.*?)\)\[T.*?\]', r'\1', worst_term)
        base_worst = re.sub(r'\[T.*?\]', '', base_worst)
        if base_worst in adjusted_predictors:
            adjusted_predictors.remove(base_worst)
        else:
            parts = base_worst.split(":")
            for p in parts:
                if p in adjusted_predictors:
                    adjusted_predictors.remove(p)

    final_formula = f"{col_resp_code} ~ {' + '.join(adjusted_predictors)}"
    modelo_final = fit_mnlogit(final_formula, train)

    if show_final_model_summary:
        print("\n=== MODELO FINAL (após Backward) ===")
        print(modelo_final.summary())

    # ------------------------------------------------------------
    # 7) Tabela de parâmetros (opcional)
    # ------------------------------------------------------------
    if show_params_table:
        coefs = modelo_final.params
        ses = modelo_final.bse
        zvals = modelo_final.tvalues
        pvals = modelo_final.pvalues
        wald_stats = zvals ** 2

        conf_int = modelo_final.conf_int().reset_index()
        conf_int.columns = ["category", "variable", "lower", "upper"]
        conf_int["category"] = conf_int["category"].astype(str).str.strip()
        conf_int["variable"] = conf_int["variable"].astype(str).str.strip()

        # Alinhar automaticamente rótulos do conf_int com coefs.columns
        # Lê as categorias existentes em coefs.columns e as do conf_int["category"].
        # Exemplo: coefs.columns => [0,1,2], conf_int["category"] => ["1","2","3"]
        # Precisamos descobrir a diferença e mapear.
        model_cats = [str(c) for c in coefs.columns]
        conf_cats = sorted(conf_int["category"].unique(), key=lambda x: int(x) if x.isdigit() else x)

        # Se a contagem for a mesma, podemos mapear "1->0", "2->1", "3->2", etc.
        # Caso contrário, apenas deixamos o que já existe (poderia ser a baseline ausente).
        if len(conf_cats) == len(model_cats):
            # Faz um dicionário de correspondência ordenada
            cat_map_conf = {old: new for old, new in zip(conf_cats, model_cats)}
            conf_int["category"] = conf_int["category"].replace(cat_map_conf)

        table_list = []
        for cat in coefs.columns:
            cat_str = str(cat).strip()
            for param in coefs.index:
                param_str = str(param).strip()

                b = coefs.loc[param, cat]
                se = ses.loc[param, cat]
                wald = wald_stats.loc[param, cat]
                pval = pvals.loc[param, cat]

                ci_row = conf_int[
                    (conf_int["category"] == cat_str) & 
                    (conf_int["variable"] == param_str)
                ]
                if not ci_row.empty:
                    ci_lower = ci_row.iloc[0]["lower"]
                    ci_upper = ci_row.iloc[0]["upper"]
                else:
                    ci_lower, ci_upper = np.nan, np.nan

                if param.lower() == "intercept":
                    expb = expb_lower = expb_upper = np.nan
                else:
                    expb = np.exp(b)
                    expb_lower = np.exp(ci_lower) if not np.isnan(ci_lower) else np.nan
                    expb_upper = np.exp(ci_upper) if not np.isnan(ci_upper) else np.nan

                table_list.append([
                    f"{cat_str} {param_str}",
                    b,
                    se,
                    wald,
                    1,
                    "<0.001" if pval < 0.001 else f"{pval:.4g}",
                    expb,
                    expb_lower,
                    expb_upper
                ])

        df_table = pd.DataFrame(table_list, columns=[
            "Category/Variable", "B", "Std. Error", "Wald", "df", "Sig.",
            "Exp(B)", "Lower Bound", "Upper Bound"
        ])

        # Formatação
        df_table["B"] = df_table["B"].round(5)
        df_table["Std. Error"] = df_table["Std. Error"].round(5)
        df_table["Wald"] = df_table["Wald"].round(3)
        df_table["Exp(B)"] = df_table["Exp(B)"].round(3)
        df_table["Lower Bound"] = df_table["Lower Bound"].round(3)
        df_table["Upper Bound"] = df_table["Upper Bound"].round(3)

        mask_intercept = df_table["Category/Variable"].str.contains("Intercept", case=False)
        df_table.loc[mask_intercept, ["Exp(B)", "Lower Bound", "Upper Bound"]] = np.nan

        print("\n=== Tabela de Parâmetros Estimados ===")
        print(
            tabulate(
                df_table,
                headers="keys",
                tablefmt="grid",
                numalign="center"
            )
        )

    # ------------------------------------------------------------
    # 8) MATRIZ DE CONFUSÃO NO TREINO
    # ------------------------------------------------------------
    train_pred_probs = modelo_final.predict(train)
    train["predicted_class"] = train_pred_probs.idxmax(axis=1)

    if show_classification_table:
        y_true_train = train[col_resp_code]
        y_pred_train = train["predicted_class"]
        classes_unicas_train = sorted(list(set(y_true_train) | set(y_pred_train)))
        cmat_train = confusion_matrix(y_true_train, y_pred_train, labels=classes_unicas_train)

        print("\n=== MATRIZ DE CONFUSÃO (TREINO) ===")
        headers_train = ["Real\\Pred"] + [str(c) for c in classes_unicas_train] + ["Total"]
        rows_train = []
        for i, c_real in enumerate(classes_unicas_train):
            row = [str(c_real)] + list(cmat_train[i, :]) + [cmat_train[i, :].sum()]
            rows_train.append(row)
        col_sum_train = cmat_train.sum(axis=0)
        rows_train.append(["Total"] + list(col_sum_train) + [col_sum_train.sum()])

        print(tabulate(rows_train, headers=headers_train, tablefmt="grid"))

    # ------------------------------------------------------------
    # 8a) AUC no TREINO (multiclass)
    # ------------------------------------------------------------
    # Precisamos das probabilidades de todas as classes
    y_train = train[col_resp_code].values
    # Converte train_pred_probs em array [n, k]
    pred_probs_train = train_pred_probs.values
    auc_train, se_train, lower_train, upper_train = compute_auc_ci_multiclass_bootstrap(
        y_train,
        pred_probs_train,
        n_bootstraps=n_bootstraps,
        random_seed=random_state,
        multi_class=multi_class_method,
        average=average_method
    )

    # Para p-valor de H0: AUC=0.5, não existe uma analogia tão direta
    # em multiclasses. Vamos apenas fazer "teste se AUC = 0.5" via z = (AUC - 0.5)/SE
    # assumindo normalidade. É algo aproximado.
    if not np.isnan(se_train) and se_train > 0:
        z_train = (auc_train - 0.5) / se_train
        p_value_train = 2 * (1 - norm.cdf(abs(z_train)))
    else:
        p_value_train = np.nan

    # Mostra resultado da AUC no treino
    if do_validation or show_classification_table:
        print(f"\n=== AUC (Treino) - {multi_class_method} / {average_method} ===")
        print(f"AUC: {auc_train:.3f}, SE: {se_train:.3f}, 95%CI: [{lower_train:.3f}, {upper_train:.3f}], p-value={p_value_train:.4g}")

    # ------------------------------------------------------------
    # 9) MATRIZ DE CONFUSÃO E AUC NO TESTE
    # ------------------------------------------------------------
    auc_test = np.nan
    se_test = np.nan
    p_value_test = np.nan
    lower_test = np.nan
    upper_test = np.nan
    diff_auc = np.nan
    se_diff = np.nan
    p_diff = np.nan

    if do_validation and test is not None and len(test) > 0:
        test_pred_probs = modelo_final.predict(test)
        test["predicted_class"] = test_pred_probs.idxmax(axis=1)

        if show_classification_table:
            y_true_test = test[col_resp_code]
            y_pred_test = test["predicted_class"]
            classes_test = sorted(list(set(y_true_test) | set(y_pred_test)))
            cmat_test = confusion_matrix(y_true_test, y_pred_test, labels=classes_test)

            print("\n=== MATRIZ DE CONFUSÃO (TESTE) ===")
            headers_test = ["Real\\Pred"] + [str(c) for c in classes_test] + ["Total"]
            rows_test = []
            for i, c_real in enumerate(classes_test):
                row = [str(c_real)] + list(cmat_test[i, :]) + [cmat_test[i, :].sum()]
                rows_test.append(row)
            col_sum_test = cmat_test.sum(axis=0)
            rows_test.append(["Total"] + list(col_sum_test) + [col_sum_test.sum()])

            print(tabulate(rows_test, headers=headers_test, tablefmt="grid"))

        # AUC teste (multiclass)
        y_test = test[col_resp_code].values
        pred_probs_test = test_pred_probs.values
        auc_test, se_test, lower_test, upper_test = compute_auc_ci_multiclass_bootstrap(
            y_test,
            pred_probs_test,
            n_bootstraps=n_bootstraps,
            random_seed=random_state,
            multi_class=multi_class_method,
            average=average_method
        )

        if not np.isnan(se_test) and se_test > 0:
            z_test = (auc_test - 0.5) / se_test
            p_value_test = 2 * (1 - norm.cdf(abs(z_test)))
        else:
            p_value_test = np.nan

        print(f"\n=== AUC (Teste) - {multi_class_method} / {average_method} ===")
        print(f"AUC: {auc_test:.3f}, SE: {se_test:.3f}, 95%CI: [{lower_test:.3f}, {upper_test:.3f}], p-value={p_value_test:.4g}")

        # --------------------------------------------------------
        # Diferença entre AUC de treino e teste
        # --------------------------------------------------------
        # Aproximação: se_diff = sqrt(se_train^2 + se_test^2)
        # p_diff => z = diff/se_diff
        if not np.isnan(se_train) and not np.isnan(se_test):
            diff_auc = auc_train - auc_test
            se_diff = np.sqrt(se_train**2 + se_test**2)
            if se_diff > 0:
                z_diff = diff_auc / se_diff
                p_diff = 2 * (1 - norm.cdf(abs(z_diff)))

        print(f"\n=== Comparação AUC Treino vs Teste ===")
        print(f"Diff (train - test) = {diff_auc:.3f}, SE={se_diff:.3f}, p_diff={p_diff:.4g}")
        if not np.isnan(se_diff) and se_diff > 0:
            # IC da diferença
            z975 = norm.ppf(0.975)
            diff_lower = diff_auc - z975 * se_diff
            diff_upper = diff_auc + z975 * se_diff
            print(f"IC 95% da diferença: [{diff_lower:.3f}, {diff_upper:.3f}]")

    elif do_validation and (test is None or len(test) == 0):
        print("\nAviso: Após split, a amostra de teste ficou vazia. Não foi possível validar.")

    # ------------------------------------------------------------
    # Retorno
    # ------------------------------------------------------------
    return {
        "modelo_saturado": modelo_saturado,
        "modelo_final": modelo_final,
        "predictors_final": adjusted_predictors,
        "df_train": train,
        "df_test": test,
        "map_categories": cat_map,
        "col_resp_code": col_resp_code,
        "auc_train": (auc_train, se_train, lower_train, upper_train, p_value_train),
        "auc_test": (auc_test, se_test, lower_test, upper_test, p_value_test),
        "diff_auc": (diff_auc, se_diff, p_diff),
        "multi_class_method": multi_class_method,
        "average_method": average_method
    }