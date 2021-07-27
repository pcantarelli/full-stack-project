// Update custom price depending on work type and size selected
$(document).ready(function () {
    // Get selected work type and size price
    let typePrice = $('input[name=work_type]:checked').attr("data-type-price")
    let sizePrice = parseFloat($('#size').find(":selected").attr("data-size-price"))
    let totalPrice = typePrice * sizePrice;
    totalPricetoString = `$ ${totalPrice.toFixed(2)}`;
    $('#custom-price').html(totalPricetoString)
    $('#total-price').val(totalPrice)

    // Function to calculate total price and update in on DOM
    function updateTotalPrice() {
        totalPrice = typePrice * sizePrice;
        totalPricetoString = `$ ${totalPrice.toFixed(2)}`;
        $('#custom-price').html(totalPricetoString)
        $('#total-price').val(totalPrice)
    }

    // Check chande on work type selector
    $('input[name=work_type]').change(function () {
        typePrice = parseFloat($('input[name=work_type]:checked').attr("data-type-price"));
        updateTotalPrice();
    });

    // Check chande on size selector
    $('#size').change(function () {
        sizePrice = parseFloat($(this).find(":selected").attr("data-size-price"));
        updateTotalPrice();
    });
});