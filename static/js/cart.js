$(document).ready(() => {

    console.log('cart.js -> Start');

    $('#catalog-panel').on('click', '.add-to-cart-btn', (event) => {
        // 1
        console.log('add-btn -> Click');

        // 2
        const userId = $('#user-id').val();
        console.log('userId -> ' + userId);

        // 3 Блокування корзини для Гостя
        if (userId == 'None'){
            alert('Для використування кошику Ви повинні авторизвуватись!');
            // -> goto signin.html
        } else {
            // 4
            let productId = $(event.target).prev().val();
            console.log('productId -> ' + productId);

            // 5 Дізнаємося ціну товару
            let productPrice = parseFloat($(event.target).parent().prev().find('h4').text());
            console.log('productPrice -> ' + productPrice);

            // AJAX-запит на збереження товару у БД:
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${userId}&pid=${productId}&price=${productPrice}`,
                success: (response) => {
                    console.log('AJAX -> OK / ' + response.message);
                    $('#count').text(response.count);
                    $('#_count').text(`Товарів: ${response.count} шт`);
                    $('#_amount').text(`Вартість: ${response.amount} грн`);
                }
            });
        }
    });

});