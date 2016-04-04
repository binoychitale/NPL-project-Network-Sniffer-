
import plotly.plotly as py
import plotly.graph_objs as go
from collections import OrderedDict
def main():
    f = open('C:\\PerfLogs\\trace.txt')
    data = f.read().split('\n')
    sources={}
    pairs={}
    destinations={}
    protocols={}
    times = {}
    tbrackets=OrderedDict()
    IPtimes=OrderedDict()
    selected=raw_input("Enter IP to analyze traffic from")
    print(len(data)-2)
    for i in range(len(data)-2):
        vals=data[i].split(' ')
        temp = vals[0]
        timestamp = temp[:8]
        src = vals[2]
        isrc=src.rfind('.')
        src=src[:isrc]
        dest = vals[4]
        idst=dest.rfind('.')
        dest=dest[:idst]
        protocol = vals[5]
        pair = src+vals[3]+dest
        tmin=timestamp[:5]
        if vals[1] == 'arp':
            if 'arp' in protocols:
                protocols['arp']+=1
            else:
                protocols['arp']=1
            continue
        if timestamp in times:
            times[timestamp]+=1
        else:
            times[timestamp]=1
        if src in sources:
            sources[src]+=1
        else:
            sources[src]=1
        if pair in pairs:
            pairs[pair]+=1
        else:
            pairs[pair]=1
        if dest in destinations:
            destinations[dest]+=1
        else:
            destinations[dest]=1
        if protocol in protocols:
            protocols[protocol]+=1
        else:
            protocols[protocol]=1
        if tmin in tbrackets:
            tbrackets[tmin]+=1
        else:
            tbrackets[tmin]=1
        if src==selected or dest==selected:
            if tmin in IPtimes:
                IPtimes[tmin]+=1
            else:
                IPtimes[tmin]=1
    print(IPtimes)
    #print(data)
    '''print(tbrackets)
    dat = [
    go.Bar(
        x=sources.keys(),
        y=sources.values()
    )
    ]
    plot_url = py.plot(dat, filename='basic-bar')
    fig = {
        'data': [{'labels': sources.keys(),
                'values': sources.values(),
                'type': 'pie'}],
        'layout': {'title': 'IP Source Distribution'}
    }

    url = py.plot(fig, filename='Pie Chart Example')
    fig1 = {
        'data': [{'labels': protocols.keys(),
                'values': protocols.values(),
                'type': 'pie'}],
        'layout': {'title': 'Protocol Distribution'}
    }
    url1 = py.plot(fig1, filename='Pie Chart Example')
    dat2 = [
    go.Scatter(
        x=tbrackets.keys(),
        y=tbrackets.values()

    )
    ]
    plot_url1 = py.plot(dat2, filename='python-datetime1')
    dat1 = [
    go.Bar(
        x=sources.keys(),
        y=sources.values()

    ),
        go.Bar(
        x=destinations.keys(),
        y=destinations.values()

    )
    ]
    plot_url = py.plot(dat1, filename='python-datetime')'''
    dat2 = [
    go.Scatter(
        x=IPtimes.keys(),
        y=IPtimes.values()

    )
    ]
    plot_url1 = py.plot(dat2, filename='python-datetime1')
main()