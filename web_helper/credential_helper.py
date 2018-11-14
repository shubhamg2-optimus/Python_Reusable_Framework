class CredentialHelper():

    # Name
    large_string_name_less_then_50_char = "TestFirstNameofmorelength"
    large_string_name_more_then_50_char = "TestFirstNameOfMoreThanFiftyCharactersTestFirstName"
    special_character_name = "#@*&a%%%"
    name_with_emojis = ":P :-) :)"
    single_char_name = "C"

    # Username
    existing_username = "Harsha"
    invalid_username = "abc"

    # EmailId
    email_without_domain = "test@"
    email_without_extension = "test@moj"
    email__with_invalid_domain = "test@test.test"
    invalid_email = "invalidEmail"
    non_existing_email = "abcd11e@moj.io"
    existing_email = "test_existing_email@moj.io"
    valid_email_for_password_reset = "goelshubham340@gmail.com"

    # Password
    valid_password = "Optimus123"
    invalid_password = "abc"

    # PhoneNumber
    phone_number_less_then_7_digit = "99999"
    phone_number_more_then_15_digit = "999991999991999991"
    phone_number_non_existing = "9874563213"
    valid_phone_number = "919599549586"
    alpha_symbols_phone_number = "aahgsf$%#"
