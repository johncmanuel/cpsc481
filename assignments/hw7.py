def perceptron_output(inputs, weights, bias):
    terms = [f"{x}*{w}" for x, w in zip(inputs, weights)]
    activation = sum(x * w for x, w in zip(inputs, weights)) + bias
    expression = " + ".join(terms)
    expression += f" + {bias}"
    print(f"Activation function: {expression} = {activation}")
    return 1 if activation >= 0 else 0


data = [(5, 1, 3), (6, 0, 2), (4, 0, 2), (5, 1, 3), (5, 0, 2)]

# weights = [-5, 13, 14]
weights = [[-5, 13, 14], [0, 0, 0], [-6, 0, -2], [0, 0, 0], [0, 0, 0]]
assert len(weights) == len(data), "Weights and data must have the same length"
bias = 0

# for input_vec in data:
for input_vec, weight in zip(data, weights):
    prediction = perceptron_output(input_vec, weight, bias)
    print(f"Input: {input_vec}, Prediction: {prediction}")
