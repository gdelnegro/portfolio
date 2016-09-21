/**
 * Created by gdelnegro on 21/09/16.
 */
$( "#contactForm" ).submit(function( event ) {
    var form = this;
    $.ajax({
        url: form.action,
        type: "POST",
        dataType: "json",
        data: $(form).serialize(),
        success:function (data) {
            alert(data);
            form.reset();
        },
        error: function (reason) {
            alert(reason);
        }
    });
  event.preventDefault();
});
