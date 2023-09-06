$(document).ready(() => {

    // 1
    console.log('cart_display.js -> Start');

    // 2
    let userId = $('#user-id').val();
    console.log('current userID: ' + userId);

    // 3
    $.ajax({
        url: '/orders/ajax_cart_display',
        data: `uid=${userId}`,
        success: (response) => {
            console.log(response.message);
            console.log(response.uid);
            $('#count').text(response.count);
            $('#_count').text(`Товарів: ${response.count} шт`);
            $('#_amount').text(`Вартість: ${response.total} грн`);
        }

    });

});