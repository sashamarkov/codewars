function evaluate(left, op, right) {
    const ops = {
        add: (a, b) => a + b,
        subtract: (a, b) => a - b,
        multiply: (a, b) => a * b,
        divide: (a, b) => a / b
    };
    
    const reduceOperand = (operand) => {
        const rootOp = Object.keys(operand)[0];
        const arr = operand[rootOp];
        const values = [
            arr.add?.reduce(ops.add, 0),
            arr.subtract?.reduce(ops.subtract),
            arr.multiply?.reduce(ops.multiply, 1),
            arr.divide?.reduce(ops.divide)
        ].filter(val => val !== undefined);
        return values.reduce((result, val, i) => i ? ops[rootOp](result, val) : val);
    };
    return ops[op](reduceOperand(left), reduceOperand(right));
}