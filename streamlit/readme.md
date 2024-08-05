run: streamlit run app.py

### Text Elements (Elementos de Texto)

* `st.title()`: Título grande.
* `st.header()`: Cabeçalho.
* `st.subheader()`: Subcabeçalho.
* `st.text()`: Texto simples.
* `st.markdown()`: Texto em Markdown.
* `st.caption()`: Texto pequeno e de legenda.
* `st.latex()`: Fórmulas matemáticas em LaTeX.
* `st.code()`: Blocos de código.
* `st.write()`: Texto e dados em diversos formatos (autoformatação).

### Data Display Elements (Elementos de Exibição de Dados)

* `st.dataframe()`: DataFrame interativo.
* `st.table()`: Tabela estática.
* `st.json()`: Visualizador de JSON.
* `st.metric()`: Métricas simples com delta.

### Media Elements (Elementos de Mídia)

* `st.image()`: Exibição de imagens.
* `st.audio()`: Reprodução de áudio.
* `st.video()`: Reprodução de vídeo.

### Chart Elements (Elementos de Gráficos)

* `st.line_chart()`: Gráfico de linha.
* `st.area_chart()`: Gráfico de área.
* `st.bar_chart()`: Gráfico de barras.
* `st.pyplot()`: Gráficos Matplotlib.
* `st.altair_chart()`: Gráficos Altair.
* `st.vega_lite_chart()`: Gráficos Vega-Lite.
* `st.plotly_chart()`: Gráficos Plotly.
* `st.bokeh_chart()`: Gráficos Bokeh.
* `st.deck_gl_chart()`: Gráficos Deck.GL.
* `st.graphviz_chart()`: Gráficos Graphviz.

### Input Widgets (Widgets de Entrada)

* `st.button()`: Botão.
* `st.download_button()`: Botão de download.
* `st.checkbox()`: Caixa de seleção.
* `st.radio()`: Botões de rádio.
* `st.selectbox()`: Caixa de seleção (drop-down).
* `st.multiselect()`: Caixa de seleção múltipla.
* `st.slider()`: Controle deslizante.
* `st.select_slider()`: Controle deslizante de seleção.
* `st.text_input()`: Campo de texto.
* `st.text_area()`: Área de texto.
* `st.number_input()`: Campo de entrada numérica.
* `st.date_input()`: Selecionador de data.
* `st.time_input()`: Selecionador de hora.
* `st.file_uploader()`: Upload de arquivos.
* `st.color_picker()`: Seletor de cores.

### Layout and Containers (Layout e Contêineres)

* `st.container()`: Container para agrupar elementos.
* `st.columns()`: Layout em colunas.
* `st.expander()`: Seção expansível.
* `st.sidebar()`: Barra lateral.

### Control Flow (Controle de Fluxo)

* `st.stop()`: Para a execução do código.
* `st.form()`: Formulário.
* `st.form_submit_button()`: Botão de submissão de formulário.

### Status Elements (Elementos de Status)

* `st.spinner()`: Spinner (carregamento).
* `st.progress()`: Barra de progresso.
* `st.success()`: Mensagem de sucesso.
* `st.info()`: Mensagem informativa.
* `st.warning()`: Mensagem de aviso.
* `st.error()`: Mensagem de erro.
* `st.exception()`: Exibição de exceções.

### Experimental Features (Recursos Experimentais)

* `st.experimental_rerun()`: Reinicializa o script.
* `st.experimental_singleton()`: Cache singleton.
* `st.experimental_memo()`: Cache memo.

### Utilitários

* `st.session_state`: Estado da sessão.
* `st.cache_data()`: Cache de dados.
* `st.cache_resource()`: Cache de recursos.
