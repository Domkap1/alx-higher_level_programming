#!/usr/bin/node
const { dict } = require('./101-data.js');
let newDict = {};
for (let key in dict) {
	if (!newDict[dict[key]]) {
		newDict[dict[key]] = [];
	}
	newDict[dict[key]].push(parseInt(key));
}
console.log(newDict);
