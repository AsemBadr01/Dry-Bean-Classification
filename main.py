from UI.GUI import window

window.mainloop()

# # -------------------make this code a function in DynamicFunctions.py and remove the print lines------------------#
#
# # print(X_test.columns)
# # print(feature1_index)
# # print(feature2_index)
#
# feature1 = X_test.iloc[:, 0]
# # print(feature1)
# feature2 = X_test.iloc[:, 1]
# # print(feature2)
#
# plt.scatter(feature1[y_test == 1], feature2[y_test == 1], label='Class 1', c='b', marker='o')
#
# plt.scatter(feature1[y_test == -1], feature2[y_test == -1], label='Class -1', c='r', marker='x')
#
# x_values = np.linspace(feature1.min() - 1, feature1.max() + 1, 100)
#
# y_values = (-weights[0] * x_values - trained_bias) / weights[1]
#
# plt.plot(x_values, y_values, 'g--', label='Decision Boundary')
#
# plt.xlabel(f'Feature {0}')
# plt.ylabel(f'Feature {1}')
# plt.legend(loc='best')
#
# plt.show()
