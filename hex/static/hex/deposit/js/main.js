$(document).ready(function () {
    $('.card-exp').mask("00/00", {
        placeholder: "MM/YY"
    });
    $('.card-num').mask("9999   9999   9999   9999", {
        placeholder: "Card number"
        
    });
    $('.money-inp').mask('£ Z99.99', {
        translation: {
            'Z': {
                pattern: /[0-4]/
            }
        },
        placeholder: 'Amount',
        selectOnFocus: true
    });


    var mn = document.getElementById('money-inp');

    mn.onkeyup = function () {
        var val = mn.value;
        var valueTrue = val.substr(2);

        var valInt = parseFloat(valueTrue ? valueTrue : 0.00).toFixed(2);

        var progr = document.getElementById('progr-bar');

        if (valInt == 0) {
            progr.style.width = '0%';
        } else if (valInt == 499.99) {
            progr.style.width = '100%';
        } else {
            var proc = parseFloat(valInt / 500 * 100).toFixed(1);

            progr.style.width = proc + '%';
        }

        var fee = document.getElementById('fees');
        var subtotal = document.getElementById('subtotals');
        var total = document.getElementById('totals');

        fee.innerHTML = parseFloat(valInt * 0.04).toFixed(2) + ' Pound';
        subtotal.innerHTML = parseFloat(valInt).toFixed(2) + ' Pound';

        var tot1 = parseFloat(valInt * 0.04).toFixed(2);
        var tot2 = parseFloat(valInt).toFixed(2);

        var tot3 = parseFloat(+tot1 + +tot2).toFixed(2);
        
        total.innerHTML = parseFloat(tot3).toFixed(2) + ' Pound';

        var rem = document.getElementById('remain');

        rem.innerHTML = '£' + parseFloat(500.00 - valInt).toFixed(2) + ' Remaining';
    }
});

//  var dep1 = document.getElementById('b-btn');
var chk1 = document.getElementById('b-check');
var in1 = document.getElementById('inf1');
var bf1 = document.getElementById('b-form');
var l1 = document.getElementById('lb1');

var chk2 = document.getElementById('b-check2');
var in2 = document.getElementById('inf2');
var bf2 = document.getElementById('b-form2');
var l2 = document.getElementById('lb2');

var chk3 = document.getElementById('b-check3');
var in3 = document.getElementById('inf3');
var bf3 = document.getElementById('b-form3');
var l3 = document.getElementById('lb3');

var chk4 = document.getElementById('b-check4');
var in4 = document.getElementById('inf4');
var bf4 = document.getElementById('b-form4');
var l4 = document.getElementById('lb4');

$('#b-btn').click(function () {   
    if (chk1.checked) {
        in1.style.display = "none";
        bf1.style.display = "block";
        $('#lb1').removeClass('err');
    } else {
        $('#lb1').addClass('err');
    }
});

$('#b-btn2').click(function () {   
    if (chk2.checked) {
        in2.style.display = "none";
        bf2.style.display = "block";
        $('#lb2').removeClass('err');
    } else {
        $('#lb2').addClass('err');
    }
});

$('#b-btn3').click(function () {   
    if (chk3.checked) {
        in3.style.display = "none";
        bf3.style.display = "block";
        $('#lb3').removeClass('err');
    } else {
        $('#lb3').addClass('err');
    }
});

$('#b-btn4').click(function () {   
    if (chk4.checked) {
        in4.style.display = "none";
        bf4.style.display = "block";
        $('#lb4').removeClass('err');
    } else {
        $('#lb4').addClass('err');
    }
});

$(function() {
	var Accordion = function(el, multiple) {
		this.el = el || {};
		this.multiple = multiple || false;

		// Variables privadas
		var links = this.el.find('.link');
		// Evento
		links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
	}

	Accordion.prototype.dropdown = function(e) {
		var $el = e.data.el;
			$this = $(this),
			$next = $this.next();

		$next.slideToggle();
		$this.parent().toggleClass('open');

		if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
            
            setTimeout(function(){
                in1.style.display = "block";
                bf1.style.display = "none";
                $('#lb1').removeClass('err');
                chk1.checked = false;

                in2.style.display = "block";
                bf2.style.display = "none";
                $('#lb2').removeClass('err');
                chk2.checked = false;

                in3.style.display = "block";
                bf3.style.display = "none";
                $('#lb3').removeClass('err');
                chk3.checked = false;

                in4.style.display = "block";
                bf4.style.display = "none";
                $('#lb4').removeClass('err');
                chk4.checked = false;
            }, 400);
		};
	}	

	var accordion = new Accordion($('#accordion'), false);
});


$('#card-btn').click(function () {
    $('#sec-btn').css('display', 'none');
    $('#card-cert').css('display', 'block');
});

$('#bank-btn').click(function () {
    $('#sec-btn').css('display', 'none');
    $('#bank-cert').css('display', 'block');
});