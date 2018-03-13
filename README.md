# AttribDict


You may use the following syntax to change or access data in this class.

```
>>> stats = AttribDict()
>>> stats.network = 'BW'
>>> stats['station'] = 'ROTZ'
>>> print(stats.get('network'))
BW
>>> print(stats['network'])
BW
>>> print(stats.station)
ROTZ
>>> x = stats.keys()
>>> x = sorted(x)
>>> print(x[0], x[1])
network station
```
