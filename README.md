# MiniTorch Module 0  

<img src="https://minitorch.github.io/_images/match.png" width="100px">

* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module0.html

* Tests:

```
python run_tests.py
```

Or test a single file:

```
python -m pytest tests/test_operators.py
```

* Visualization:

I'm running all the codes on a remote server, so displaying Viszom requires an extra port forwarding step:

On server, run:

```
visdom 2> error.log &
```

On local terminal, run:

```
ssh -N -f -L localhost:8888:localhost:8097 myname@server
```

Ajust the port based on your actual server ports, then you can open localhost:8888 to see the plots.

