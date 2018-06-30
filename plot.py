import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
import plotly.figure_factory as FF



def run_1(x_a,y_a):
    trace1 = go.Scatter(
        x=x_a,
        y=y_a
        )

    layout = go.Layout(
        title='世界杯参赛队强对抗胜率参考',
        hovermode='closest',
        xaxis=dict(
            title='胜率',
            showline=True),
        yaxis=dict(
            title='进失球比',
            showline=True))
    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)
if __name__ == '__main__':
    df = pd.read_csv('china.csv')
    data = FF.create_table(df)
    y_a = (df['胜场'] / df['总场次']) * 100
    x_a = df['排名范围']
    run_1(x_a,y_a)

