class Encryptor:
    @staticmethod
    def xor_encryption_and_decryption(text, key="k"):

        result = ''.join(chr(ord(i) ^ ord(key)) for i in text)

        return result

    # original_text = "sholem laufer \n melech"
    # key = "K"

    # encrypted_text = xor_encryption_and_decryption(original_text, key)
    # print("Encrypted text:", encrypted_text)

    # decrypted_text = xor_encryption_and_decryption(encrypted_text, key)
    # print("Decrypted text:", decrypted_text)

