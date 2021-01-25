# Name: Jennifer Daniels
# Assignment: HW1
# Description: Program test program cred_card_validation for valid inputs


import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """
    Class includes methods for testing various Visa, Mastercard,
    and American Express inputs that should be True
    or False
    """

    # Test below are invalid: correct length, correct prefix, wrong bits
    # These below are being tested to check invalid bits
    # -------------------------------------------------------------------

    def test1(self):
        # test correct prefix 4, correct length 16, incorrect bits
        # Test return True for invalid bits
        self.assertFalse(credit_card_validator("4485169066676962"),
                         msg='credit_card_validator()'.format())

    def test2(self):
        # test correct prefix 51, correct length 16, incorrect bits
        # Test return True for invalid bits
        self.assertFalse(credit_card_validator("5151571872967765"),
                         msg='credit_card_validator()'.format())

    def test3(self):
        # test correct prefix 51, correct length 16, incorrect bits
        # Test return True for invalid bits
        self.assertFalse(credit_card_validator("5547694405358495"),
                         msg='credit_card_validator()'.format())

    def test4(self):
        # test correct prefix 2221, correct length 16, incorrect bits
        # Test return True for invalid bits
        self.assertFalse(credit_card_validator("2221070783784735"),
                         msg='credit_card_validator()'.format())

    def test51(self):
        # test correct prefix 2221, correct length 16, incorrect bits

        # Test return True for invalid bits
        self.assertFalse(credit_card_validator("2720070783784735"),
                         msg='credit_card_validator()'.format())

    def test5(self):
        # test correct prefix 34, correct length 15, incorrect bits
        # Test return True for invalid bits
        self.assertTrue(credit_card_validator("349950866061665"),
                        msg='credit_card_validator()'.format())

    def test6(self):
        # test correct prefix 34, correct length 15, incorrect bits
        # Test return True for invalid bits
        self.assertTrue(credit_card_validator("379950866061662"),
                        msg='credit_card_validator()'.format())

    # Test below are invalid: incorrect length, correct prefix, correct bits
    # These below are being tested to check lower bounds of length
    # ----------------------------------------------------------------------

    def test7(self):
        # test correct prefix 4, incorrect length 15, correct bits
        # Test return True for invalid length
        self.assertTrue(credit_card_validator("453953068855990"),
                        msg='credit_card_validator()'.format())

    def test8(self):
        # test correct prefix 51, incorrect length 15, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("512344611835987"),
                         msg='credit_card_validator()'.format())

    def test9(self):
        # test correct prefix 55, incorrect length 15, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("551379573149391"),
                         msg='credit_card_validator()'.format())

    def test10(self):
        # test correct prefix 2221, incorrect length 15, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("222199444400073"),
                         msg='credit_card_validator()'.format())

    def test11(self):
        # test correct prefix 2720, incorrect length 15, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("272007078378474"),
                         msg='credit_card_validator()'.format())

    def test12(self):
        # test correct prefix 34, incorrect length 14, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("34995086606168"),
                         msg='credit_card_validator()'.format())

    def test13(self):
        # test correct prefix 37, incorrect length 14, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("37995086606165"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid: incorrect length, correct prefix, correct bits
    # These below are being tested to check upper bounds of length
    # ---------------------------------------------------------------------

    def test14(self):
        # test correct prefix 4, incorrect length 17, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("42454570116715256"),
                         msg='credit_card_validator()'.format())

    def test15(self):
        # test correct prefix 51, incorrect length 17, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("51236604924078221"),
                         msg='credit_card_validator()'.format())

    def test16(self):
        # test correct prefix 55, incorrect length 17, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("55292796501342582"),
                         msg='credit_card_validator()'.format())

    def test17(self):
        # test correct prefix 2221, incorrect length 17, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("22210707837847318"),
                         msg='credit_card_validator()'.format())

    def test18(self):
        # test correct prefix 2720, incorrect length 17, correct bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("27200707837847319"),
                         msg='credit_card_validator()'.format())

    def test19(self):
        # test correct prefix 34, incorrect length 16, correct bits
        # Test return True for invalid length
        self.assertTrue(credit_card_validator("3499508660616008"),
                        msg='credit_card_validator()'.format())

    def test20(self):
        # test correct prefix 37, incorrect length 16, correct bits
        # Test return True for invalid length
        self.assertTrue(credit_card_validator("3799508660616005"),
                        msg='credit_card_validator()'.format())

    # Test below are invalid: incorrect length, correct prefix, incorrect bits
    # These below are being tested to check incorrect length and incorrect bits
    # -------------------------------------------------------------------------

    def test21(self):
        # test correct prefix 4, incorrect length 17, incorrect bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("42454570116715255"),
                         msg='credit_card_validator()'.format())

    def test22(self):
        # test correct prefix 51, incorrect length 17, incorrect bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("51236604924078225"),
                         msg='credit_card_validator()'.format())

    def test23(self):
        # test correct prefix 2221, incorrect length 17, incorrect bits
        # Test return True for invalid length
        self.assertFalse(credit_card_validator("22210707837847315"),
                         msg='credit_card_validator()'.format())

    def test24(self):
        # test correct prefix 34, incorrect length 16, incorrect bits
        # Test return True for invalid length
        self.assertTrue(credit_card_validator("3499508660616005"),
                        msg='credit_card_validator()'.format())

    # Test below are invalid: correct length, incorrect prefix, correct bits
    # These below to check lower bounds of prefix
    # ------------------------------------------------------------------------

    def test25(self):
        # test incorrect prefix 39, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3999723232323232"),
                         msg='credit_card_validator()'.format())

    def test26(self):
        # test incorrect prefix 50, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("5001125656567867"),
                         msg='credit_card_validator()'.format())

    def test27(self):
        # test incorrect prefix 2220, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("2220000000000000"),
                         msg='credit_card_validator()'.format())

    def test28(self):
        # test incorrect prefix 33, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("337000000000004"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid: correct length, incorrect prefix, correct bits
    # These below to check upper bounds of prefix
    # ------------------------------------------------------------------------

    def test29(self):
        # test incorrect prefix 5, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("6049264075312233"),
                         msg='credit_card_validator()'.format())

    def test30(self):
        # test incorrect prefix 56, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("5674235971157512"),
                         msg='credit_card_validator()'.format())

    def test31(self):
        # test incorrect prefix 2721, correct length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("2721990000000006"),
                         msg='credit_card_validator()'.format())

    def test32(self):
        # test incorrect prefix 6, correct length 15, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3804926407531225"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid: correct length, incorrect prefix, incorrect bits
    # These below to check incorrect prefix, incorrect bits
    # ------------------------------------------------------------------------

    def test33(self):
        # test incorrect prefix 5, correct length 16, incorrect bits
        # Test return True for invalid prefix, bits
        self.assertFalse(credit_card_validator("5049264075312265"),
                         msg='credit_card_validator()'.format())

    def test34(self):
        # test incorrect prefix 56, correct length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("5674235971157515"),
                         msg='credit_card_validator()'.format())

    def test35(self):
        # test correct prefix 2721, correct length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("2220990000000005"),
                         msg='credit_card_validator()'.format())

    def test36(self):
        # test correct prefix 2721, correct length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("2721990000000005"),
                         msg='credit_card_validator()'.format())

    def test37(self):
        # test incorrect prefix 38, correct length 15, incorrect bits
        # Test return True for invalid prefix, length
        self.assertFalse(credit_card_validator("330008877382085"),
                         msg='credit_card_validator()'.format())

    def test38(self):
        # test incorrect prefix 38, correct length 15, incorrect bits
        # Test return True for invalid prefix, length
        self.assertFalse(credit_card_validator("380008877382085"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid: incorrect length, incorrect prefix, correct bits
    # These below to check incorrect length, incorrect prefix
    # ------------------------------------------------------------------------

    def test39(self):
        # test incorrect prefix 5, incorrect length 17, correct bits
        # Test return True for invalid prefix, length
        self.assertFalse(credit_card_validator("50492640753122681"),
                         msg='credit_card_validator()'.format())

    def test40(self):
        # test incorrect prefix 56, correct length 17, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("56742359711575125"),
                         msg='credit_card_validator()'.format())

    def test41(self):
        # test incorrect prefix 2721, correct length 17, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("22209900000000061"),
                         msg='credit_card_validator()'.format())

    def test42(self):
        # test incorrect prefix 2721, correct length 17, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("27219900000000065"),
                         msg='credit_card_validator()'.format())

    def test43(self):
        # test incorrect prefix 38, incorrect length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3300088773820887"),
                         msg='credit_card_validator()'.format())

    def test44(self):
        # test incorrect prefix 38, incorrect length 16, correct bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3800088773820882"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid: incorrect length, prefix, bits
    # These below to check incorrect length, prefix, bits
    # ------------------------------------------------------

    def test45(self):
        # test incorrect prefix 5, incorrect length 17, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("60492640753122685"),
                         msg='credit_card_validator()'.format())

    def test46(self):
        # test incorrect prefix 56, incorrect length 17, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("50742359711575125"),
                         msg='credit_card_validator()'.format())

    def test47(self):
        # test incorrect prefix 56, incorrect length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("56742359711575155"),
                         msg='credit_card_validator()'.format())

    def test48(self):
        # test incorrect prefix 2721, incorrect length 17, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("27209900000000065"),
                         msg='credit_card_validator()'.format())

    def test49(self):
        # test incorrect prefix 33, incorrect length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3300088773820885"),
                         msg='credit_card_validator()'.format())

    def test50(self):
        # test incorrect prefix 38, incorrect length 16, incorrect bits
        # Test return True for invalid prefix
        self.assertFalse(credit_card_validator("3800088773820885"),
                         msg='credit_card_validator()'.format())

    # Test below are invalid:
    # These below to check for empty string
    # -------------------------------------

    def test51(self):
        # Test below are invalid:
        # These below to check for empty string
        self.assertFalse(credit_card_validator(""),
                         msg='credit_card_validator()'.format())


if __name__ == '__main__':
    unittest.main(verbosity=2)
