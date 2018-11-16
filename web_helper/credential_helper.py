from web_helper.general_utils import GeneralUtility


class CredentialHelper():

    # EmailId
    valid_email = GeneralUtility.email_generator()

    # Password
    valid_password = "Amazon" + GeneralUtility.num_string_generator(3)

    # Username
    username = "test_amazon_" + GeneralUtility.num_string_generator(2)