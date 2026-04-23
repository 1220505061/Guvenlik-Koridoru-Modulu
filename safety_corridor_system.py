import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm


class ObstacleGenerator:
    """
    Otonom araç için 2 boyutlu düzlemde engel koordinatları üreten sınıf.
    """

    def __init__(self, seed=42):
        np.random.seed(seed)

    def generate_data(self, n_samples=20):
        """
        Doğrusal olarak ayrılabilen iki farklı engel sınıfı üretir.
        """
        # Sınıf 1: Engel Grubu A (Sol alt bölge)
        class_a = np.random.uniform(low=1, high=4, size=(n_samples, 2))

        # Sınıf 2: Engel Grubu B (Sağ üst bölge)
        class_b = np.random.uniform(low=6, high=9, size=(n_samples, 2))

        return class_a, class_b


class SafetyCorridorModel:
    """
    Maksimum marjinli (en güvenli) ayrıştırıcıyı hesaplayan sınıf.
    """

    def __init__(self):
        # Linear SVM: En yakın koordinatlara uzaklığı maksimum olan çizgiyi bulur.
        self.model = svm.SVC(kernel='linear', C=1000)
        self.w = None
        self.b = None

    def fit(self, class_a, class_b):
        # Verileri birleştirme ve etiketleme (A: -1, B: 1)
        X = np.vstack((class_a, class_b))
        y = np.hstack((np.ones(len(class_a)) * -1, np.ones(len(class_b))))

        # Modeli eğitme
        self.model.fit(X, y)
        self.w = self.model.coef_[0]
        self.b = self.model.intercept_[0]


class Visualizer:
    """
    Sonuçları ve güvenlik koridorunu görselleştiren sınıf.
    """

    @staticmethod
    def plot_all(class_a, class_b, model):
        plt.figure(figsize=(10, 8))

        plt.scatter(class_a[:, 0], class_a[:, 1], color='red', label='Engel A', edgecolors='k', s=60)
        plt.scatter(class_b[:, 0], class_b[:, 1], color='blue', label='Engel B', edgecolors='k', s=60)

        ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        xx = np.linspace(xlim[0], xlim[1], 30)
        yy = np.linspace(ylim[0], ylim[1], 30)
        YY, XX = np.meshgrid(yy, xx)
        xy = np.vstack([XX.ravel(), YY.ravel()]).T
        Z = model.model.decision_function(xy).reshape(XX.shape)

        ax.contour(XX, YY, Z, colors='darkgreen', levels=[-1, 0, 1], alpha=0.9,
                   linestyles=['--', '-', '--'], linewidths=[2, 3, 2])

        ax.scatter(model.model.support_vectors_[:, 0], model.model.support_vectors_[:, 1], s=150,
                   linewidth=1.5, facecolors='none', edgecolors='black', label='Destek Vektörleri')

        plt.title("Otonom Navigasyon - Maksimum Güvenlik Koridoru Analizi (SVM)")
        plt.xlabel("X Koordinatı (Metre)")
        plt.ylabel("Y Koordinatı (Metre)")
        plt.legend(loc='upper left')
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.show()

if __name__ == "__main__":

    generator = ObstacleGenerator()
    data_a, data_b = generator.generate_data(n_samples=15)

    safety_model = SafetyCorridorModel()
    safety_model.fit(data_a, data_b)

    print("Sistem Çalışıyor: Güvenlik koridoru ve en güvenli rota hesaplandı.")
    Visualizer.plot_all(data_a, data_b, safety_model)