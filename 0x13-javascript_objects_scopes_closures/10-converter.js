#!/usr/bin/node
exports.converter = function (base) {
    return function convert(number) {
        if (number === 0) return '0';
        function recurse(n) {
            return n === 0 ? '' : recurse(Math.floor(n / base)) + (n % base).toString(base);
        }
        return recurse(number);
    }
}
