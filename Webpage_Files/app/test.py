from machine_learning import predict, loaded_model

predict = predict(loaded_model, "Khabib Nurmagomedov", "Tony Ferguson")
print(int(round(predict[0][0] * 100)))
