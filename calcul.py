table = [(0.0009765625, 0.44618),
         (0.001953125,  0.99663),
         (0.00263671875,0.20843),
         (0.00390625,	2.4081),
         (0.0052734375,	0.44703),
         (0.00703125,	0.58853),
         (0.0078125,	3.3163),
         (0.009375,	0.76831),
         (0.0125,	1.0275),
         (0.015625,	3.9781),
         (0.025,	2.221),
         (0.03125,	3.2763)]

import torch
import numpy

XY = torch.FloatTensor(table).t()
X = torch.autograd.Variable(XY[0], requires_grad=False)
Y = torch.autograd.Variable(XY[1], requires_grad=False)


class LinearRegression:
    def get_loss(self, preds, y):
        """
            @param preds: предсказания модели
            @param y: истиные значения
            @return mse: значение MSE на переданных данных
        """
        # возьмите средний квадрат ошибки по всем выходным переменным
        # то есть сумму квадратов ошибки надо поделить на количество_элементов * количество_таргетов
        minus = (preds - y) ** 2
        return torch.sum(minus) / minus.numel()

    def init_weights(self, input_size, output_size):
        """
            Инициализирует параметры модели
            W - матрица размерности (input_size, output_size)
            инициализируется рандомными числами из
            uniform распределения (torch.rand())
            b - вектор размерности (1, output_size)
            инициализируется нулями
        """
        torch.manual_seed(0)
        self.W = torch.autograd.Variable(torch.FloatTensor([90]), requires_grad=True)

    def fit(self, X, y, num_epochs=1000, lr=0.001):
        """
            Обучение модели линейной регрессии методом градиентного спуска
            @param X: размерности (num_samples, input_shape)
            @param y: размерности (num_samples, output_shape)
            @param num_epochs: количество итераций градиентного спуска
            @param lr: шаг градиентного спуска
            @return metrics: вектор значений MSE на каждом шаге градиентного
            спуска.
        """
        self.init_weights(X.shape[0], y.shape[1])
        metrics = []
        for _ in range(num_epochs):
            preds = self.predict(X)
            # сделайте вычисления градиентов c помощью Pytorch и обновите веса
            # осторожнее, оберните вычитание градиента в
            #                 with torch.no_grad():
            #                     #some code
            # иначе во время прибавления градиента к переменной создастся очень много нод в дереве операций
            # и ваши модели в будущем будут падать от нехватки памяти
            # YOUR_CODE
            # YOUR_CODE
            self.get_loss(preds, y).backward()
            with torch.no_grad():
                self.W -= self.W.grad * lr
            self.W.grad.data.zero_()
            metrics.append(self.get_loss(preds, y).data)
        return metrics

    def predict(self, X):
        """
            Думаю, тут все понятно. Сделайте свои предсказания :)
        """
        return X * self.W