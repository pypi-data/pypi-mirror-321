from Babaji import HeightPredictor,DiabeticPredictor

# # Initialize the predictor (no need to pass URLs)
# predictor = HeightPredictor()

# # Predict height for a given weight
#   # Example input
# predicted_height = predictor.predict(78)
# print(predicted_height)

model = DiabeticPredictor()
print(model.predict([1,2,3,4,5,6,67,8]))