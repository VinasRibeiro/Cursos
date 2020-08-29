let number = 12354987,
    output = [],
    sNumber = number.toString();

for (let i = 0, len = sNumber.length; i < len; i += 1) {
    output.push(+sNumber.charAt(i));
}

console.log(output);