#!/usr/bin/node

exports.esrever = function (list) {
  let leng = list.length - 1;
  let numi = 0;
  while ((leng - numi) > 0) {
    const auxil = list[leng];
    list[leng] = list[numi];
    list[numi] = auxil;
    numi++;
    leng--;
  }
  return list;
};
