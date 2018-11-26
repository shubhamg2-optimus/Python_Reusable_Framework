from web_helper.general_utils import GeneralUtility


class CredentialHelper():

    # EmailId
    random_email = GeneralUtility.email_generator()
    valid_email = "amazon16nov2018@gmail.com"

    # Password
    random_password = "Amazon" + GeneralUtility.num_string_generator(3)
    valid_password = "Amazon123"

    # Username
    random_username = "test_amazon_" + GeneralUtility.num_string_generator(2)
    username = "Test123"