var value = $( "#msg" ).val();

if (value == "email_or_pass_wrong") {
    swal({
        title: "Invalid Email/Password..!",
        icon: "error",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "input_not_valid") {
    swal({
        title: "Invalid input..!",
        icon: "warning",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "success_login") {
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'login successfully',
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}


else if (value.includes("allready")) {
    swal({
        title: value,
        icon: "error",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "signup_success") {
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'singup successfully',
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "update_success") {
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'update successfully',
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "email_wrong") {
    swal({
        title: "Invalid Email..!",
        icon: "error",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "pass_dont_match") {
    swal({
        title: "Password don't match..!",
        icon: "error",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "otp_missmatch") {
    swal({
        title: "OTP don't match..! Try again",
        icon: "error",
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}

else if (value == "sold_success") {
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'sold item successfully',
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}
else if (value == "add_stock_success") {
    swal({
        position: 'top-end',
        icon: 'success',
        title: 'add item successfully',
        showConfirmButton: false,
        timer: 2500
    });
    $('#msg').remove();
}