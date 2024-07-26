# feels-like

Parses https://www.theweathernetwork.com/en/city/ca/ontario/toronto/hourly to see what the "feels like" temperature is between 7pm-10pm over the next three days.

Example:

```
python main.py
```

```
Day: Fri Jul 26, Time: 7pm, Feels Like: 27 °C
Day: Fri Jul 26, Time: 8pm, Feels Like: 27 °C
Day: Fri Jul 26, Time: 9pm, Feels Like: 24 °C
Day: Sat Jul 27, Time: 7pm, Feels Like: 29 °C
Day: Sat Jul 27, Time: 8pm, Feels Like: 29 °C
Day: Sat Jul 27, Time: 9pm, Feels Like: 26 °C
Day: Sun Jul 28, Time: 7pm, Feels Like: 33 °C
Day: Sun Jul 28, Time: 8pm, Feels Like: 32 °C
Day: Sun Jul 28, Time: 9pm, Feels Like: 31 °C
```

Note that each time refers to a one hour period beginning at the indicated time. For example, 7pm means 7pm-8pm.
