# import visdom
# import matplotlib.pyplot as plt
# vis = visdom.Visdom()

# # Loss goes does!
# plt.plot([2.0, 1.0, 0.0], c="blue")
# plt.title("Model Loss")

# # Send to visdom
# vis.matplot(plt, win="loss")

from project.datasets import Simple, Split, Xor
N = 100
Simple(N, vis=True).graph("initial")

def classify(pt):
    "Classify based on x position"
    if pt[0] > 0.5:
        return 1.0
    else:
        return 0.0

Split(N, vis=True).graph("initial", model=classify)