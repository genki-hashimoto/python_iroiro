import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.mixture import GMM


def use_pca(dim,data):
	pca = PCA(dim)
	pca.fit(data)

	return pca.transform(data)


if __name__ == "__main__":
	iris = datasets.load_iris()
	feature = iris.data
	target = iris.target
	print(feature)
	print(iris.target)

	pca_result = use_pca(2,feature)
	print(pca_result)

	gmm = GMM(n_components=3, covariance_type="full")
	gmm.fit(pca_result)
	weights = gmm.weights_
	means = gmm.means_
	covars = gmm.covars_

	print("weights:")
	print(weights)
	print("means:")
	print(means)
	print("covars:")
	print(covars)

	print(gmm.covars_[0][0][0])

	for data,t in zip(pca_result,target):
		if t == 0:
			plt.plot(data[0],data[1],"ro")
		elif t == 1:
			plt.plot(data[0],data[1],"bo")
		else :
			plt.plot(data[0],data[1],"go")

	# 推定したガウス分布を描画
	x = np.linspace(-4, 4, 1000)
	y = np.linspace(-1.5, 1.5, 1000)
	X, Y = np.meshgrid(x, y)

	# 各ガウス分布について
	for k in range(3):
		# 平均を描画
		plt.plot(gmm.means_[k][0], gmm.means_[k][1], 'ro')
		# ガウス分布の等高線を描画
		Z = mlab.bivariate_normal(X, Y,
			np.sqrt(gmm.covars_[k][0][0]), np.sqrt(gmm.covars_[k][1][1]),
			gmm.means_[k][0], gmm.means_[k][1],
			gmm.covars_[k][0][1])
		plt.contour(X, Y, Z)

	# メッシュ上の各点での対数尤度の等高線を描画
	XX = np.array([X.ravel(), Y.ravel()]).T
	Z = gmm.score_samples(XX)[0]
	Z = Z.reshape(X.shape)
	CS = plt.contour(X, Y, Z)
	CB = plt.colorbar(CS)

	plt.xlim(-4, 4)
	plt.ylim(-1.5, 1.5)

	plt.show()
