import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X)


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrow_props = dict(arrowstyle='->', linewidth=2, shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrow_props)


plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v)
plt.axis('eq')

pca = PCA(n_components=1)
pca.fit(X)
X_pca = pca.transform(X)
X_new = pca.inverse_transform(X_pca)

from sklearn.datasets import load_digits

digits = load_digits()
pca = PCA(2)
projected = pca.fit_transform(digits.data)
plt.scatter(projected[:, 0], projected[:, 1], c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('spectral', 10))


def plot_digits(data):
    fig, axes = plt.subplots(4, 10, figsize=(10, 4), subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(8, 8), cmap='binary', interpolation='nearest', clim=(0, 16))


plot_digits(digits.data)

# np.random.seed(42)
# noisy = np.random.normal(digits.data, 4)
# plot_digits(noisy)
# pca = PCA(0.50).fit(noisy)
# components = pca.transform(noisy)
# filtered = pca.inverse_tarnsform(components)

from sklearn.datasets import fetch_lfw_people

faces = fetch_lfw_people(min_faces_per_person=60)
from sklearn.decomposition import SparsePCA

pca = SparsePCA(150)
pca.fit(faces.data)
fig, axes = plt.subplots(3, 8, figsize=(9, 4), subplot_kw={'xticks': [], 'yticks': []},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')

pca=SparsePCA(150).fit(faces.data)
components=pca.transform(faces.data)
projected=pca.inverse_transform(components)
fig,ax=plt.subplots(2,10,figsize=(10,2.5),subplot_kw={'xticks':[],'yticks':[]},gridspec_kw=dict(hspace=0.1,wspace=0.1))
for i in range(10):
    ax[0,i].imshow(faces.data[i].reshape(62,47),cmap='binary_r')
    ax[1,i].imshow(projected[i].reshape(62,47),cmap='binary_r')
