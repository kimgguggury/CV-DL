import matplotlib.pyplot as plt
import numpy as np

# X 값 설정 (부드러운 곡선을 위해 linspace 사용)
X = np.linspace(-10, 10, 1000)  # -10부터 10까지 1000개 점 생성
sigma = 1  # 표준편차
mu = 0     # 평균

# 1차원 가우시안 함수 공식 적용
Y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(- (X - mu)**2 / (2 * sigma**2))

# 그래프 그리기
plt.plot(X, Y, label="Gaussian Function (σ=1)")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("1D Gaussian Function")
plt.legend()
plt.show()