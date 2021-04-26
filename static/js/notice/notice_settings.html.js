$(document).ready(function () {
    $("body").css("height", "100%");
    // var elem = document.querySelector('.js-switch');
    // var switchery = new Switchery(elem, {
    //     color: '#1AB394'
    // });

    // var elem_2 = document.querySelector('.js-switch_2');
    // var switchery_2 = new Switchery(elem_2, {
    //     color: '#ED5565'
    // });

    // var elem_3 = document.querySelector('.js-switch_3');
    // var switchery_3 = new Switchery(elem_3, {
    //     color: '#1AB394'
    // });

    $("form").each(function(){
        var tag = "#" + this.id + " input.js-switch";
        var ele = document.querySelector(tag);
        var sw = new Switchery(ele, {
            color: '#1AB394',
            size: 'small',
        });
    });
    $("form").each(function(){
        var tag1 = "#" + this.id + " input.js-check-change";
        var tag2 = "#" + this.id + " div.js-check-change-field";
        var changeCheckbox = document.querySelector(tag1), changeField = document.querySelector(tag2);

        changeCheckbox.onchange = function() {
            changeField.innerHTML = changeCheckbox.checked;
        };
    });
});

var config = {
    '.chosen-select': {},
    '.chosen-select-deselect': {
        allow_single_deselect: true
    },
    '.chosen-select-no-single': {
        disable_search_threshold: 10
    },
    '.chosen-select-no-results': {
        no_results_text: 'Oops, nothing found!'
    },
    '.chosen-select-width': {
        width: "95%"
    }
}
for (var selector in config) {
    $(selector).chosen(config[selector]);
}

$("#ionrange_1").ionRangeSlider({
    min: 0,
    max: 5000,
    type: 'double',
    prefix: "&yen;",
    maxPostfix: "+",
    prettify: false,
    hasGrid: true
});

$("#ionrange_2").ionRangeSlider({
    min: 0,
    max: 10,
    type: 'single',
    step: 0.1,
    postfix: " 克",
    prettify: false,
    hasGrid: true
});

$("#ionrange_3").ionRangeSlider({
    min: -50,
    max: 50,
    from: 0,
    postfix: "°",
    prettify: false,
    hasGrid: true
});

$("#ionrange_4").ionRangeSlider({
    values: [
        "一月", "二月", "三月",
        "四月", "五月", "六月",
        "七月", "八月", "九月",
        "十月", "十一月", "十二月"
    ],
    type: 'single',
    hasGrid: true
});

$("#ionrange_5").ionRangeSlider({
    min: 10000,
    max: 100000,
    step: 100,
    postfix: " km",
    from: 55000,
    hideMinMax: true,
    hideFromTo: false
});

$(".dial").knob();