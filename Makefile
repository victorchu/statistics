#
# Makefile for launching Jupyter
#

JUPYTER = jupyter
IPYTHON3 = ipython

default: j

j:
	$(JUPYTER) notebook

p3:
	$(IPYTHON3) notebook

p2:
	$(IPYTHON2) notebook


