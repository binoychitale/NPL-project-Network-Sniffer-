import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='binoychitale', api_key='teu3p3u7e4')
data = [
    go.Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[20, 14, 23]
    )
]
plot_url = py.plot(data, filename='basic-bar')