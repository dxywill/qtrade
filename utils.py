from datetime import datetime
import plotly.graph_objects as go


def plot_k(df, start, end, skip=1):
    df = df.loc[start:end]
    opens = df.open.tolist()
    closes = df.close.tolist()
    highs = df.high.tolist()
    lows = df.low.tolist()
    #ticks = [datetime.strptime(date, "%Y-%m-%d") for date in df.index]
    xticks = ["{}/{}".format(t.month, t.day) for t in df.index]
    xx = list(range(len(df.index)))
    fig = go.Figure(data=[go.Candlestick(x=xx,
                open=df.open,
                high=df.high,
                low=df.low,
                close=df.close)])

    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = xx[::skip],
            ticktext = xticks[::skip]
        )
    )
    cs = fig.data[0]

    # Set line and fill colors
    # cs.increasing.fillcolor = '#3D9970'
    # cs.increasing.line.color = '#3D9970'
    # cs.decreasing.fillcolor = '#FF4136'
    # cs.decreasing.line.color = '#FF4136'

    cs.increasing.fillcolor = '#FF4136'
    cs.increasing.line.color = '#FF4136'
    cs.decreasing.fillcolor = '#3D9970'
    cs.decreasing.line.color = '#3D9970'

    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()