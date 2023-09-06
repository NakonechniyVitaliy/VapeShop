
const doCalculate = () => {
    // 1
    let checkedCells = $('.check:checked');
    totalPrice = 0.0;
    selOrdersList = '';

    // 2
    for (cell of checkedCells){
        parentRow = $(cell).parent().parent();
        totalPrice += parseFloat($(parentRow).find('.price-cell').text());
        selOrdersList += $(parentRow).find('.id-cell').text() + ',';
    }
    selOrdersList += totalPrice;

    // 3
    console.log(`totalPrice: ${totalPrice}`);
    console.log(`selOrdersList: ${selOrdersList}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн`);
    $('#bill-btn').attr('href', `/orders/bill/${selOrdersList}`);
};


$(document).ready(() => {
    // 1
    console.log('calc_orders.js -> Start');
    doCalculate();

    // 2
    $('.check').click((event) => {
        console.log('input.check -> Click');
        doCalculate();
    });

});