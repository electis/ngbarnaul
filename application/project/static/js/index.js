"use strict";

$(window).load(function () {
    //------------------------------------------------------------------------
    //						PRELOADER SCRIPT
    //------------------------------------------------------------------------
    $("#preloader").delay(400).fadeOut("slow");
    $("#preloader .clock").fadeOut();
});

document.addEventListener('DOMContentLoaded', function () {


//------------------------------------------------------------------------
//						OWL CAROUSEL OPTIONS
//------------------------------------------------------------------------

    $('.carousel-single-nav').owlCarousel({
        loop: false,
        margin: 0,
        nav: true,
        autoplay: true,
        autoplayHoverPause: true,
        autoHeight: false,
        items: 1,
        dots: false,
        navText: ['', ''],
        rewind: true
    });


//start spr-countdown
    var $counter_halfbg_timer_countdown = $('#counter-halfbg-timer-countdown');
    $counter_halfbg_timer_countdown.countdown('2019/11/29 23:59:59', function (event) {
        $counter_halfbg_timer_countdown.find('.days').html(event.strftime('%D'));
        $counter_halfbg_timer_countdown.find('.hours').html(event.strftime('%H'));
        $counter_halfbg_timer_countdown.find('.minutes').html(event.strftime('%M'));
        $counter_halfbg_timer_countdown.find('.seconds').html(event.strftime('%S'));
    }).on('finish.countdown', function () {

        }//end finish.countdown
    );//end spr-countdown


//------------------------------------------------------------------------
//						OWL CAROUSEL OPTIONS
//------------------------------------------------------------------------

    $('.carousel-3item-nav-marg').owlCarousel({
        loop: false,
        margin: 120,
        nav: true,
        dots: false,
        navText: ['', ''],
        autoplay: true,
        autoplayHoverPause: true,
        rewind: true,
        responsive: {
            0: {
                items: 1,
                stagePadding: 30
            },
            600: {
                items: 2,
                stagePadding: 30
            },
            1000: {
                items: 3,
                stagePadding: 118
            },
            1600: {
                items: 4,
                stagePadding: 118
            }
        }

    });


//------------------------------------------------------------------------------------
//								CONTACT FORM SCRIPT
//------------------------------------------------------------------------------------

    $('.contact_form').submit(function () {
        // submit the form
        //data area
        var data = [];
        var ctoken = $(this).find('input').val();
        var $fields = $(this).find('.form-group, div.radio');
        $fields.each(function (indx, el) {
            if ($(el).hasClass('radio')) {
                var name = $(el).find('.label-name').html();
                var $radioinput = $(el).find('input');
                $(el).find('input').each(function (indx, el) {
                    if ($(el)[0].checked) {
                        var value = $(el).parent().find('span.lbl').html();
                        data.push({name: name, value: value, name_attr: $radioinput.attr('name')});
                        return;
                    }
                });
            } else if ($(el).find('input').attr('type') === 'checkbox') {
                var $input = $(el).find('input');
                data.push({
                    name: $input.attr('placeholder'),
                    value: $input[0].checked ? 'checked' : 'unchecked',
                    name_attr: $input.attr('name')
                });
            } else if ($(el).find('select')[0]) {
                var name = $(el).find('select option').val();
                var $select = $(el).find('select');
                data.push({name: name, value: $select.val(), name_attr: $select.attr('name')});
            } else if ($(el).find('textarea')[0]) {
                var $textarea = $(el).find('textarea');
                data.push({
                    name: $textarea.attr('placeholder'),
                    value: $textarea.val(),
                    name_attr: $textarea.attr('name')
                });
            } else {
                var $input = $(el).find('input');
                data.push({name: $input.attr('placeholder'), value: $input.val(), name_attr: $input.attr('name')});
            }
        });
        //end data area
        if ($(this).valid()) {
            $(this).find('[type=submit]').button('loading');
            var form = new FormData();
            var $inputFiles = $('.inputfile');
            $inputFiles.each(function (indx, inputFile) {
                $.each(inputFile.files, function (i, file) {
                    form.append('file-' + indx + '-' + i, file);
                });
            });
            var id = this.id;
            form.append('data', JSON.stringify(data));
            form.append('id', id);
            form.append("csrfmiddlewaretoken", ctoken);
            // var action = $(this).attr('action');
            $.ajax({
                url: '/ajax/',
                type: 'POST',
                data: form,
                cache: false,
                contentType: false,
                processData: false,
                success: function () {
                    $('#' + id).find('[type=submit]').button('complete').attr('type', 'button').css('background-color', '#337ab7').css('cursor', 'default');
                    // true; //css('background-color', 'red');
                },
                error: function (response) {
                    // if (response.status === 400) {alert(response.responseText)};
                    $('#' + id).find('[type=submit]').button('reset');
                    alert(response.responseText);
                }
            });
        } else {
            //if data was invalidated
        }
        // $('#'+id).find('[type=submit]').addClass('disabled');
        return false;
    });
});
