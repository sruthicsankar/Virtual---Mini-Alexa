from datetime_utils import get_current_hour

def recommend_activity():
    hour = get_current_hour()
    if 5 <= hour < 11:
        activity = "Breakfast"
    elif 11<= hour<14:
        activity  = "Lunch"
    elif 14 <= hour < 17:
        activity = "A Break"
    elif 17 <= hour< 21:
        activity = "Dinner"
    else:
        activity = "Touch Grass"

    return (
        f"Assistant: Based on the time right now, Id recommend {activity}.\n"
        # No  LEARNING USED 
    )

def run_perceptron_demo():
    print("Assistant: Let's a mini 'neuron ' calculation.I will ask 3 Numbers,")
    print("Assistant: Multiply each by a fixed weight, add a bias, then decide 0 or 1.")
    inputs = []

    for i in range(1,4):
        while True:
            raw = input(f"Assistant: Enter input #{i} ( a number):").strip()
            try:
                inputs.append(float(raw))
                break
            except ValueError:
                print("Assistant: That's not a number -- please try again")

    weights = [0.4,0.3,0.3]
    bias = -0.5

    weighted_sum = sum(x*w for x,w  in zip(inputs,weights)) + bias
    output = 1 if weighted_sum  > 0 else 0

    print(f" Assistant: Weighted Sum = {weighted_sum:.2f}")
    print(f"Assistant: Step Activation output = {output}")
    print(40*"/")
    print(
        "Assistant: This mirror forward propagation in a real neuron:"
        "Inputs -> weights/bias -> activation -> output"
    )
    # print(40*"/")
    return output

def run_hidden_layer_demo(first_output):
    weight = 0.6
    bias = 0.1
    weighted_sum = (first_output*weight)+ bias
    output = 1 if weighted_sum > 0 else 0
    print(f"Assistant: Feeding that output into a second neuron (hidden layer) ... ")
    print(f"Assistant: Second Neuron Output = {output}")
    print("Assistant: This is how layering works: One neuron's output becomes the next one's input")
    return output
