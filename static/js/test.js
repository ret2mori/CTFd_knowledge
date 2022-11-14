var radio = new Array();
function get_option()
{
    option = Document.getElementsByName(name);
    radio.push(option)
    console.log(radio)

    $.ajax({
        type: 'POST',
        url: 127.0.0.1/,
        data: data,
        dataType: 'json',
        success: function(data) {
        },
        error: function (xhr, type) {
        }

    });
}