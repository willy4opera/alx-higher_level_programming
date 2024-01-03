t #!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const val = Object.values(dict);
const Uniqval = [...new Set(val)];
const NewDict = {};
for (const numj in Uniqval) {
  const list = [];
  for (const numk in totalist) {
    if (totalist[numk][1] === Uniqval[numj]) {
      list.unshift(totalist[numk][0]);
    }
  }
  NewDict[Uniqval[numj]] = list;
}
console.log(NewDict);
