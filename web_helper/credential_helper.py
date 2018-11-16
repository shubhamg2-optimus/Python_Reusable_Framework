from web_helper.general_utils import GeneralUtility

class CredentialHelper():

    # EmailId
    valid_email = GeneralUtility.email_generator()

    # Password
    valid_password = GeneralUtility.num_string_generator(8)

    # Username
    username = GeneralUtility.num_string_generator(10)