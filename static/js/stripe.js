// STRIPE PAYMENT PROCESSING

/** 
 * JS code copied and pasted from the Code Institute tutorial
**/

$( document ).ready(function() {
    $("#payment-form").submit(function() {
        let form = this;
        let card  = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

        Stripe.createToken(card, function(status, response) {
            if (status === 200) {
                $("#card-errors").hide();
                $("#id_stripe_id").val(response.id);

                $("#id_credit_card_number").removeAttr("name");
                $("#id_cvv").removeAttr("name");
                $("#id_expiry_month").removeAttr("name");
                $("#id_expiry_year").removeAttr("name");

                form.submit();
            } else {
                $("#stripe-error-message").text(response.error.message);
                $("#card-errors").show();
                $("#validate_card_btn").attr("disabled", false);
            }
        });
        return false;
    });
});