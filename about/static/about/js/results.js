$(function() {

    function getResults() {
        if ($('.progress').length > 0) {
            $.get('/api/job/' + jobId, function(data) {
                console.log(data);
                if (data.status == 'SUCCESS' || data.status == 'FAILURE') {
                    window.location.reload();
                } else {
                    setTimeout(function () {
                        getResults();
                    }, 1000);
                }
            });
        }
    }

    // Poll to check if job has completed
    getResults();

    // Enable tooltips
    $('[data-toggle="tooltip"]').tooltip();

    $('.nav-properties a').click(function (e) {
        console.log('click!');
        var tab = $(this);
        if(tab.parent('li').hasClass('active')) {
            window.setTimeout(function() {
                console.log(tab.parent().parent().parent());
                tab.parent().parent().parent().find('.tab-pane').removeClass('active');
                tab.parent('li').removeClass('active');
            }, 1);
        }
    });
});
