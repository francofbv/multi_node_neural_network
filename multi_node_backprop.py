# constants
num_nodes = 5
max_iterations = 10
learning_rate = 0.1
start = 9

# variables
w_0 = w_1 = w_2 = w_3 = 0.8
a_0 = a_1 = a_2 = a_3 = a_4 = 0

# defining functions

def mean_sqrd_err(a, y): # cost function 
    return (a - y) ** 2

def mean_sqrd_err_drv(a, y): # dC/da
    return 2 * (a - y)

# a = i * w, therefore, the derivative with respect to w is just i (the input)
def output_derivative(i): # da/dw
    return i

# the derivative of the cost function with respect to a given weight (dC/dw) = da/dw * dC/da
def dC_dw(w):
    return 4.5 * w - 1.5

def gradient_descent(max_iterations, start, learning_rate): # modifies the value of x to minimize the function
    x = start
    for _ in range(max_iterations):
        x = x - learning_rate * (dC_dw(x))
    return x



