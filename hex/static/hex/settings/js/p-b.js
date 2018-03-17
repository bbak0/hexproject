var inputLtc = document.getElementById('input-ltc'),
inputBtc = document.getElementById('input-btc'),
fees = document.getElementById('fee'),
totals = document.getElementById('total');

var constantNumber = 408.79;
var feeConst = 0;
var tot = 0;

inputLtc.onkeyup = function() {
var result = parseFloat((inputLtc.value) / constantNumber).toFixed(5);
inputBtc.value = !isNaN(result) ? result : '';

feeConst = parseFloat(inputLtc.value / constantNumber * 0.04).toFixed(5);
fees.innerHTML = feeConst + ' Byteball';

tot = parseFloat(inputLtc.value / constantNumber + inputLtc.value / constantNumber * 0.04).toFixed(5);
totals.innerHTML = tot + ' Byteball';

};