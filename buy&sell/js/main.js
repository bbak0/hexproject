$('.card-receive').click(function () {
    var card = document.getElementsByClassName('card-receive');
    var length = card.length;
    
    for (let index = 0; index < card.length; index++) {
        $(card[index]).removeClass('active-card');
        // card[index].removeClass('active-card');
    }

    var card2 = document.getElementsByClassName('card-receive2');
    var length2 = card2.length;
    
    for (let index2 = 0; index2 < card2.length; index2++) {
        $(card2[index2]).removeClass('active-card');
    }

    var card3 = document.getElementsByClassName('card-receive3');
    var length3 = card3.length;
    
    for (let index3 = 0; index3 < card3.length; index3++) {
        $(card3[index3]).removeClass('active-card');
    }

    var pt = document.getElementsByClassName('point');

    var getTotalPoints = $('.point').length,
    getIndex = $(pt[1]).index(),
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: (getIndex - 1) / (getTotalPoints - 1) * 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $(pt[1]).addClass('point--active');
    $(pt[1]).prevAll().addClass('point--complete');
    $(pt[1]).nextAll().removeClass('point--complete');
  }

    // $(this).css('background', '#37BC9B');
    // $(this).css('color', 'white');
    $(this).addClass('active-card');
    $('#from').css('display', 'none');

    if (this.classList.contains('pound')) {
        var cont = document.getElementById('not-pound');

        cont.style.display = 'none';

        var cont2 = document.getElementById('with-pound');

        cont2.style.display = 'block';
        
    } else {
        var cont3 = document.getElementById('with-pound');

        cont3.style.display = 'none';

        var cont4 = document.getElementById('not-pound');

        cont4.style.display = 'block';
    }
});

$('.card-receive2').click(function () {
    var card = document.getElementsByClassName('card-receive2');
    var length = card.length;
    
    for (let index = 0; index < card.length; index++) {
        card[index].style.background = 'white';
        card[index].style.color = '#333333c8';
        $(card[index]).removeClass('active-card');
        // card[index].removeClass('active-card');
    }

    var card2 = document.getElementsByClassName('card-receive2');
    var length2 = card2.length;
    
    for (let index2 = 0; index2 < card2.length; index2++) {
        card2[index2].style.background = 'white';
        card2[index2].style.color = '#333333c8';
        $(card[index2]).removeClass('active-card');
    }

    var card3 = document.getElementsByClassName('card-receive3');
    var length3 = card3.length;
    
    for (let index3 = 0; index3 < card3.length; index3++) {
        card3[index3].style.background = 'white';
        card3[index3].style.color = '#333333c8';
        $(card[index3]).removeClass('active-card');
    }

    var pt = document.getElementsByClassName('point');

    var getTotalPoints = $('.point').length,
    getIndex = $(pt[2]).index(),
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $(pt[2]).addClass('point--active');
    $(pt[2]).prevAll().addClass('point--complete');
    $(pt[2]).nextAll().removeClass('point--complete');
  }

    // $(this).css('background', '#37BC9B');
    // $(this).css('color', 'white');
    $(this).addClass('active-card');

    $('#from').css('display', 'block');
});

$('.card-receive3').click(function () {
    var card = document.getElementsByClassName('card-receive3');
    var length = card.length;
    
    for (let index = 0; index < card.length; index++) {
        card[index].style.background = 'white';
        card[index].style.color = '#333333c8';
        $(card[index]).removeClass('active-card');
        // card[index].removeClass('active-card');
    }

    var card2 = document.getElementsByClassName('card-receive2');
    var length2 = card2.length;
    
    for (let index2 = 0; index2 < card2.length; index2++) {
        card2[index2].style.background = 'white';
        card2[index2].style.color = '#333333c8';
        $(card[index2]).removeClass('active-card');
    }

    var card3 = document.getElementsByClassName('card-receive3');
    var length3 = card3.length;
    
    for (let index3 = 0; index3 < card3.length; index3++) {
        card3[index3].style.background = 'white';
        card3[index3].style.color = '#333333c8';
        $(card[index3]).removeClass('active-card');
    }

    var pt = document.getElementsByClassName('point');

    var getTotalPoints = $('.point').length,
    getIndex = $(pt[2]).index(),
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $(pt[2]).addClass('point--active');
    $(pt[2]).prevAll().addClass('point--complete');
    $(pt[2]).nextAll().removeClass('point--complete');
  }

    // $(this).css('background', '#37BC9B');
    // $(this).css('color', 'white');
    $(this).addClass('active-card');

    $('#from').css('display', 'block');
});

$('#wallet').click(function () {
   const pound = document.getElementById('pound');
   const nano = document.getElementById('nano');
   const iota = document.getElementById('iota');
   const ball = document.getElementById('ball');

   const pound2 = document.getElementById('pound2');
   const nano2 = document.getElementById('nano2');
   const iota2 = document.getElementById('iota2');
   const ball2 = document.getElementById('ball2');

   if (pound.classList.contains('active-card')) {
        if (nano2.classList.contains('active-card')) {
            window.location.href = "../buy&sell/p-n.html";
        }
        if (iota2.classList.contains('active-card')) {
            window.location.href = "../buy&sell/p-i.html";
        }
        if (ball2.classList.contains('active-card')) {
            window.location.href = "../buy&sell/p-b.html";
        }
    }

   if (nano.classList.contains('active-card')) {
        window.location.href = "../buy&sell/n-p.html";
    }

    if (iota.classList.contains('active-card')) {
        window.location.href = "../buy&sell/i-p.html";
    }

    if (ball.classList.contains('active-card')) {
        window.location.href = "../buy&sell/b-p.html";
    }
});

$('#depo').click(function () {
    window.location.href = "../deposit";
});